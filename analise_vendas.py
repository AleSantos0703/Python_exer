"""Você trabalha no setor de dados de uma loja virtual. O gerente quer entender:

Quais produtos mais venderam

Qual foi o faturamento total por mês

Qual cliente mais gastou"""

#%%
import pandas as pd




def pmv(df : pd.DataFrame):
        produtos_mais_vendidos = df.groupby('product')['quantity'].sum()
        produtos_mais_vendidos = produtos_mais_vendidos.sort_values(ascending=False)
        return print(produtos_mais_vendidos)
        


def fpm(df : pd.DataFrame):
        df['faturamento'] = df['price'] * df['quantity']
        df['date'] = pd.to_datetime(df['date'])
        faturamento_por_mes = df.groupby(df['date'].dt.to_period('M'))['faturamento'].sum()
        return print(faturamento_por_mes)



def cmg(df : pd.DataFrame):
        dsa_df['total'] = dsa_df['price'] * dsa_df['quantity']
        cliente_mais_gastou = dsa_df.groupby('customer')['total'].sum()
        cliente_mais_gastou = cliente_mais_gastou.sort_values(ascending=False)
        return cliente_mais_gastou.head(1)




dsa_df = pd.read_csv(r"./vendas.csv")
print("*************Tabela de vendas***************\n")
print(dsa_df)



print("\n********Produtos mais vendidos*********")
pmv(dsa_df)




print("\n**********Faturamento do mês**********\n")
fpm(dsa_df)



print("\n********Cliente que mais gastou********")
cmg(dsa_df)









# %%
