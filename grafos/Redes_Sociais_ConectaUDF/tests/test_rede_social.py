# -*- coding: utf-8 -*-
"""Testes automatizados da rede ConectaUDF.

Execução (a partir da pasta ``Redes_Sociais_ConectaUDF``):

    python -m unittest -v
"""
import unittest

from conecta_udf import RedeSocial, rede_ampliada, rede_original
from conecta_udf.relatorio import formatar_caminho, formatar_relatorio

try:  # a comparação com o NetworkX é opcional
    import networkx as nx
except ImportError:  # pragma: no cover
    nx = None


class TestRedeOriginal(unittest.TestCase):
    """Valores do Caderno do Estudante e da apresentação (rede de 6 usuários)."""

    def setUp(self):
        self.rede = rede_original()

    def test_ordem_e_tamanho(self):
        self.assertEqual(self.rede.numero_usuarios, 6)
        self.assertEqual(self.rede.numero_amizades, 8)

    def test_graus(self):
        esperado = {"Ana": 2, "Bruno": 3, "Carla": 3, "Diego": 3, "Elisa": 3, "Felipe": 2}
        self.assertEqual(self.rede.graus(), esperado)

    def test_lema_do_aperto_de_maos(self):
        self.assertEqual(sum(self.rede.graus().values()), 2 * self.rede.numero_amizades)

    def test_usuarios_mais_conectados(self):
        self.assertEqual(self.rede.usuarios_mais_conectados(), ("Bruno", "Carla", "Diego", "Elisa"))

    def test_densidade(self):
        self.assertAlmostEqual(self.rede.densidade(), 16 / 30)
        self.assertEqual(f"{self.rede.densidade():.2%}", "53.33%")

    def test_menor_caminho_ana_felipe(self):
        self.assertEqual(self.rede.menor_caminho("Ana", "Felipe"), ["Ana", "Bruno", "Diego", "Felipe"])
        self.assertEqual(self.rede.distancia("Ana", "Felipe"), 3)

    def test_todos_os_caminhos_minimos(self):
        self.assertEqual(
            self.rede.caminhos_minimos("Ana", "Felipe"),
            [["Ana", "Bruno", "Diego", "Felipe"], ["Ana", "Carla", "Elisa", "Felipe"]],
        )

    def test_caminho_de_um_usuario_para_ele_mesmo(self):
        self.assertEqual(self.rede.menor_caminho("Ana", "Ana"), ["Ana"])

    def test_rede_conexa_e_diametro(self):
        self.assertTrue(self.rede.esta_conexa())
        self.assertEqual(self.rede.diametro(), 3)

    def test_amigos_em_comum(self):
        self.assertEqual(self.rede.amigos_em_comum("Bruno", "Elisa"), ("Carla", "Diego"))

    def test_coeficiente_de_agrupamento(self):
        self.assertEqual(self.rede.coeficiente_de_agrupamento("Ana"), 1.0)   # Bruno e Carla são amigos
        self.assertEqual(self.rede.coeficiente_de_agrupamento("Bruno"), 1 / 3)  # só Ana-Carla entre 3 pares

    def test_proximidade(self):
        # Ana: distâncias 1,1,2,2,3 -> soma 9 -> 5/9
        self.assertAlmostEqual(self.rede.centralidade_de_proximidade("Ana"), 5 / 9)


class TestRedeAmpliada(unittest.TestCase):
    """Desafio em grupo: 4 novos usuários e 6 novas amizades."""

    def setUp(self):
        self.antes = rede_original()
        self.depois = rede_ampliada()

    def test_ordem_e_tamanho(self):
        self.assertEqual(self.depois.numero_usuarios, 10)
        self.assertEqual(self.depois.numero_amizades, 14)

    def test_densidade_diminui(self):
        self.assertAlmostEqual(self.depois.densidade(), 28 / 90)
        self.assertLess(self.depois.densidade(), self.antes.densidade())

    def test_usuario_mais_conectado(self):
        self.assertEqual(self.depois.usuarios_mais_conectados(), ("Diego",))
        self.assertEqual(self.depois.grau("Diego"), 4)

    def test_ampliacao_nao_altera_a_rede_original(self):
        self.assertEqual(self.antes.numero_usuarios, 6)
        self.assertEqual(rede_original().numero_amizades, 8)

    def test_sugestoes_de_amizade(self):
        pares = [(s.usuario_a, s.usuario_b, s.amigos_em_comum) for s in self.depois.sugestoes_de_amizade()]
        self.assertEqual(
            pares,
            [
                ("Bruno", "Elisa", ("Carla", "Diego")),
                ("Carla", "Diego", ("Bruno", "Elisa")),
                ("Diego", "Gabriela", ("Felipe", "Hugo")),
                ("Felipe", "Hugo", ("Diego", "Gabriela")),
            ],
        )

    def test_sugestoes_nunca_sao_amigos_atuais(self):
        for s in self.depois.sugestoes_de_amizade(minimo_em_comum=1):
            self.assertFalse(self.depois.sao_amigos(s.usuario_a, s.usuario_b))


class TestConstrucaoEValidacao(unittest.TestCase):
    def test_amizade_e_reciproca(self):
        rede = RedeSocial(amizades=[("A", "B")])
        self.assertTrue(rede.sao_amigos("A", "B"))
        self.assertTrue(rede.sao_amigos("B", "A"))

    def test_amizade_repetida_nao_duplica_aresta(self):
        rede = RedeSocial(amizades=[("A", "B"), ("B", "A"), ("A", "B")])
        self.assertEqual(rede.numero_amizades, 1)

    def test_laco_e_rejeitado(self):
        with self.assertRaises(ValueError):
            RedeSocial(amizades=[("A", "A")])

    def test_usuario_inexistente(self):
        with self.assertRaises(KeyError):
            rede_original().grau("Zeca")

    def test_lista_de_adjacencia_do_caderno(self):
        rede = RedeSocial.de_lista_de_adjacencia({
            "Ana": ["Bruno", "Carla"],
            "Bruno": ["Ana", "Carla", "Diego"],
            "Carla": ["Ana", "Bruno", "Elisa"],
            "Diego": ["Bruno", "Elisa", "Felipe"],
            "Elisa": ["Carla", "Diego", "Felipe"],
            "Felipe": ["Diego", "Elisa"],
        })
        self.assertEqual(rede.amizades(), rede_original().amizades())

    def test_lista_de_adjacencia_nao_reciproca_e_rejeitada(self):
        with self.assertRaises(ValueError):
            RedeSocial.de_lista_de_adjacencia({"A": ["B"], "B": []})

    def test_lista_de_adjacencia_com_amigo_desconhecido_e_rejeitada(self):
        with self.assertRaises(ValueError):
            RedeSocial.de_lista_de_adjacencia({"A": ["B"]})


class TestRedeDesconexa(unittest.TestCase):
    def setUp(self):
        self.rede = RedeSocial(usuarios=["Solitario"], amizades=[("A", "B"), ("B", "C"), ("X", "Y")])

    def test_sem_caminho(self):
        self.assertIsNone(self.rede.menor_caminho("A", "X"))
        self.assertIsNone(self.rede.distancia("A", "X"))
        self.assertEqual(self.rede.caminhos_minimos("A", "X"), [])

    def test_componentes(self):
        tamanhos = [len(c) for c in self.rede.componentes_conexos()]
        self.assertEqual(tamanhos, [3, 2, 1])
        self.assertFalse(self.rede.esta_conexa())
        self.assertIsNone(self.rede.diametro())

    def test_rede_vazia_e_com_um_usuario(self):
        self.assertEqual(RedeSocial().densidade(), 0.0)
        self.assertEqual(RedeSocial(usuarios=["A"]).densidade(), 0.0)
        self.assertEqual(RedeSocial().usuarios_mais_conectados(), ())


class TestRelatorio(unittest.TestCase):
    def test_formatar_caminho(self):
        self.assertEqual(formatar_caminho(["Ana", "Bruno"]), "Ana → Bruno")
        self.assertEqual(formatar_caminho(None), "(sem caminho)")

    def test_relatorio_contem_metricas_principais(self):
        texto = formatar_relatorio("Teste", rede_original())
        for trecho in ("Total de usuários: 6", "Total de amizades: 8", "53.33%", "Diâmetro: 3"):
            self.assertIn(trecho, texto)


@unittest.skipIf(nx is None, "NetworkX não instalado")
class TestContraNetworkX(unittest.TestCase):
    """Valida as implementações próprias contra uma biblioteca de referência."""

    def _comparar(self, rede):
        grafo = nx.Graph(rede.amizades())
        grafo.add_nodes_from(rede.usuarios)
        self.assertAlmostEqual(rede.densidade(), nx.density(grafo))
        self.assertEqual(rede.graus(), dict(grafo.degree()))
        for usuario in rede.usuarios:
            self.assertAlmostEqual(
                rede.centralidade_de_proximidade(usuario), nx.closeness_centrality(grafo, usuario))
            self.assertAlmostEqual(
                rede.coeficiente_de_agrupamento(usuario), nx.clustering(grafo, usuario))
        self.assertEqual(rede.diametro(), nx.diameter(grafo))
        for a in rede.usuarios:
            for b in rede.usuarios:
                self.assertEqual(rede.distancia(a, b), nx.shortest_path_length(grafo, a, b))
                self.assertEqual(
                    sorted(rede.caminhos_minimos(a, b)), sorted(nx.all_shortest_paths(grafo, a, b)))

    def test_rede_original(self):
        self._comparar(rede_original())

    def test_rede_ampliada(self):
        self._comparar(rede_ampliada())

    def test_rede_desconexa(self):
        rede = RedeSocial(usuarios=["Solitario"], amizades=[("A", "B"), ("B", "C"), ("X", "Y")])
        grafo = nx.Graph(rede.amizades())
        grafo.add_node("Solitario")
        for usuario in rede.usuarios:
            self.assertAlmostEqual(
                rede.centralidade_de_proximidade(usuario), nx.closeness_centrality(grafo, usuario))


if __name__ == "__main__":
    unittest.main()
