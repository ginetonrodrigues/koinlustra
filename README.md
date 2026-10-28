# Koinlustra

Skill de ilustrações Koin com referências visuais consultadas diretamente neste repositório.

## Usar sem baixar o acervo

Envie ao seu assistente o link do [SKILL.md](https://raw.githubusercontent.com/ginetonrodrigues/koinlustra/main/SKILL.md) e um pedido, por exemplo:

> Leia a skill Koinlustra neste link e consulte suas referências online. Crie uma versão empty state da carteira, sem notas e moedas, em escala de cinza.

A skill já contém o endereço do catálogo e as regras essenciais. O catálogo e o manifesto apontam para os PNGs por links públicos diretos. O assistente consulta somente as referências relevantes; você não precisa informar uma pasta, baixar os quatro ZIPs antigos ou mesclar diretórios.

Em um aplicativo com instalação de skills, disponibilize o **SKILL.md** usando o mecanismo do aplicativo. Uma vez reconhecido, a chamada pode ser `$koinlustra`. O modo de instalar varia conforme o aplicativo; o repositório não instala nada automaticamente no seu computador.

## O que o assistente precisa conseguir fazer

- Abrir URLs e ler Markdown/JSON.
- Visualizar os PNGs selecionados, não apenas ler o nome do arquivo.
- Usar uma ferramenta de edição/geração para criar a imagem final.

Algumas ferramentas precisam obter uma cópia temporária das imagens escolhidas para enxergá-las ou anexá-las ao gerador. Isso é feito pelo assistente quando suportado, sem download manual de toda a pasta. Se o aplicativo não tiver acesso à internet ou visão, a skill deve explicar o limite e pedir uma referência, sem fingir que consultou o acervo.

## Quatro estados

| Estado | Cor principal | Regra |
| --- | --- | --- |
| Brand | Verde e roxo discreto | Funcionalidade ou ação no estilo Koin |
| Alerta | Laranja | Atenção ou condição pendente |
| Erro | Vermelho | Falha; um check pode virar X quando fizer sentido |
| Empty state | Cinza | Ausência de conteúdo; remover notas, moedas ou outros conteúdos |

O [sistema visual](references/sistema-visual.md) reúne os HEX, traço, composição, perspectiva e ressalvas. A consistência de stroke é regra; **8 px em 1080 px** é uma normalização técnica proposta. A escala HEX de cinzas também é proposta de padronização. Os exemplos não tornam automaticamente aprovados todos os seus detalhes.

## Acervo

- [Catálogo visual](references/catalogo.md)
- [Manifesto com URLs, dimensões e SHA-256](references/asset-manifest.json)
- [Exemplos de pedidos](references/pedidos-e-prompts.md)
- 79 ilustrações individuais, 4 folhas de contato e 2 paletas, total de 85 PNGs.

Inclui exemplos históricos e explorações. As notas do catálogo distinguem a utilidade de cada referência. Regras atuais prevalecem sobre cores de empty states antigos ou gradientes presentes em algumas imagens geradas.

## Uso local opcional

Se preferir trabalhar offline, baixe o ZIP completo pelo GitHub ou clone o repositório. O pacote já contém a estrutura inteira, sem mesclar partes. O nome da pasta externa pode ser `koinlustra-main` ou qualquer outro: a raiz é a pasta que contém `SKILL.md` e `references`; os caminhos das imagens são definidos no manifesto.

O assistente deve resolver os caminhos a partir do local real de `SKILL.md`, nunca de Downloads, do nome da pasta externa ou do diretório atual. Não existe configuração global nem passo de autoexecução oculto.

## Manutenção

Adicione novas imagens e atualize catálogo/manifesto após revisão do time. Mantenha URLs diretas, nomes estáveis e hashes corretos. Os links `main` acompanham a versão atual; para reproduzir um trabalho, fixe a mesma revisão no catálogo e nos PNGs.

Para validar o pacote local com Python 3, execute `python3 scripts/validate_package.py`. O validador não instala nem modifica arquivos.

Acesso público ao repositório não substitui autorização para reutilizar marca e ilustrações em outros contextos. Este pacote não adiciona uma licença de uso aberta.

