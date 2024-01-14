from processamento_dados import Dados

path_json = 'raw_data/dados_empresaA.json'
path_csv = 'raw_data/dados_empresaB.csv'

# Extract
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print('Nomes de colunas dados_empresaA '
      f'antes do rename: {dados_empresaA.nome_colunas}')
print(f'Quantidade linhas de dados_empresaA: {dados_empresaA.qtd_linhas}')

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print('Nomes de colunas dados_empresaB '
      f'antes do rename: {dados_empresaB.nome_colunas}')
print(f'Quantidade linhas de dados_empresaB: {dados_empresaB.qtd_linhas}')

# Transform
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print('Novos nomes de colunas dados_empresaB '
      f'depois do rename: {dados_empresaB.nome_colunas}')

dados_fusao = Dados.join_data(dados_empresaA, dados_empresaB)
print(f'Nomes de colunas dados_fusao {dados_fusao.nome_colunas}')
print(f'Quantidade linhas de dados_fusao: {dados_fusao.qtd_linhas}')

# Load
path_dados_combinados = 'processed_data/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f'Dados salvos com sucesso em {path_dados_combinados}')
