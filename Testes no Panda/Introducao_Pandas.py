from calendar import c
import pandas as pd

# dataframe =  pd.DataFrame()
# DataFrame representa tabela

venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 80], }

vendas = pd.DataFrame(venda)

# print(vendas)
# display(vendas) - Não funciona no VSCODE pois é um item mais gráfico

vendas_df = pd.read_excel(
    'C:\\Users\\bruno\\Projetos Python\\Testes no Panda\\Vendas.xlsx')
# print(vendas_df)

# print(vendas_df.head())
# head() por padrão exibi 5 primeiras linhas, se quiser alterar a qtde é só inserir a número pro método

# print(vendas_df.shape)
# O shape() exibi a quantidade de linhas e colunas

# print(vendas_df.describe())
# describe() te da um resumo das transações desta planilha

produtos = vendas_df['Produto']
# print(produtos)
# Exibi somente a coluna selecionada

produtos_loja = vendas_df[['Produto', 'ID Loja']]
# print(produtos_loja)
# Exibe as duas colunas selecionadas

serie1 = vendas_df.loc[1]
# print(serie1)
# Vai exibir somente a linha 1
# loc[1:5] seleciona esse intervalo

vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja']
                                        == 'Norte Shopping']
# print(vendas_norteshopping_df)

vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja']
                                        == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]
# print(vendas_norteshopping_df)

# O segundo modelo esta exibindo somente as colunas selecionadas

# print(vendas_df.loc[1, 'Produto'])
# Ele deu uma coisa só pq escolheu uma linha só e um produto só

vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
# print(vendas_df)
# Assim está criando uma coluna nova baseado em uma coluna já existente

vendas_df.loc[:, 'Imposto'] = 0
# print(vendas_df)
# Adicionando uma coluna do zero com nenhum valor

vendas_dez_df = pd.read_excel(
    'C:\\Users\\bruno\\Projetos Python\\Testes no Panda\\Vendas - Dez.xlsx')
# print(vendas_dez_df)

# vendas_df = vendas_df.append(vendas_dez_df)
# print(vendas_df)

# vendas_df = vendas_df.drop(1, axis=0)
# print(vendas_df)
# No drop pode fazer ambos caminhos, excluir coluna ou linha
# Primeiro 'eixo' exclui a linha e o segundo a coluna

# vendas_df = vendas_df.dropna(how='all', axis=1)
# Assim vai excluir todas as colunas com o vazio

# vendas_df = vendas_df.dropna()
# Exclui as linhas vazias no automatico

# vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
# preenche todos os valores vazios com a média mean()
# print(vendas_df)

# vendas_df = vendas_df.ffill()
# Preenche a a linha da coluna com o valor de cima

transacoes_loja = vendas_df['ID Loja'].value_counts()
# print(transacoes_loja)
# Conta todas os itens iguais daquela linha da coluna

faturamento_produto = vendas_df[['Produto',
                                 'Valor Final']].groupby('Produto').sum()
# print(faturamento_produto)
# Seleciona as colunas que quer saber o valor e no fim coloca o que fazer com as outras colunas, tbm funciona com outras funções matemáticas

gerentes_df = pd.read_excel(
    'C:\\Users\\bruno\\Projetos Python\\Testes no Panda\\Gerentes.xlsx')
# print(gerentes_df)

vendas_df2 = vendas_df.merge(gerentes_df)
# print(vendas_df)
# Consegue mesclar as duas planilhas pois os gerentes tem o mesmo código das lojas
