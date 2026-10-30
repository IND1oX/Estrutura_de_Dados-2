# -*- coding: utf-8 -*-
"""Testes automatizados da solução de BFS e DFS.

Execução (dentro desta pasta):

    python -m unittest -v
"""
import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest import mock

from solucao_grafos import (CONEXOES_PADRAO, CidadeInexistenteError,
                            RedeDeCidades, _perguntar, arestas, formatar_caminho, main)

try:  # a comparação com o NetworkX é opcional
    import networkx as nx
except ImportError:  # pragma: no cover
    nx = None


def eh_caminho_valido(rede, caminho, origem, destino):
    """Confere extremos, ausência de repetição e adjacência de cada passo."""
    return (caminho[0] == origem and caminho[-1] == destino
            and len(set(caminho)) == len(caminho)
            and all(b in rede.vizinhas(a) for a, b in zip(caminho, caminho[1:])))


class TestConstrucao(unittest.TestCase):
    def setUp(self):
        self.rede = RedeDeCidades(CONEXOES_PADRAO)

    def test_ordem_e_tamanho(self):
        self.assertEqual(len(self.rede.cidades), 9)
        self.assertEqual(len(self.rede.conexoes()), 11)

    def test_conexoes_sao_nos_dois_sentidos(self):
        for a, b in CONEXOES_PADRAO:
            self.assertIn(b, self.rede.vizinhas(a))
            self.assertIn(a, self.rede.vizinhas(b))

    def test_lema_do_aperto_de_maos(self):
        soma = sum(self.rede.grau(c) for c in self.rede.cidades)
        self.assertEqual(soma, 2 * len(self.rede.conexoes()))

    def test_conexao_repetida_nao_duplica(self):
        rede = RedeDeCidades([("A", "B"), ("B", "A"), ("A", "B")])
        self.assertEqual(rede.conexoes(), [("A", "B")])

    def test_laco_e_rejeitado(self):
        with self.assertRaises(ValueError):
            RedeDeCidades([("A", "A")])

    def test_cidade_inexistente(self):
        with self.assertRaises(CidadeInexistenteError):
            self.rede.vizinhas("Atlântida")
        with self.assertRaises(CidadeInexistenteError):
            self.rede.bfs("Brasília", "Atlântida")
        with self.assertRaises(CidadeInexistenteError):
            self.rede.dfs("Atlântida", "Curitiba")


class TestBuscas(unittest.TestCase):
    def setUp(self):
        self.rede = RedeDeCidades(CONEXOES_PADRAO)

    def test_bfs_encontra_menor_caminho(self):
        self.assertEqual(self.rede.bfs("Brasília", "Curitiba"),
                         ["Brasília", "Goiânia", "São Paulo", "Curitiba"])

    def test_dfs_encontra_caminho_valido_mas_mais_longo(self):
        caminho = self.rede.dfs("Brasília", "Curitiba")
        self.assertEqual(caminho, ["Brasília", "Goiânia", "Campo Grande",
                                   "Porto Alegre", "Florianópolis", "Curitiba"])
        self.assertTrue(eh_caminho_valido(self.rede, caminho, "Brasília", "Curitiba"))
        self.assertGreater(arestas(caminho), arestas(self.rede.bfs("Brasília", "Curitiba")))

    def test_ordem_dos_vizinhos_muda_a_dfs_e_nao_o_grafo(self):
        # mesma rede, vizinhos de Goiânia cadastrados em outra ordem
        invertida = RedeDeCidades([
            ("Brasília", "Goiânia"), ("Brasília", "Belo Horizonte"),
            ("Goiânia", "São Paulo"), ("Goiânia", "Campo Grande"),
            ("Belo Horizonte", "Rio de Janeiro"), ("Belo Horizonte", "São Paulo"),
            ("Rio de Janeiro", "São Paulo"), ("São Paulo", "Curitiba"),
            ("Campo Grande", "Porto Alegre"), ("Porto Alegre", "Florianópolis"),
            ("Florianópolis", "Curitiba")])
        self.assertEqual(sorted(map(sorted, invertida.conexoes())),
                         sorted(map(sorted, self.rede.conexoes())))
        self.assertNotEqual(invertida.dfs("Brasília", "Curitiba"),
                            self.rede.dfs("Brasília", "Curitiba"))
        self.assertEqual(arestas(invertida.bfs("Brasília", "Curitiba")), 3)

    def test_origem_igual_ao_destino(self):
        self.assertEqual(self.rede.bfs("Brasília", "Brasília"), ["Brasília"])
        self.assertEqual(self.rede.dfs("Brasília", "Brasília"), ["Brasília"])
        self.assertEqual(arestas(["Brasília"]), 0)

    def test_todas_as_cidades_sao_alcancaveis(self):
        for destino in self.rede.cidades:
            self.assertIsNotNone(self.rede.bfs("Brasília", destino))
            self.assertIsNotNone(self.rede.dfs("Brasília", destino))


class TestBloqueios(unittest.TestCase):
    def setUp(self):
        self.rede = RedeDeCidades(CONEXOES_PADRAO)

    def test_bloqueio_nao_altera_a_rede_original(self):
        antes = self.rede.conexoes()
        self.rede.com_bloqueio("Goiânia", "São Paulo")
        self.assertEqual(self.rede.conexoes(), antes)
        self.assertIn("São Paulo", self.rede.vizinhas("Goiânia"))

    def test_bloqueio_remove_nos_dois_sentidos(self):
        bloqueada = self.rede.com_bloqueio("Goiânia", "São Paulo")
        self.assertNotIn("São Paulo", bloqueada.vizinhas("Goiânia"))
        self.assertNotIn("Goiânia", bloqueada.vizinhas("São Paulo"))
        self.assertEqual(len(bloqueada.conexoes()), 10)

    def test_bloqueio_de_conexao_inexistente_nao_muda_nada(self):
        self.assertEqual(self.rede.com_bloqueio("Brasília", "Curitiba").conexoes(),
                         self.rede.conexoes())

    def test_bloqueio_com_cidade_inexistente(self):
        with self.assertRaises(CidadeInexistenteError):
            self.rede.com_bloqueio("Brasília", "Atlântida")

    def test_bloqueio_unico_desvia_a_bfs(self):
        bloqueada = self.rede.com_bloqueio("Goiânia", "São Paulo")
        self.assertEqual(bloqueada.bfs("Brasília", "Curitiba"),
                         ["Brasília", "Belo Horizonte", "São Paulo", "Curitiba"])

    def test_nenhum_bloqueio_unico_isola_brasilia_de_curitiba(self):
        for a, b in self.rede.conexoes():
            rede = self.rede.com_bloqueio(a, b)
            self.assertIsNotNone(rede.bfs("Brasília", "Curitiba"), (a, b))
            self.assertIsNotNone(rede.dfs("Brasília", "Curitiba"), (a, b))

    def test_dois_bloqueios_podem_isolar(self):
        rede = (self.rede.com_bloqueio("Brasília", "Goiânia")
                .com_bloqueio("Brasília", "Belo Horizonte"))
        self.assertIsNone(rede.bfs("Brasília", "Curitiba"))
        self.assertIsNone(rede.dfs("Brasília", "Curitiba"))
        self.assertEqual(formatar_caminho(None), "sem caminho")

    def test_conjuntos_de_corte_minimos(self):
        cortes = self.rede.conjuntos_de_corte("Brasília", "Curitiba", 2)
        self.assertEqual(len(cortes), 5)
        self.assertEqual(self.rede.conjuntos_de_corte("Brasília", "Curitiba", 1), [])
        for grupo in cortes:
            rede = self.rede
            for a, b in grupo:
                rede = rede.com_bloqueio(a, b)
            self.assertIsNone(rede.bfs("Brasília", "Curitiba"))

    def test_bfs_e_dfs_concordam_sobre_existencia_de_caminho(self):
        for a, b in self.rede.conexoes():
            rede = self.rede.com_bloqueio(a, b)
            for c, d in rede.conexoes():
                menor = rede.com_bloqueio(c, d)
                self.assertEqual(menor.bfs("Brasília", "Curitiba") is None,
                                 menor.dfs("Brasília", "Curitiba") is None)


class TestRedeDesconexa(unittest.TestCase):
    def test_sem_caminho_entre_componentes(self):
        rede = RedeDeCidades([("A", "B"), ("C", "D")])
        self.assertIsNone(rede.bfs("A", "D"))
        self.assertIsNone(rede.dfs("A", "D"))

    def test_rede_com_ciclo_nao_entra_em_laco_infinito(self):
        rede = RedeDeCidades([("A", "B"), ("B", "C"), ("C", "A"), ("C", "D")])
        self.assertEqual(rede.bfs("A", "D"), ["A", "C", "D"])
        self.assertTrue(eh_caminho_valido(rede, rede.dfs("A", "D"), "A", "D"))


class TestPrograma(unittest.TestCase):
    def executar(self, *argumentos):
        saida, erro = io.StringIO(), io.StringIO()
        # stdin sem terminal: o programa não pergunta nada e usa os padrões
        with redirect_stdout(saida), redirect_stderr(erro), \
                mock.patch("sys.stdin", io.StringIO("")):
            codigo = main(list(argumentos))
        return codigo, saida.getvalue(), erro.getvalue()

    def test_execucao_padrao(self):
        codigo, saida, _ = self.executar()
        self.assertEqual(codigo, 0)
        self.assertIn("Brasília → Goiânia → São Paulo → Curitiba (3 arestas)", saida)
        self.assertIn("5 arestas", saida)

    def test_origem_inexistente_retorna_erro(self):
        codigo, _, erro = self.executar("--origem", "Atlântida")
        self.assertEqual(codigo, 1)
        self.assertIn("cidade inexistente", erro)

    def test_bloqueios_informados_pelo_usuario(self):
        codigo, saida, _ = self.executar("--bloquear", "Brasília-Goiânia",
                                         "--bloquear", "Brasília-Belo Horizonte")
        self.assertEqual(codigo, 0)
        self.assertIn("sem caminho", saida)

    def test_pergunta_repete_ate_o_nome_existir(self):
        rede = RedeDeCidades(CONEXOES_PADRAO)
        with redirect_stdout(io.StringIO()) as saida, \
                mock.patch("builtins.input", side_effect=["Atlântida", "Goiânia"]):
            cidade = _perguntar(rede, "Origem", "Brasília")
        self.assertEqual(cidade, "Goiânia")
        self.assertIn("Cidade inexistente", saida.getvalue())

    def test_pergunta_vazia_usa_o_padrao(self):
        rede = RedeDeCidades(CONEXOES_PADRAO)
        with mock.patch("builtins.input", return_value=""):
            self.assertEqual(_perguntar(rede, "Origem", "Brasília"), "Brasília")

    def test_bloqueio_em_formato_invalido(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            main(["--bloquear", "semhifen"])


@unittest.skipIf(nx is None, "NetworkX não instalado")
class TestContraNetworkX(unittest.TestCase):
    """O comprimento do caminho da BFS deve coincidir com o do NetworkX."""

    def test_distancias_de_todos_os_pares(self):
        rede = RedeDeCidades(CONEXOES_PADRAO)
        grafo = nx.Graph(CONEXOES_PADRAO)
        for a in rede.cidades:
            for b in rede.cidades:
                self.assertEqual(arestas(rede.bfs(a, b)), nx.shortest_path_length(grafo, a, b))

    def test_conectividade_por_arestas(self):
        grafo = nx.Graph(CONEXOES_PADRAO)
        self.assertEqual(nx.edge_connectivity(grafo, "Brasília", "Curitiba"), 2)


if __name__ == "__main__":
    unittest.main()
