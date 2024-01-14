import unittest
from scripts.processamento_dados import Dados


class TestProcessamentoDados(unittest.TestCase):

    def test_leitura_dados_json(self):
        path_json = 'raw_data/dados_empresaA.json'
        dados = Dados.leitura_dados(path_json, 'json')
        self.assertEqual(dados.qtd_linhas, 3123)
        self.assertEqual(len(dados.nome_colunas), 5)

    def test_leitura_dados_csv(self):
        path_csv = 'raw_data/dados_empresaB.csv'
        dados = Dados.leitura_dados(path_csv, 'csv')
        self.assertEqual(dados.qtd_linhas, 1323)
        self.assertEqual(len(dados.nome_colunas), 6)


if __name__ == '__main__':
    unittest.main()
