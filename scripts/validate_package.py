#!/usr/bin/env python3
"""Validate Koinlustra assets and remote URL mapping without writes or downloads."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import struct
from urllib.parse import quote, unquote, urlsplit

BASE = 'https://raw.githubusercontent.com/ginetonrodrigues/koinlustra/main/'


def validate(root):
    root = Path(root).resolve()
    manifest = json.loads((root / 'references/asset-manifest.json').read_text())
    errors, seen = [], set()
    entries = manifest['entries']
    for entry in entries:
        rel = entry['path']
        parts = PurePosixPath(rel)
        if parts.is_absolute() or '..' in parts.parts or '\\' in rel:
            errors.append(f'Unsafe path: {rel}')
            continue
        if rel in seen:
            errors.append(f'Duplicate path: {rel}')
        seen.add(rel)
        path = root / rel
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root):
            errors.append(f'Missing or unsafe asset: {rel}')
            continue
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry['sha256']:
            errors.append(f'SHA-256 differs: {rel}')
        if data[:8] != b'\x89PNG\r\n\x1a\n' or data[12:16] != b'IHDR':
            errors.append(f'Not a PNG: {rel}')
        elif struct.unpack('>II', data[16:24]) != (entry['width'], entry['height']):
            errors.append(f'Dimensions differ: {rel}')
        if entry.get('url') != BASE + quote(rel, safe='/'):
            errors.append(f'Incorrect remote URL: {rel}')
    if len(entries) != manifest['count']:
        errors.append('Manifest asset count mismatch')
    actual_assets = {str(p.relative_to(root)) for p in (root / 'assets').rglob('*.png')}
    if actual_assets != seen:
        errors.append('Asset tree differs from manifest')
    for doc in root.rglob('*.md'):
        content = doc.read_text()
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if target.startswith(BASE):
                resolved = root / unquote(urlsplit(target).path.split('/main/', 1)[1])
            elif '://' not in target and not target.startswith('#'):
                resolved = doc.parent / target.split('#', 1)[0]
            else:
                continue
            if not resolved.is_file():
                errors.append(f'Broken link in {doc.name}: {target}')
    return errors, len(entries)


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    errors, count = validate(root)
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {count} PNGs, hashes, dimensions, URLs and Markdown links')
