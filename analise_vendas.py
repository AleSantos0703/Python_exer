"""Você trabalha no setor de dados de uma loja virtual. O gerente quer entender:

Quais produtos mais venderam

Qual foi o faturamento total por mês

Qual cliente mais gastou"""


import pandas as pd
from pandas import DataFrame

dsa_df = pd.read_csv(r"C:\Users\Usuário\Downloads\vendas.csv")
print("*************Tabela de vendas***************\n")
print(dsa_df.head())

produtos_mais_vendidos = dsa_df.groupby('product')['quantity'].sum()

produtos_mais_vendidos = produtos_mais_vendidos.sort_values(ascending=False)
print("\n********Produtos mais vendidos*********")
print(produtos_mais_vendidos)

dsa_df['faturamento'] = dsa_df['price'] * dsa_df['quantity']

dsa_df['date'] = pd.to_datetime(dsa_df['date'])
faturamento_por_mes = dsa_df.groupby(dsa_df['date'].dt.to_period('M'))['faturamento'].sum()

print("\n**********Faturamento do mês**********\n")
print(faturamento_por_mes)


dsa_df['total'] = dsa_df['price'] * dsa_df['quantity']
cliente_mais_gastou = dsa_df.groupby('customer')['total'].sum()
cliente_mais_gastou = cliente_mais_gastou.sort_values(ascending=False)

print("\n********Cliente que mais gastou********")
print(cliente_mais_gastou.head(1))
