# Koinlustra — kit de ilustração

Material compartilhável para criar e adaptar ilustrações com a mesma linguagem visual.

## O que está incluído

- `SKILL.md`: instruções que o assistente deve seguir.
- `references/sistema-visual.md`: cores, traço, composição, perspectiva e critérios de qualidade.
- `references/pedidos-e-prompts.md`: exemplos de pedidos e adaptação de estados.
- `references/catalogo.md`: índice para localizar os exemplos.
- `references/asset-manifest.json`: inventário técnico e origem das imagens.
- `assets/references/`: 79 ilustrações individuais, 4 folhas de contato e 2 paletas, total de 85 PNGs.

Este é o acervo recuperado para esta entrega. As imagens não foram redesenhadas para o kit. Há exemplos históricos e explorações; o catálogo indica como usá-los. O estado atual prevalece sobre cores antigas: brand verde/roxo, alerta laranja, erro vermelho, empty state cinza.

## Como usar e compartilhar

1. Compartilhe **os quatro arquivos ZIP**, partes 1, 2, 3 e 4. Extraia todos no mesmo local, mesclando a pasta `koinlustra` e preservando sua estrutura. As partes contêm arquivos diferentes e, juntas, formam o kit completo.
2. Em um assistente com suporte a skills, disponibilize a pasta conforme o mecanismo de instalação desse aplicativo. O arquivo de entrada é `SKILL.md`.
3. Em um chat sem instalação de skills, anexe os quatro ZIPs e peça: “Leia o SKILL.md, consulte o catálogo e abra as referências relevantes antes de criar a imagem.” O assistente precisa conseguir extrair e visualizar os arquivos. Se não conseguir, envie o SKILL.md, o sistema visual e as imagens de referência escolhidas.
4. Ao pedir uma variação, indique o arquivo-base e o estado desejado, ou anexe o ícone. Para uma criação do zero, descreva a ideia e o estado.

Exemplo: “Use $koinlustra para transformar o ícone de carteira em empty state, removendo notas e moeda, em escala de cinza.”

Enviar somente o SKILL.md não leva as imagens junto. Este pacote não instala automaticamente a skill no aplicativo de outra pessoa.

## Parâmetros que merecem validação do time

A consistência do traço é uma regra já definida. O número de **8 px em 1080 px** é a normalização técnica proposta a partir do ícone de carteira, não uma medida anteriormente aprovada. A escala HEX de cinzas também é uma proposta de padronização. As referências brand possuem alguns rótulos HEX inconsistentes; o sistema visual explica quais cores foram recuperadas visualmente.

Para trabalhos com exigência rígida de marca, validar estes parâmetros e o arquivo final. A geração por IA pode aproximar cores e traços. As imagens recentes de empty state servem como exemplos de significado, não como garantia de precisão de pixels.

## Atualizar o kit

Depois de uma nova ilustração ser aprovada pelo time, adicione seu PNG à pasta e atualize o catálogo/manifesto. Identifique o estado e a referência-base. Revise a tabela de tokens se houver uma decisão de marca, sem transformar uma exceção pontual em regra geral.
