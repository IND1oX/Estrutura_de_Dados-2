# ConectaUDF: redes sociais, grafos e métricas

Mini projeto de Estrutura de Dados II (Profa. Kadidja Valéria): desenvolver uma rede social modelada como grafo, calcular métricas e analisar as relações entre usuários.

A análise completa (modelagem, cálculos manuais, desafio em grupo, refatoração e respostas às perguntas da apresentação) está em [Analise_RedesSociais.md](Analise_RedesSociais.md). O enunciado está em [Caderno_do_Estudante_ConectaUDF.md](Caderno_do_Estudante_ConectaUDF.md).

## Estrutura

```
Redes_Sociais_ConectaUDF/
├── conecta_udf/
│   ├── __init__.py    # interface pública do pacote
│   ├── __main__.py    # programa principal (linha de comando)
│   ├── grafo.py       # classe RedeSocial: estrutura de dados e algoritmos
│   ├── dados.py       # usuários e amizades do Caderno e do desafio em grupo
│   └── relatorio.py   # funções que montam o texto do relatório
├── tests/
│   └── test_rede_social.py   # testes automatizados (unittest)
├── Analise_RedesSociais.md
└── Caderno_do_Estudante_ConectaUDF.md
```

## Como executar

Requer Python 3.8 ou superior e nenhuma biblioteca externa. Dentro desta pasta:

```bash
python -m conecta_udf                              # relatório completo
python -m conecta_udf --origem Ana --destino Felipe  # escolhe os usuários do caminho
```

## Como testar

```bash
python -m unittest -v
```

Os testes conferem os valores do Caderno e as propriedades do grafo. Se o NetworkX estiver instalado (`pip install networkx`), os resultados também são comparados com a biblioteca; sem ele, esses testes são ignorados.

## Modelo

Grafo simples não direcionado: vértices são usuários e arestas são amizades (recíprocas, sem laços e sem repetições). A representação é uma lista de adjacência `dict[str, set[str]]`.

## Métricas implementadas

| Métrica | Método |
|---|---|
| Grau e usuários mais conectados | `grau`, `graus`, `usuarios_mais_conectados` |
| Número de amizades (lema do aperto de mãos) | `numero_amizades` |
| Densidade `2E / V(V-1)` | `densidade` |
| Menor caminho e todos os caminhos mínimos (busca em largura) | `menor_caminho`, `caminhos_minimos`, `distancia` |
| Componentes conexos e diâmetro | `componentes_conexos`, `diametro` |
| Centralidade de proximidade | `centralidade_de_proximidade` |
| Coeficiente de agrupamento | `coeficiente_de_agrupamento` |
| Recomendação por amigos em comum | `sugestoes_de_amizade` |

## Resultados

| | Rede original | Rede ampliada |
|---|---|---|
| Usuários / amizades | 6 / 8 | 10 / 14 |
| Densidade | 53,33% | 31,11% |
| Diâmetro | 3 | 4 |
| Caminho Ana → Felipe | 3 arestas | 3 arestas |

## Boas práticas aplicadas

- Separação de responsabilidades: dados, lógica, apresentação e programa principal em módulos distintos.
- Funções sem variáveis globais e sem efeitos colaterais; só o programa principal imprime.
- Validação de entrada (laços, reciprocidade, usuário inexistente) e tratamento de casos de borda.
- *Type hints*, *docstrings* e nomes descritivos em português, seguindo a PEP 8.
- Testes automatizados e comparação com uma biblioteca de referência.

## Privacidade

Uma rede social lida com dados pessoais: em um sistema real, a coleta e o uso das conexões dos usuários devem respeitar a LGPD (Lei nº 13.709/2018). Neste projeto todos os nomes são fictícios.
