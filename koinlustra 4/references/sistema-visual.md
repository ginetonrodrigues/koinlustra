# Sistema visual e parâmetros

## Hierarquia das referências

1. Pedido atual e imagem-alvo enviada pelo usuário.
2. Regras explícitas deste sistema, principalmente a distinção entre brand, alerta, erro e empty state.
3. Exemplo existente da mesma família visual e estado.
4. Parâmetros operacionais abaixo quando não houver especificação mais precisa.

Não copie defeitos de geração encontrados em exemplos. Um arquivo entregue anteriormente não prova aprovação do usuário nem transforma gradientes ou cores residuais em regra de estilo.

## Paleta brand

| Token | HEX | Aplicação |
| --- | --- | --- |
| brand-primary | `#14DD3E` | Verde principal e superfície dominante |
| brand-secondary | `#10B132` | Plano secundário verde |
| brand-dark | `#085819` | Profundidade, lateral e interior |
| brand-light | `#A1F1B2` | Apoio claro e áreas de menor destaque |
| brand-accent | `#7A5AF8` | Roxo discreto em botão ou detalhe |
| white | `#FFFFFF` | Respiro e superfícies neutras |
| outline | `#0C1114` | Contorno-base observado no ícone de carteira fornecido |

Proveniência: cores visuais da referência brand enviada pelo usuário e dos exemplos produzidos. A carteira-fonte confirma `#14DD3E`, `#085819` e `#7A5AF8` como cores dominantes exatas. Há rótulos HEX inconsistentes na imagem original da paleta brand; não transcrever automaticamente os rótulos dos verdes. Esta tabela consolida a aparência usada no acervo, não substitui uma exportação oficial de tokens da marca. Se o time fornecer tokens oficiais atualizados, priorizá-los e registrar a revisão.

Alguns prompts antigos usam `#101828` para contorno. Não alternar esse tom e `#0C1114` arbitrariamente dentro de uma mesma família. Ao adaptar um ícone, preserve seu contorno; para uma família nova baseada na carteira, use `#0C1114`.

## Cores semânticas

| Estado | Token principal | Origem e uso |
| --- | --- | --- |
| Alerta | `#F79009` | Orange 500 da paleta de alerta fornecida; acento de atenção |
| Erro | `#F04438` | Error 500 da paleta de erro fornecida; acento de falha |
| Empty state | Cinzas neutros | Mapeamento explicitamente solicitado; escala abaixo é padronização operacional |

Use branco e cinzas nas superfícies de alerta/erro, com laranja ou vermelho concentrado no indicador e detalhes relevantes. Preserve a cor semântica como elemento de identificação, sem depender apenas dela: X, exclamação ou composição também devem comunicar o estado quando apropriado.

Para planos mais claros/escuros de alerta e erro, consulte a paleta original incluída. Não invente múltiplos acentos coloridos numa mesma cena. Se precisar de um tom sem token definido, registre-o como derivação, não como cor histórica aprovada.

### Escala neutra proposta para empty states

| Token | HEX | Aplicação |
| --- | --- | --- |
| neutral-white | `#FFFFFF` | Área clara |
| neutral-light | `#E5E5E5` | Face principal clara |
| neutral-base | `#CACACA` | Superfície secundária |
| neutral-mid | `#999999` | Lateral ou detalhe |
| neutral-dark | `#4D4D4D` | Cavidade e profundidade |
| neutral-outline | `#111111` | Contorno estritamente acromático |

**Status:** a escala de cinza foi pedida pelo usuário; estes HEX são uma proposta técnica para tornar a reprodução consistente. Não foram todos aprovados individualmente. São neutros reais, com R=G=B. O contorno quase preto `#0C1114` das referências tem leve componente frio; para o pedido “em escala de cinza”, use `#111111`.

O objetivo não é simplesmente dessaturar um ícone cheio. Ajuste também seu conteúdo ao estado vazio e preserve contraste suficiente entre interior, face e contorno.

## Traço

- Exigência já definida: mesma espessura visual de contorno entre os elementos e entre imagens da mesma família, sem engrossamentos arbitrários.
- **Normalização operacional proposta:** 8 px em uma prancheta de 1080 × 1080, equivalente a aproximadamente 0,74% da largura da prancheta.
- Base observada: a carteira original de 540 × 540 tem cerca de 4 px de traço em trechos isolados quase verticais. O valor de 8 px é uma normalização dessa referência, não uma medida numérica anteriormente aprovada pelo usuário.
- Escale proporcionalmente: `traço = largura_da_prancheta × 8 / 1080`. Exemplos: 4 px em 540; aproximadamente 7,6 px em 1024; 16 px em 2160.
- Usar pontas e junções arredondadas; contornos internos e externos com o mesmo peso-base. Evitar linhas finas decorativas e contornos duplos.
- Em edições, a espessura existente do alvo prevalece sobre redimensionar cegamente para 8 px. O importante é pertencer à mesma família.
- Em raster gerado, a medida é alvo visual, não garantia matemática. Para espessura rigorosa em produção, verifique no desenho final ou em uma versão vetorial autorizada.

## Geometria, composição e profundidade

- Silhuetas geométricas grandes, poucos componentes, cantos arredondados.
- Um conceito por imagem. Somente objetos que ajudem a explicar esse conceito.
- Profundidade curta, com uma ou duas faces secundárias chapadas. Sem luz de estúdio, materiais brilhantes ou render fotorrealista.
- Objetos isolados: seguir a perspectiva do exemplo selecionado, inclusive leve 3/4.
- Cenas complexas: vista frontal, sem isometria e sem visão lateral dominante. Esta regra não proíbe a perspectiva dos ícones simples fornecidos depois.
- Personagens abstratos e inclusivos, sem marcações explícitas de gênero ou raça.
- Padrão de arquivo: quadrado, centralizado, fundo transparente. Como orientação de composição, ocupar aproximadamente 70–80% da prancheta e manter 10–15% de margem por lado; adaptar opticamente a objetos estreitos, sem distorcer proporções.
- Sem textos, rótulos, números financeiros ou marcas adicionais por padrão.

## Limites e precedência

As regras semânticas atuais são: **alerta laranja; erro vermelho; empty state cinza; brand verde e roxo.** Elas prevalecem sobre explorações antigas que tinham presente verde ou voucher laranja para empty states e sobre nomes de arquivos antigos que agrupavam alertas e erros juntos.

Preserve a imagem-alvo ao adaptar. Não transformar uma carteira em uma caixa, um ticket em cartão bancário ou um selo pequeno em objeto principal. Se o pedido exigir mudança radical de metáfora, trate como nova composição.
