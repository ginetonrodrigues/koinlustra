---
name: koinlustra
description: Crie e adapte ilustrações e ícones da Koin usando o acervo visual incluído, com versões brand, alerta, erro e empty state. Use para novos conceitos ou variações de imagens existentes, preservando identidade, traço e composição.
---

# Koinlustra

Crie uma ilustração simples e reconhecível, consistente com os exemplos desta pasta. Entregue um arquivo utilizável, não apenas um prompt. A solicitação atual define o tema, o estado e eventuais exceções.

## Antes de desenhar

1. Leia [o sistema visual](references/sistema-visual.md), especialmente a paleta e as medidas proporcionais.
2. Consulte [o catálogo](references/catalogo.md) e localize o ícone mais próximo do tema. Abra visualmente o arquivo escolhido; ler seu nome não substitui ver a referência.
3. Quando o usuário enviar uma imagem, use essa imagem como alvo principal. Para uma variação de estado, procure também uma referência do estado desejado.
4. Preserve as características do alvo: silhueta, proporções, perspectiva, posição das peças e espessura relativa do contorno. Altere somente o necessário para comunicar o novo estado.
5. Se não existir um ícone adequado, crie do zero a partir da linguagem de um exemplo da mesma família. Se a pasta não estiver acessível, peça uma referência ou acesso aos arquivos. Não diga que consultou exemplos que não abriu.

Os links Markdown são relativos ao documento que os contém. O campo `path` do manifesto é relativo à raiz desta skill, onde fica o SKILL.md. Mantenha esta pasta inteira ao compartilhar ou instalar a skill. O catálogo diferencia acervo anterior, referências fornecidas e explorações recentes; estar no acervo não significa aprovação individual de cada arquivo.

## Escolha o estado

| Estado | Cor e significado | Adaptação |
| --- | --- | --- |
| **Brand** | Verde predominante, roxo discreto, branco e verde escuro de apoio | Representar a funcionalidade ou ação de forma positiva e clara. |
| **Alerta** | Laranja como sinal semântico, superfícies neutras | Atenção ou condição pendente. Usar exclamação somente quando ajudar o significado. |
| **Erro** | Vermelho como sinal semântico, superfícies neutras | Falha real. Trocar check por X quando o objeto e o contexto justificarem essa troca. |
| **Empty state** | Cinzas neutros, branco e contornos cinza-escuros | Ausência de conteúdo ou algo ainda não conquistado. Remover o conteúdo, não sugerir falha. |

Não classifique pelo nome de um arquivo antigo: alguns exemplos anteriores de falha usam laranja. Para novos pedidos, prevalece o mapeamento acima. Não misture laranja e vermelho sem motivo. Um empty state não recebe verde, roxo, laranja ou vermelho por padrão.

## Regras essenciais

- Formas geométricas simples, contornos arredondados e contínuos, peso consistente. Poucos detalhes, reconhecíveis em tamanho pequeno.
- Preenchimentos chapados. Profundidade, quando presente na referência, feita com planos sólidos de cor. Evitar gradientes, brilhos realistas, texturas, ruído e aparência de render 3D.
- Objetos simples podem manter a perspectiva levemente inclinada/3⁄4 dos exemplos. Para cenas complexas com pessoas e vários elementos, preferir vista frontal e composição não isométrica.
- Verde é dominante no estado brand; roxo é apoio discreto. Não preencher metade da cena de roxo por padrão.
- Sem títulos, rótulos, frases, valores ou logotipos não solicitados. Não adicionar elementos alheios à ideia.
- Personagens, se necessários, abstratos, sem codificação explícita de gênero ou raça.
- Uma composição por arquivo, centralizada, quadrada 1:1, com margem. Fundo realmente transparente, não um quadriculado desenhado.
- Meta de entrega: PNG RGBA 1080 × 1080. Verifique dimensões reais; não anuncie esse tamanho se a ferramenta produzir outro. Vetor somente quando solicitado e realmente entregue como vetor.

## Adaptações de estado

**Empty state:** uma carteira fica sem notas e moedas; um porta-vouchers fica vazio; o espaço de uma recompensa pode mostrar um presente fechado sem comemoração. Preserve a identificação do objeto. Tracejado é opcional para indicar um elemento futuro, não obrigatório. Não use X, cadeado, rosto triste ou exclamação como substituto automático de “vazio”.

**Erro:** mantenha o objeto base e substitua o indicador de sucesso por um X legível, com peso e escala equivalentes. Remova o check anterior, inclusive os pequenos. Aplique vermelho nos acentos semânticos. Um X não deve ocupar a composição inteira se o ícone base tiver um pequeno selo.

**Alerta:** mantenha o objeto e use laranja em um sinal de atenção ou detalhe principal. Não transforme todo o ícone em uma placa de aviso se isso destruir a ideia original.

**Brand:** restaure a família verde/roxo e os conteúdos necessários ao conceito. Não adicione check automaticamente a toda ilustração.

Consulte [exemplos de pedidos e modelo de prompt](references/pedidos-e-prompts.md) quando precisar estruturar a geração ou edição.

## Produção e revisão

Use uma ferramenta de edição/geração de imagens disponível para PNGs, anexando o alvo e as referências selecionadas. Se houver SVG editável e o usuário pedir edição vetorial, preserve a estrutura nativa. Não substitua uma imagem por uma simples descrição.

Antes de entregar, abra o resultado e confira:

- O estado é compreensível sem texto? O empty state realmente está vazio?
- A paleta corresponde ao estado e usa os tokens da referência?
- O contorno tem peso uniforme, sem duplicação, cortes ou halos?
- A silhueta e a perspectiva do ícone original foram preservadas?
- Há apenas os elementos necessários? Não sobrou check em uma versão de erro?
- A leitura funciona em aproximadamente 64–96 px, além do tamanho grande?
- Transparência, proporção, margens e dimensões reais foram verificadas?

Se houver desvio importante, corrija-o antes da entrega. Geração por IA pode alterar traços e cores; o texto do prompt não comprova conformidade do arquivo. Medidas exatas de produção precisam de verificação no arquivo final.

Salve versões com nomes claros, por exemplo `carteira-empty-state-cinza.png` ou `pagamento-erro.png`. Preserve o original quando o pedido for uma nova versão. Entregue a imagem e informe apenas observações úteis. Não publique, instale em aplicativos, altere Figma ou compartilhe com terceiros sem pedido correspondente.
