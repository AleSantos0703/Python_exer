"""Qual foi o livro mais vendido no total
Qual foi o faturamento total de cada loja?
Qual cliente comprou mais livros (em quantidade)?
"""


import pandas as pd
from pandas import DataFrame
#%%
print("\n*********Dados Atuais*********\n")
df =  pd.read_csv(r"./livraria.csv")
print(df)



print("\n******Livro mais vendido******\n")

livro_mais_vendido = df.groupby('book')['quantity'].sum()
livro_mais_vendido= livro_mais_vendido.sort_values(ascending=False)
print(livro_mais_vendido.head(1))




print("\n*******faturamento total de cada loja*******\n")
df['total'] = df['price'] * df['quantity']
fatura_store = df.groupby('store')['total'].sum()

print(fatura_store)



client_que_mais_compra = df.groupby('customer')['quantity'].sum()
client_que_mais_compra = client_que_mais_compra.sort_values(ascending=False)




print("\n********Cliente que mais comprou********\n")
print(client_que_mais_compra.head(1))






# %%
