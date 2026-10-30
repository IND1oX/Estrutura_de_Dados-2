# Projeto ConectaUDF: análise de redes sociais com grafos

**Disciplina:** Estrutura de Dados II (Unidade III: Grafos)  
**Estudante:** Gustavo Alves  
**Objetivo:** desenvolver uma rede social por meio de um grafo, calculando métricas e analisando as relações entre os usuários.  
**Material:** [Caderno do Estudante](Caderno_do_Estudante_ConectaUDF.md)  
**Código:** pacote [conecta_udf](conecta_udf/) (testes em [tests](tests/); instruções no [README](README.md))  
**Desenho do grafo (Miro):** https://miro.com/app/board/uXjVEYmJPE4=/

---

## 1. Modelagem

A amizade é recíproca; por isso a rede é representada por um **grafo simples não direcionado**, no qual cada vértice é um usuário e cada aresta é uma amizade.

**V** = {Ana, Bruno, Carla, Diego, Elisa, Felipe}  
**E** = {(Ana, Bruno), (Ana, Carla), (Bruno, Carla), (Bruno, Diego), (Carla, Elisa), (Diego, Elisa), (Diego, Felipe), (Elisa, Felipe)}

## 2. Desenho do grafo

O grafo foi desenhado no Miro (quadro "Rede original (6 usuários)"), com seis círculos e oito linhas, uma para cada amizade, sem arestas repetidas. A disposição é a seguinte:

```text
            Bruno ───────── Diego
           /  |               |  \
       Ana    |               |    Felipe
           \  |               |  /
            Carla ───────── Elisa
```

## 3. Graus

| Usuário | Amigos diretos | Grau |
|---|---|---:|
| Ana | Bruno, Carla | 2 |
| Bruno | Ana, Carla, Diego | 3 |
| Carla | Ana, Bruno, Elisa | 3 |
| Diego | Bruno, Elisa, Felipe | 3 |
| Elisa | Carla, Diego, Felipe | 3 |
| Felipe | Diego, Elisa | 2 |

**Pergunta 1: quem tem mais conexões diretas?**  
Bruno, Carla, Diego e Elisa empatam com o maior grau, 3 conexões cada.

## 4. Número de amizades

1. Soma dos graus: 2 + 3 + 3 + 3 + 3 + 2 = **16**
2. Divisão por 2: 16 ÷ 2 = **8**
3. Existem **8 amizades** no grafo, o que coincide com a lista do caderno.

## 5. Densidade

D = 2 × E / (V × (V − 1))

D = 2 × 8 / (6 × (6 − 1)) = 16 / 30

- Resultado decimal: **0,5333**
- Resultado percentual: **53,33 %**

**Interpretação:** a rede possui pouco mais da metade das amizades possíveis (8 de 15). É uma rede de densidade média: há vários triângulos e ciclos, mas nenhum usuário conhece todos os demais, e Ana e Felipe, nas extremidades, só se alcançam por intermediários.

## 6. Representação em Python

A versão básica pedida no Caderno (lista de adjacência e cálculo das métricas) é a seguinte. A versão final, refatorada em módulos e com testes, está descrita na seção 11 e no pacote [conecta_udf](conecta_udf/).

```python
rede = {
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa"],
}
n = len(rede)
soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2
densidade = (2 * arestas) / (n * (n - 1))
```

Saída da execução (rede original):

```text
Ana tem 2 conexoes
Bruno tem 3 conexoes
Carla tem 3 conexoes
Diego tem 3 conexoes
Elisa tem 3 conexoes
Felipe tem 2 conexoes
Total de usuarios: 6
Soma dos graus: 16
Total de amizades: 8
Densidade: 53.33% (0.5333)
```

Os valores calculados pelo programa coincidem com os cálculos manuais das seções 3, 4 e 5 (verificado também por testes automatizados).

## 7. Caminho de Ana até Felipe

`Ana → Bruno → Diego → Felipe`

- Quantidade de arestas no caminho: **3**
- Outro caminho com a mesma quantidade de arestas: `Ana → Carla → Elisa → Felipe`

Não existe caminho com menos de 3 arestas, pois Ana só é amiga de Bruno e Carla, e nenhum dos dois é amigo de Felipe. A busca em largura (`menor_caminho` e `caminhos_minimos`) confirma que a distância é 3 e que há exatamente dois caminhos mínimos.

## 8. Desafio em grupo: rede ampliada

**Novos usuários (4):** Gabriela, Hugo, Iris e Joana.  
**Novas amizades (6):** Felipe–Gabriela, Gabriela–Hugo, Hugo–Iris, Iris–Joana, Joana–Ana e Hugo–Diego.

Os novos dados foram acrescentados em [dados.py](conecta_udf/dados.py) (`rede_ampliada()`), e o desenho está no quadro "Rede ampliada (10 usuários)" do Miro, com os novos usuários em verde.

| Usuário | Grau |
|---|---:|
| Ana | 3 |
| Bruno | 3 |
| Carla | 3 |
| Diego | 4 |
| Elisa | 3 |
| Felipe | 3 |
| Gabriela | 2 |
| Hugo | 3 |
| Iris | 2 |
| Joana | 2 |

- Soma dos graus: **28**; número de arestas: 28 ÷ 2 = **14** (8 antigas + 6 novas).
- Densidade: D = 2 × 14 / (10 × 9) = 28 / 90 = **0,3111 (31,11 %)**.

**Comparação das densidades:** antes, 53,33 %; depois, 31,11 %. A densidade diminuiu porque o número de usuários cresceu de 6 para 10 e o número de pares possíveis subiu de 15 para 45, enquanto as amizades passaram de 8 para apenas 14. Adicionar usuários com poucas conexões dilui a rede.

**Usuário com mais conexões:** Diego, com 4 conexões, pois passou a ser amigo também de Hugo.

**Como a rede poderia recomendar uma nova amizade:** pela quantidade de amigos em comum entre pessoas que ainda não são amigas. O programa lista os pares com pelo menos dois amigos em comum:

| Par sugerido | Amigos em comum |
|---|---|
| Bruno e Elisa | Carla, Diego |
| Carla e Diego | Bruno, Elisa |
| Diego e Gabriela | Felipe, Hugo |
| Felipe e Hugo | Diego, Gabriela |

## 9. Pergunta de reflexão

**Duas pessoas ainda não são amigas, mas têm três amigos em comum. Como essa informação poderia ser usada para sugerir uma nova conexão? Quais cuidados de privacidade devem ser considerados?**

Três amigos em comum indicam que as duas pessoas pertencem à mesma vizinhança do grafo: existem três caminhos de duas arestas entre elas, o que torna provável que se conheçam ou venham a se conhecer. A rede pode ordenar as sugestões pela quantidade de amigos em comum e exibi-las ao usuário como "pessoas que você talvez conheça", exatamente como faz o método `sugestoes_de_amizade` da classe `RedeSocial`.

Quanto à privacidade, é necessário: (a) obter o consentimento do usuário para que sua lista de amigos seja usada em recomendações, em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018); (b) permitir que cada pessoa oculte sua lista de amigos e opte por não ser sugerida; (c) evitar que a sugestão revele relações privadas, por exemplo expor quem são os amigos em comum quando eles preferem não ser identificados, ou sugerir ex-parceiros, agressores ou pessoas bloqueadas; (d) usar apenas os dados necessários, armazená-los com segurança e deixar claro, em linguagem simples, como a recomendação é calculada.

## 10. Conclusão

A representação por grafo permitiu quantificar a rede ConectaUDF por meio do grau, do número de amizades e da densidade, localizar caminhos entre usuários e gerar recomendações a partir de vizinhos em comum. A rede original tem 6 usuários, 8 amizades e densidade de 53,33 %; após a ampliação, 10 usuários, 14 amizades e densidade de 31,11 %.

## 11. Refatoração e boas práticas

A primeira versão do programa era um *script* procedural, com variáveis globais e todos os cálculos misturados com a impressão. Ela funcionava, mas apresentava os seguintes problemas (*code smells*), que motivaram a refatoração:

| Problema na versão inicial | Refatoração aplicada |
|---|---|
| Lógica de grafo, dados e impressão no mesmo arquivo | Separação em módulos: `grafo.py` (estrutura de dados e algoritmos), `dados.py` (dados do Caderno), `relatorio.py` (formatação) e `__main__.py` (programa principal) |
| Dicionário de listas escrito à mão: cada amizade aparece duas vezes e pode ficar inconsistente (A lista B, mas B não lista A) | Classe `RedeSocial` com `adicionar_amizade`, que grava a aresta nos dois sentidos; a lista de adjacência do Caderno é aceita por `de_lista_de_adjacencia`, que **valida** reciprocidade, laços e repetições |
| Listas (`list`) permitiam amizade repetida | Conjuntos (`set`) por usuário: a repetição é impossível por construção |
| Funções que dependiam de variáveis globais | Funções e métodos que recebem tudo por parâmetro e devolvem valores (sem efeitos colaterais) |
| Cálculo misturado com `print` | Métodos retornam valores; `relatorio.py` só monta *strings*, e quem imprime é o `main` |
| Divisão por zero em redes com menos de 2 usuários | `densidade()` trata o caso e devolve 0 |
| Busca de caminho recursiva, que só encontrava caminhos de tamanho fixo | Busca em largura `O(V + E)`, que garante o **menor** caminho, e `caminhos_minimos` para listar todos |
| Sem testes | 33 testes automatizados com `unittest` |
| Sem documentação | *Docstrings* em todo o código, *type hints* e README |

**Decisões de projeto**

- **Lista de adjacência com conjuntos** em vez de matriz de adjacência: o grafo é esparso (8 arestas entre 15 pares possíveis na rede original), a memória é `O(V + E)` e consultar os amigos de um usuário é direto.
- **Determinismo:** os vizinhos são percorridos em ordem alfabética, de modo que o resultado do programa e dos testes é sempre o mesmo.
- **Sem bibliotecas externas** no código principal (apenas a biblioteca padrão), para que o programa rode em qualquer ambiente, inclusive no Google Colab. O NetworkX é usado **somente nos testes**, como referência, e os testes são ignorados se ele não estiver instalado.

**Complexidade dos algoritmos**

| Operação | Complexidade |
|---|---|
| `grau`, `sao_amigos`, `adicionar_amizade` | O(1) em média |
| `densidade`, `numero_amizades`, `graus` | O(V) |
| `menor_caminho`, `distancia`, componentes conexos, proximidade de um usuário | O(V + E) |
| `diametro` | O(V · (V + E)) |
| `sugestoes_de_amizade` | O(V² · grau máximo) |

**Testes.** Os testes conferem (i) os valores do Caderno e da apresentação (ordem 6, tamanho 8, densidade 16/30, caminho Ana → Felipe de 3 arestas e seus dois caminhos mínimos); (ii) propriedades gerais, como o Lema do Aperto de Mãos (soma dos graus = 2E); (iii) casos de borda (rede vazia, usuário isolado, rede desconexa, laços, amizades repetidas, usuário inexistente); e (iv) a concordância de densidade, graus, proximidade, agrupamento, diâmetro e caminhos mínimos com o NetworkX nas redes original, ampliada e desconexa.

## 12. Outras métricas (pergunta da apresentação)

Além de grau, número de arestas e densidade, o programa calcula:

- **Componentes conexos e diâmetro:** a rede original e a ampliada são conexas; o diâmetro vai de 3 para 4 (a maior distância entre dois usuários aumentou com a ampliação).
- **Centralidade de proximidade (*closeness*):** inverso da distância média até os demais usuários. Na rede original, Bruno, Carla, Diego e Elisa têm proximidade 0,714, e Ana e Felipe, 0,556. Na rede ampliada, Diego é o mais próximo dos demais (0,600).
- **Coeficiente de agrupamento:** fração dos pares de amigos de um usuário que também são amigos. Ana e Felipe têm 1,000 (os dois amigos de cada um são amigos entre si), enquanto Bruno, Carla, Diego e Elisa têm 0,333.

**Quem é mais conectado é o mais influente?** Não necessariamente. O grau mede apenas as conexões diretas. Na rede original, quatro usuários empatam em grau 3, e o grau não distingue, por exemplo, uma pessoa cujos amigos formam um grupo fechado (Ana, agrupamento 1,000) de uma que conecta grupos diferentes. A proximidade e o agrupamento descrevem o papel do usuário na estrutura da rede, e uma análise de influência deveria considerar também outras métricas, como a centralidade de intermediação (quantos caminhos mínimos passam pelo usuário), que não foi implementada neste projeto.

## Referência

GOMES, Paulo César Rodacki. **Grafos: conceitos fundamentais, algoritmos e aplicações**. Blumenau: Editora IFC, 2022.
