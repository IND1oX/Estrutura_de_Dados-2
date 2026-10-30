# Material do Estudante - Prática de Grafos

**Disciplina:** Estrutura de Dados II\
**Unidade III:** Grafos\
**Professora:** Kadidja Valéria\
**Conteúdo-base:** Capítulo 1 - Conceitos Fundamentais\
**Duração prevista:** atividades distribuídas ao longo da aula de 2
horas

------------------------------------------------------------------------

## 1. Objetivos da prática

Ao final das atividades, você deverá ser capaz de:

-   representar problemas utilizando grafos;
-   identificar vértices e arestas;
-   reconhecer incidência e adjacência;
-   diferenciar grafos não dirigidos e grafos dirigidos;
-   determinar ordem, tamanho e grau de vértices;
-   reconhecer laços e arestas paralelas;
-   analisar isomorfismo e subgrafos;
-   construir e conferir sequências de graus;
-   utilizar ferramentas digitais para representar grafos.

------------------------------------------------------------------------

## 2. Orientações gerais

1.  Leia o enunciado antes de iniciar o desenho.
2.  Quando solicitado, registre primeiro os conjuntos de vértices `V` e
    de arestas `E`.
3.  Utilize círculos ou pontos para representar vértices e linhas/setas
    para representar arestas.
4.  Em grafos dirigidos, a seta deve indicar claramente a origem e o
    destino.
5.  Não entregue somente o desenho: apresente também as respostas e
    justificativas solicitadas.
6.  Quando utilizar uma plataforma digital, registre uma captura de tela
    ou o link da atividade.

------------------------------------------------------------------------

## 3. Atividade 1 - Desenhando um grafo

### Proposta

Considere:

`V = {1, 2, 3, 4, 5}`

`E = {(1,2), (1,4), (1,5), (2,3), (3,4), (4,4)}`

### Faça

1.  Desenhe o grafo.
2.  Identifique o número de vértices.
3.  Identifique o número de arestas.
4.  Determine a ordem `|V|`.
5.  Determine o tamanho `|E|`.
6.  Identifique se existe laço.
7.  Determine o grau de cada vértice.

> **Atenção:** a aresta `(4,4)` é um laço. No cálculo do grau, um laço é
> contado duas vezes.

### Plataformas

-   papel e lápis;
-   Graph Online;
-   diagrams.net;
-   Graphviz;
-   Google Colab com Python e NetworkX.

### Resolução

- **Ordem:** |V| = 5
- **Tamanho:** |E| = 6
- **Laço:** sim, a aresta `(4,4)`
- **Graus:**

| Vértice | 1 | 2 | 3 | 4 | 5 |
|---|:-:|:-:|:-:|:-:|:-:|
| Grau | 3 | 2 | 2 | 4 | 1 |

**Grafo:**

<img width="451" height="332" alt="Grafo da Atividade 1" src="https://github.com/user-attachments/assets/5095546d-994c-4b92-993e-6177e0dfe23a" />

------------------------------------------------------------------------

## 4. Atividade 2 - Incidência e adjacência

Utilize o grafo construído na Atividade 1.

### Faça

1.  Liste os vértices adjacentes a cada vértice.
2.  Informe quais arestas são incidentes em cada vértice.
3.  Escolha dois vértices adjacentes e explique por que são considerados
    vizinhos.
4.  Escolha dois vértices não adjacentes e justifique sua resposta.

### Registro

| Vértice | Vértices adjacentes | Arestas incidentes |
|:-:|:-:|:--|
| 1 | 2, 4 e 5 | (1,2), (1,4) e (1,5) |
| 2 | 1 e 3 | (1,2) e (2,3) |
| 3 | 2 e 4 | (2,3) e (3,4) |
| 4 | 1, 3 e 4 | (1,4), (3,4) e (4,4) |
| 5 | 1 | (1,5) |


### Plataformas

-   papel;
-   Graph Online;
-   diagrams.net;
-   quadro colaborativo indicado pela professora.

------------------------------------------------------------------------

## 5. Atividade 3 - Modelagem de uma rede de amizades

Considere quatro pessoas:

**João, Carolina, Maria e Marco.**

### Situação

Crie uma pequena rede de amizades entre essas pessoas.

### Faça

1.  Defina o conjunto de vértices `V`.
2.  Defina o conjunto de arestas `E`.
3.  Desenhe o grafo correspondente.
4.  Informe se o grafo deve ser dirigido ou não dirigido.
5.  Justifique a escolha.
6.  Identifique quem possui maior grau no grafo criado.

### Questão para reflexão

**O que os vértices e as arestas representam nesse problema?**

### Plataformas

-   diagrams.net;
-   Graph Online;
-   Canva;
-   papel;
-   Google Colab com NetworkX.

### Resolução

- **Vértices:** `V = {João, Carolina, Maria, Marco}`
- **Arestas:** `E = {(João, Carolina), (João, Maria), (João, Marco), (Carolina, Maria), (Carolina, Marco), (Maria, Marco)}`
- **Tipo de grafo:** não dirigido, pois a amizade é mútua.

**Grafo:**

<img width="421" height="269" alt="Grafo da rede de amizades" src="https://github.com/user-attachments/assets/276e269d-165b-4eee-8050-3300f44ce835" />

------------------------------------------------------------------------

## 6. Atividade 4 - Modelagem de ruas de mão única

### Situação

Considere um pequeno sistema urbano formado por cruzamentos e ruas de
mão única.

### Faça

1.  Represente cada cruzamento ou ponto relevante por um vértice.
2.  Represente cada rua por uma aresta dirigida.
3.  Utilize setas para indicar o sentido permitido.
4.  Defina os conjuntos `V` e `E`.
5.  Escolha um vértice e determine:
    -   seu grau de entrada;
    -   seu grau de saída.
6.  Explique por que um grafo não dirigido não representa adequadamente
    essa situação.

### Plataformas

-   diagrams.net;
-   Graph Online;
-   Graphviz;
-   Google Colab com NetworkX.

### Resolução

- **Vértices:** `V = {1, 2, 3, 4}`
- **Arestas dirigidas:** `E = {(1,2), (2,3), (3,4), (4,1), (1,3)}`
- **Vértice 3:** grau de entrada 2 e grau de saída 1.
- **Por que um grafo não dirigido não serve:** as ruas são de sentido único, e o grafo não dirigido não representa sentido em suas arestas.

**Grafo:**

<img width="464" height="302" alt="Grafo dirigido das ruas de mão única" src="https://github.com/user-attachments/assets/87468cf1-3f61-4d47-b182-de4f029a052a" />

------------------------------------------------------------------------

## 7. Atividade 5 - Desafio de isomorfismo

### Faça

Dois grafos podem ter desenhos e rótulos diferentes e ainda apresentar a mesma estrutura. Compare os grafos a seguir:

- `G: V = {1, 2, 3, 4}; E = {(1,2), (2,3), (3,4), (4,1)}`
- `H: V = {a, b, c, d}; E = {(a,c), (c,b), (b,d), (d,a)}`

1.  Determine a ordem e o tamanho de cada grafo.
2.  Calcule o grau de cada vértice e escreva a sequência de graus de G e H.
3.  Procure uma correspondência entre os vértices de G e os de H.
4.  Verifique, aresta por aresta, se a correspondência preserva as adjacências.
5.  Conclua se os grafos são isomorfos e justifique.

> Não considere apenas a aparência dos desenhos. Grafos desenhados de
> formas diferentes podem apresentar a mesma estrutura.

### Plataformas

-   papel;
-   Graph Online;
-   diagrams.net.

### Resolução

#### 5.1 Ordem e tamanho

- **Grafo G:** ordem 4 (vértices 1, 2, 3, 4) e tamanho 4 (4 arestas).
- **Grafo H:** ordem 4 (vértices a, b, c, d) e tamanho 4 (4 arestas).

#### 5.2 Grau de cada vértice e sequência de graus

**Grafo G:** `E = {(1,2), (2,3), (3,4), (4,1)}`

| Vértice | Grau | Ligado a |
|:-:|:-:|:-:|
| 1 | 2 | 2 e 4 |
| 2 | 2 | 1 e 3 |
| 3 | 2 | 2 e 4 |
| 4 | 2 | 1 e 3 |

Sequência de graus de G: `(2, 2, 2, 2)`

**Grafo H:** `E = {(a,c), (c,b), (b,d), (d,a)}`

| Vértice | Grau | Ligado a |
|:-:|:-:|:-:|
| a | 2 | c e d |
| b | 2 | c e d |
| c | 2 | a e b |
| d | 2 | a e b |

Sequência de graus de H: `(2, 2, 2, 2)`

#### 5.3 e 5.4 Correspondência e preservação das adjacências

Ambos os grafos têm formato de ciclo com 4 vértices. Percorrendo as arestas: em G, `1 → 2 → 3 → 4 → 1`; em H, `a → c → b → d → a`.

| Vértice em G | Correspondente em H |
|:-:|:-:|
| 1 | a |
| 2 | c |
| 3 | b |
| 4 | d |

#### 5.5 Conclusão e justificativa

Sim, os grafos são **isomorfos**. Eles têm o mesmo número de vértices (ordem 4), o mesmo número de arestas (tamanho 4), a mesma sequência de graus `(2, 2, 2, 2)` e, mais importante, existe uma função bijetora (o mapeamento da tabela acima) que preserva todas as adjacências. Ambos representam o mesmo ciclo.

------------------------------------------------------------------------

## 8. Atividade 6 - Construindo subgrafos

A partir do grafo `G` indicado pela professora, construa **dois
subgrafos diferentes**.

### Para cada subgrafo

1.  informe o conjunto de vértices;
2.  informe o conjunto de arestas;
3.  desenhe o subgrafo;
4.  confirme que seus vértices e arestas pertencem ao grafo original.

### Registro

**Subgrafo G1**

`V1 = { }`

`E1 = { }`

**Subgrafo G2**

`V2 = { }`

`E2 = { }`

### Plataformas

-   Graph Online;
-   diagrams.net;
-   papel;
-   Google Colab com NetworkX.

------------------------------------------------------------------------

## 9. Atividade 7 - Desafio da sequência de graus

Construa um **grafo simples** de acordo com a sequência de graus
indicada pela professora.

### Faça

1.  Crie os vértices necessários.
2.  Adicione as arestas progressivamente.
3.  Calcule o grau de cada vértice.
4.  Organize os graus em ordem não decrescente.
5.  Compare a sequência obtida com a sequência solicitada.
6.  Caso não coincida, revise as arestas.

### Registro

  Vértice     Grau
  --------- ------
            
            
            
**Sequência final de graus:** `( ______________________________ )`

### Plataformas

-   papel;
-   Graph Online;
-   Python/NetworkX no Google Colab.

------------------------------------------------------------------------

### Resolução

#### 7.1 Grafo construído

<img width="328" height="348" alt="Grafo construído na Atividade 7" src="https://github.com/user-attachments/assets/57cb9ec5-9ef9-4cd7-9dbe-aebd23e0fa4a" />

#### 7.2 Tabela de graus obtidos

| Vértice | Grau obtido | Conectado a |
|:-:|:-:|:--|
| A | 6 | B, C, D, E, F, G |
| B | 4 | A, C, D, E |
| C | 4 | A, B, D, H |
| D | 3 | A, B, C |
| E | 3 | A, B, F |
| F | 2 | A, E |
| G | 1 | A |
| H | 1 | C |

#### 7.3 Arestas, sequência e verificação

- **Arestas:** `E = {(A,B), (A,C), (A,D), (A,E), (A,F), (A,G), (B,C), (B,D), (B,E), (C,D), (C,H), (E,F)}`
- **Sequência obtida (ordem não decrescente):** `(1, 1, 2, 3, 3, 4, 4, 6)`
- **Soma dos graus:** 1 + 1 + 2 + 3 + 3 + 4 + 4 + 6 = 24
- **Número de arestas:** 12 (contando os pares de E)
- **Verificação:** a soma dos graus é 24 e 2 × 12 = 24, o que confirma o Lema dos Apertos de Mão.

------------------------------------------------------------------------

## 10. Plataformas recomendadas

### Graph Online

Indicado para construção visual rápida de grafos e exploração das
conexões.

### diagrams.net

Indicado para desenhar grafos, redes, mapas simplificados e modelos de
situações-problema.

### Graphviz

Indicado para representar grafos por meio de uma descrição
textual/código.

### Google Colab + Python/NetworkX

Indicado para relacionar os conceitos da Teoria dos Grafos à
implementação computacional.

### Canva

Pode ser utilizado nas atividades de modelagem predominantemente visual.

### Papel e lápis

Continua sendo uma opção adequada para os exercícios conceituais e para
os primeiros esboços.

------------------------------------------------------------------------

## 11. Entrega das atividades

Ao final da aula, entregue **um único documento** contendo:

-   nome do estudante ou integrantes da dupla;
-   identificação das atividades;
-   desenhos dos grafos;
-   conjuntos `V` e `E`, quando solicitados;
-   cálculos;
-   respostas;
-   justificativas;
-   captura de tela ou link, quando utilizada uma plataforma digital.

------------------------------------------------------------------------

## 12. Checklist de revisão

-   [ ] Identifiquei corretamente vértices e arestas.
-   [ ] Diferenciei grafo dirigido e não dirigido.
-   [ ] Identifiquei incidência e adjacência.
-   [ ] Calculei os graus quando solicitado.
-   [ ] Considerei o laço corretamente no cálculo do grau.
-   [ ] Utilizei setas nos grafos dirigidos.
-   [ ] Justifiquei a análise de isomorfismo.
-   [ ] Identifiquei corretamente os subgrafos.
-   [ ] Conferi a sequência de graus.
-   [ ] Revisei os desenhos e as justificativas.
-   [ ] Registrei a plataforma utilizada.

------------------------------------------------------------------------

## 13. Referência

GOMES, Paulo César Rodacki. **Grafos: conceitos fundamentais, algoritmos
e aplicações**. Blumenau: Editora IFC, 2022.

Material de apoio elaborado a partir do **Capítulo 1 - Conceitos
Fundamentais**.
