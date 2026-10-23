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

------------------------------------------------------------------------
> Ordem |V| = 5.
> Tamanho |E| = 6.
> Grau do vértice 1 = 3.
> Grau do vértice 2 = 2.
> Grau do vértice 3 = 2.
> Grau do vértice 4 = 4.
> Grau do vértice 5 = 1.
>
<img width="451" height="332" alt="ex01" src="https://github.com/user-attachments/assets/5095546d-994c-4b92-993e-6177e0dfe23a" />

-------------------------------------------------------------------------


## 4. Atividade 2 - Incidência e adjacência

Utilize o grafo construído na Atividade 1.

### Faça

1.  Liste os vértices adjacentes a cada vértice.
2.  Informe quais arestas são incidentes em cada vértice.
3.  Escolha dois vértices adjacentes e explique por que são considerados
    vizinhos.
4.  Escolha dois vértices não adjacentes e justifique sua resposta.

### Registro


|  Vértice | Vértices adjacentes | Arestas incidentes |
| :--- | :---: | ---: |
|1  | 2, 4 e 5 | (1,2), (1,4) e (1,5) |
|2  | 1 e 3  | (1,2) e (2,3) |
|3   | 2 e 4  |  (2,3) e (3,4)|
|4 |  1, 3 e 4 | (1,4), (3,4) e (4,4)|
|5| 1 | (1,5)|


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

------------------------------------------------------------------------
> V = {João, Carolina, Maria, Marco} E = {(João, Carolina), (João, Maria), (João, Marco), (Carolina, Maria), (Carolina, Marco), (Maria, Marco)} O > grafo é não dirigido pois a amizade é mútua.
<img width="421" height="269" alt="image" src="https://github.com/user-attachments/assets/276e269d-165b-4eee-8050-3300f44ce835" />

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

------------------------------------------------------------------------
> V = {1, 2, 3, 4} E = {(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)} Vértice 3: Grau de entrada 2, grau de saída 1 O grafo não dirigido não se
> enquadra essa situação pois as ruas são de sentido único. O grafo não dirigido não representa sentido em suas arestas.
<img width="464" height="302" alt="image" src="https://github.com/user-attachments/assets/87468cf1-3f61-4d47-b182-de4f029a052a" />

------------------------------------------------------------------------
## 7. Atividade 5 - Desafio de isomorfismo

### Faça

Dois grafos podem ter desenhos e rótulos diferentes e ainda apresentar a mesma estrutura. Compare os
grafos a seguir:
G: V = {1, 2, 3, 4}; E = {(1,2), (2,3), (3,4), (4,1)}
H: V = {a, b, c, d}; E = {(a,c), (c,b), (b,d), (d,a)}
O que fazer
1. Determine a ordem e o tamanho de cada grafo.
2. Calcule o grau de cada vértice e escreva a sequência de graus de G e H.
3. Procure uma correspondência entre os vértices de G e os de H.
4. Verifique, aresta por aresta, se a correspondência preserva as adjacências.
5. Conclua se os grafos são isomorfos e justifique.

### Registro sugerido

  |Vértice do grafo G |  Vértice correspondente no grafo H|
 
                       
            
> Não considere apenas a aparência dos desenhos. Grafos desenhados de
> formas diferentes podem apresentar a mesma estrutura.

### Plataformas

-   papel;
-   Graph Online;
-   diagrams.net.

-------------------------------------------------------------------------------------
5.1- 
Ordem e Tamanho
Grafo G: Ordem é 4 (possui os vértices 1, 2, 3, 4) e o Tamanho é 4 (possui 4 arestas).
Grafo H: Ordem é 4 (possui os vértices a, b, c, d) e o Tamanho é 4 (possui 4 arestas).
-------------------------------------------------------------------------------------
5.2-
Grau de cada vértice e sequência de graus
Grafo G: O conjunto de arestas é {(1,2), (2,3), (3,4), (4,1)}.   
Grau do vértice 1: 2 (ligado a 2 e 4)
Grau do vértice 2: 2 (ligado a 1 e 3)
Grau do vértice 3: 2 (ligado a 2 e 4)
Grau do vértice 4: 2 (ligado a 1 e 3)
Sequência de graus de G: (2, 2, 2, 2)

Grafo H: O conjunto de arestas é {(a,c), (c,b), (b,d), (d,a)}.   
Grau do vértice a: 2 (ligado a c e d)
Grau do vértice b: 2 (ligado a c e d)
Grau do vértice c: 2 (ligado a a e b)
Grau do vértice d: 2 (ligado a b e a)
Sequência de graus de H: (2, 2, 2, 2)
--------------------------------------------------------------------------------------------------------
5.3 e 5.4-
Correspondência e preservação das adjacências
Ao analisar a estrutura, ambos são grafos em formato de ciclo com 4 vértices.
Podemos mapear caminhando pelas arestas: em G, partimos de 1 -> 2 -> 3 -> 4 -> 1; em H, partimos de a -> c -> b -> d -> a.

|Vértice em G      |      Correspondente em H|
|1                 |              a|
|2                 |              c|
|3                 |              b|
|4                 |              d|

----------------------------------------------------------------------------------------------------------
5.5-
Conclusão e Justificativa
Sim, os grafos são isomorfos.
A justificativa é que eles possuem o mesmo número de vértices (ordem 4), o mesmo número de arestas (tamanho 4), a mesma sequência de graus (2, 2, 2, 2) e, mais importante, é possível estabelecer uma 
função bijetora (o mapeamento da tabela acima) que preserva perfeitamente todas as adjacências originais de ambos os grafos. Ambos representam um ciclo idêntico.

-------------------------------------------------------------------------------------------------------

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

<img width="328" height="348" alt="graphviz" src="https://github.com/user-attachments/assets/57cb9ec5-9ef9-4cd7-9dbe-aebd23e0fa4a" /> 

------------------------------------------------------------------------
7.2-
Tabela de Graus Obtidos
De acordo com a construção acima, preenchemos a tabela:
|Vértice           |     Grau obtido|
|A                 |     6 (conectado a B, C, D, E, F, G)|
|B                 |     4 (conectado a A, C, D, E)|
|C                 |     4 (conectado a A, B, D, H)|
|D                 |     3 (conectado a A, B, C)|
|E                 |     3 (conectado a A, B, F)|
|F                 |     2 (conectado a A, E)|
|G                 |     1 (conectado a A)|
|H                 |     1 (conectado a C)|

--------------------------------------------------------------------------
7.3-
Conjunto de arestas E:
E = {(A,B), (A,C), (A,D), (A,E), (A,F), (A,G), (B,C), (B,D), (B,E), (C,D), (C,H), (E,F)}
Sequência obtida:
(1, 1, 2, 3, 3, 4, 4, 6) (ordenada de forma não decrescente, conforme solicitado).
Soma dos graus:1 + 1 + 2 + 3 + 3 + 4 + 4 + 6 = 24
Número de arestas:Contando os pares no conjunto E, temos 12 arestas.
A soma dos graus é 24. Duas vezes o número de arestas é 2 X 12 = 24. 
Isso comprova o Teorema do Aperto de Mãos (ou Lema dos Apertos de Mão).

----------------------------------------------------------------------------

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
