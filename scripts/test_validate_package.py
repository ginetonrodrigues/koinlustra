#!/usr/bin/env python3
"""Small regression tests for portable paths and validation failures."""
import hashlib
import json
import os
from pathlib import Path
import struct
import tempfile
import unittest
from urllib.parse import quote
import zlib

from validate_package import BASE, validate


def png():
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 6, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(b'\0\0\0\0\0')) + chunk(b'IEND', b'')


class PackageValidation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'qualquer nome-main com espaços'
        (self.root / 'references').mkdir(parents=True)
        (self.root / 'assets').mkdir()
        self.rel = 'assets/ícone com espaço.png'
        self.data = png()
        (self.root / self.rel).write_bytes(self.data)
        self.entry = {'path': self.rel, 'url': BASE + quote(self.rel, safe='/'), 'width': 1, 'height': 1, 'sha256': hashlib.sha256(self.data).hexdigest()}
        self.manifest = {'count': 1, 'entries': [self.entry]}
        self.write()
        (self.root / 'SKILL.md').write_text('[imagem](' + self.entry['url'] + ')')

    def write(self):
        (self.root / 'references/asset-manifest.json').write_text(json.dumps(self.manifest))

    def tearDown(self):
        self.temp.cleanup()

    def test_arbitrary_root_and_current_directory(self):
        cwd = os.getcwd()
        try:
            os.chdir(self.temp.name)
            self.assertEqual(validate(self.root)[0], [])
        finally:
            os.chdir(cwd)

    def test_encoded_url(self):
        self.assertIn('%20', self.entry['url'])
        self.assertIn('%C3%AD', self.entry['url'])
        self.assertEqual(validate(self.root)[0], [])

    def test_missing_reference(self):
        (self.root / self.rel).unlink()
        self.assertTrue(any('Missing' in x for x in validate(self.root)[0]))

    def test_modified_reference(self):
        (self.root / self.rel).write_bytes(self.data + b'changed')
        self.assertTrue(any('SHA-256' in x for x in validate(self.root)[0]))

    def test_path_traversal_rejected(self):
        self.entry['path'] = '../outside.png'; self.write()
        self.assertTrue(any('Unsafe path' in x for x in validate(self.root)[0]))

    def test_wrong_url_rejected(self):
        self.entry['url'] = 'https://example.invalid/image.png'; self.write()
        self.assertTrue(any('Incorrect remote URL' in x for x in validate(self.root)[0]))

    def test_unlisted_image_rejected(self):
        (self.root / 'assets/extra.png').write_bytes(self.data)
        self.assertTrue(any('tree differs' in x for x in validate(self.root)[0]))

    def test_broken_document_link_rejected(self):
        (self.root / 'SKILL.md').write_text('[absent](references/missing.md)')
        self.assertTrue(any('Broken link' in x for x in validate(self.root)[0]))


if __name__ == '__main__':
    unittest.main()
