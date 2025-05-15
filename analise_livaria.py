"""Qual foi o livro mais vendido no total
Qual foi o faturamento total de cada loja?
Qual cliente comprou mais livros (em quantidade)?
"""

#%%
import pandas as pd
from pandas import DataFrame



def lmv(df1 : pd.DataFrame):
    livro_mais_vendido = df1.groupby('book')['quantity'].sum()
    livro_mais_vendido= livro_mais_vendido.sort_values(ascending=False)
    return print(livro_mais_vendido.head(1))


def ftcl(df1 : pd.DataFrame):
    df1['total'] = df1['price'] * df1['quantity']
    fatura_store = df1.groupby('store')['total'].sum()
    print(fatura_store)


def cmc(df1 : pd.DataFrame):

    client_que_mais_compra = df1.groupby('customer')['quantity'].sum()
    client_que_mais_compra = client_que_mais_compra.sort_values(ascending=False)
    return print(client_que_mais_compra.head(1))




print("\n*********Dados Atuais*********\n")
df =  pd.read_csv(r"./livraria.csv")
print(df)




print("\n******Livro mais vendido******\n")
lmv(df)




print("\n*******faturamento total de cada loja*******\n")
ftcl(df)




print("\n********Cliente que mais comprou********\n")
cmc(df)











# %%
