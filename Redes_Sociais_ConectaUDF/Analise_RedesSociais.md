# Projeto ConectaUDF: análise de redes sociais com grafos

**Disciplina:** Estrutura de Dados II (Unidade III: Grafos)  
**Estudante:** Gustavo Alves  
**Objetivo:** desenvolver uma rede social por meio de um grafo, calculando métricas e analisando as relações entre os usuários.  
**Material:** [Caderno do Estudante](Caderno_do_Estudante_ConectaUDF.md)  
**Código:** [conecta_udf.py](conecta_udf.py)  
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

O código completo, com validações, está em [conecta_udf.py](conecta_udf.py). A lista de adjacência e o cálculo das métricas são:

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

Os valores calculados pelo programa coincidem com os cálculos manuais das seções 3, 4 e 5.

## 7. Caminho de Ana até Felipe

`Ana → Bruno → Diego → Felipe`

- Quantidade de arestas no caminho: **3**
- Outro caminho com a mesma quantidade de arestas: `Ana → Carla → Elisa → Felipe`

Não existe caminho com menos de 3 arestas, pois Ana só é amiga de Bruno e Carla, e nenhum dos dois é amigo de Felipe. A busca em largura do programa confirma que a distância é 3.

## 8. Desafio em grupo: rede ampliada

**Novos usuários (4):** Gabriela, Hugo, Iris e Joana.  
**Novas amizades (6):** Felipe–Gabriela, Gabriela–Hugo, Hugo–Iris, Iris–Joana, Joana–Ana e Hugo–Diego.

A lista de adjacência foi atualizada no programa (variável `rede2`), e o desenho está no quadro "Rede ampliada (10 usuários)" do Miro, com os novos usuários em verde.

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

Três amigos em comum indicam que as duas pessoas pertencem à mesma vizinhança do grafo: existem três caminhos de duas arestas entre elas, o que torna provável que se conheçam ou venham a se conhecer. A rede pode ordenar as sugestões pela quantidade de amigos em comum e exibi-las ao usuário como "pessoas que você talvez conheça", exatamente como faz a função `recomendar` do programa.

Quanto à privacidade, é necessário: (a) obter o consentimento do usuário para que sua lista de amigos seja usada em recomendações, em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018); (b) permitir que cada pessoa oculte sua lista de amigos e opte por não ser sugerida; (c) evitar que a sugestão revele relações privadas, por exemplo expor quem são os amigos em comum quando eles preferem não ser identificados, ou sugerir ex-parceiros, agressores ou pessoas bloqueadas; (d) usar apenas os dados necessários, armazená-los com segurança e deixar claro, em linguagem simples, como a recomendação é calculada.

## 10. Conclusão

A representação por grafo permitiu quantificar a rede ConectaUDF por meio do grau, do número de amizades e da densidade, localizar caminhos entre usuários e gerar recomendações a partir de vizinhos em comum. A rede original tem 6 usuários, 8 amizades e densidade de 53,33 %; após a ampliação, 10 usuários, 14 amizades e densidade de 31,11 %.

## Referência

GOMES, Paulo César Rodacki. **Grafos: conceitos fundamentais, algoritmos e aplicações**. Blumenau: Editora IFC, 2022.
