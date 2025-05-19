
#%%


import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display





pd.set_option('display.max_columns', None)  
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000) 


# Tabela Atual
dsa = pd.read_csv(r"./dataset.csv")
print("*****************************************Tabela**********************************************\n")
display(dsa.head())

#Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?



print("\n\n\n****************************************Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'***************************************\n\n\n")
office = dsa[dsa['Categoria'] == 'Office Supplies']
vendas_cidade = office.groupby('Cidade')['Valor_Venda'].sum()
vendas_cidade_df = vendas_cidade.sort_values(ascending=False).head(1).reset_index()
vendas_cidade_df.columns = ['Cidade', 'Valor_Venda']
vendas_cidade_df['Valor_Venda'] = vendas_cidade_df['Valor_Venda'].apply(lambda x: f"R$ {x:,.2f}")

display(vendas_cidade_df)




#Qual o Total de Vendas Por Data do Pedido? Demonstre o resultado através de um gráfico de barras.
print("\n\n\n*******************************Total de Vendas por Data***********************************************\n\n\n")
dsa['Data_Pedido'] = pd.to_datetime(dsa['Data_Pedido'],dayfirst=True)
faturamento_por_data = dsa.groupby('Data_Pedido')['Valor_Venda'].sum()
faturamento_por_data_df = faturamento_por_data.reset_index()
faturamento_por_data_df.columns = ['Data do Pedido', 'Total de Vendas']
display(faturamento_por_data_df.head())





fig, ax = plt.subplots(figsize=(12,6))
ax.bar(faturamento_por_data.index, faturamento_por_data.values, color='tab:blue')
ax.set_xlabel('Data do Pedido')
ax.set_ylabel('Total de vendas')
ax.set_title('Total de Vendas por Data')
plt.xticks(rotation=45)  
plt.show()




#Qual o Total de Vendas por Estado? 
print("\n\n\n*********************************Total de vendas por Estado*********************************************\n\n\n")
total_vendas_estado = dsa.groupby('Estado')['Valor_Venda'].sum()
total_vendas_estado_df = total_vendas_estado.reset_index()
total_vendas_estado_df.columns = ['Estado' , 'Total_Vendas']
total_vendas_estado_df['Total_Vendas'] = total_vendas_estado_df['Total_Vendas'].apply(lambda x: f"R$ {x:,.2f}")

display(total_vendas_estado_df)



#Quais São as 10 Cidades com Maior Total de Vendas? 
#Demonstre o resultado através de um gráfico de barras.



print("\n\n\n******************************Top 10 Cidades com Maior número de Vendas**************************************\n\n\n")
vendas_cidade = office.groupby('Cidade')['Valor_Venda'].sum()
top10_cidades = vendas_cidade.sort_values(ascending=False).head(10)
top10_cidades_df = top10_cidades.reset_index()
top10_cidades_df.columns = ['Cidade', 'Total vendas']
top10_cidades_df['Total vendas'] = top10_cidades_df['Total vendas'].apply(lambda x: f"R$ {x:,.2f}")
display(top10_cidades_df)



fig, ax = plt.subplots(figsize=(10,6))
ax.bar(top10_cidades.index, top10_cidades.values, color='tab:blue')
ax.set_xlabel('Cidade')
ax.set_ylabel('Total de Vendas')
ax.set_title('Top 10 Cidades com Maior Total de Vendas')
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()
 
#Qual Segmento Teve o Maior Total de Vendas? 
#Demonstre o resultado através de um gráfico de pizza. 

print("\n\n\n***********************************Segmento com maior número de vendas********************************\n\n\n")
segmento_maior_vendas = dsa.groupby('Segmento')['Valor_Venda'].sum()
segmento_maior_vendas_df = segmento_maior_vendas.reset_index()
segmento_maior_vendas_df.columns = ['Segmento' , 'Número_de_vendas' ]
display(segmento_maior_vendas_df)



labels = segmento_maior_vendas.index.tolist()
sizes = segmento_maior_vendas.values
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.set_title('Total de Vendas por Segmento')
ax.axis('equal') 
plt.show()




#Qual o Total de Vendas Por Segmento e Por Ano?

print("\n\n\n************************************Total de Vendas Por Segmento e Por Ano*******************************\n\n\n")
dsa['Data_Pedido'] = pd.to_datetime(dsa['Data_Pedido'], dayfirst=True)
dsa['Ano'] = dsa['Data_Pedido'].dt.year
seg_year = dsa.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()
seg_year_df = seg_year.reset_index()
seg_year_df.columns = ['Ano', 'Segmento', 'Valor_Venda']
seg_year_df['Valor_Venda'] = seg_year_df['Valor_Venda'].apply(lambda x: f"R$ {x:,.2f}")

display(seg_year_df)




"""Os  gestores  da  empresa  estão  considerando  conceder  diferentes  faixas  de  descontos  e 
gostariam de fazer uma simulação com base na regra abaixo: 
Se o Valor_Venda for maior que 1000 recebe 15% de desconto. 
Se o Valor_Venda for menor que 1000 recebe 10% de desconto. 
Quantas Vendas Receberiam 15% de Desconto? """



 
dsa['valores_maiores_1000'] = dsa['Valor_Venda'] > 1000
quantidade1 = dsa['valores_maiores_1000'].sum()
print("Quantidade de vendas que ganhariam 15% de desconto: " , quantidade1)
dsa['valores_menores_1000'] = dsa['Valor_Venda'] < 1000
quantidade2 = dsa['valores_menores_1000'].sum()
print("Quantidade de vendas que ganhariam 10% de desconto: " , quantidade2)






"""Considere  Que  a  Empresa  Decida  Conceder  o  Desconto  de  15%  do  Item  Anterior.  Qual 
Seria a Média do Valor de Venda Antes e Depois do Desconto?"""

print("\n\n\n**********************Média do Valor de Venda Antes e Depois do Desconto****************************\n\n\n")
dsa['Valores_15'] = dsa['Valor_Venda'] * (0.15 * (dsa['Valor_Venda'] > 1000))
dsa['Com_desconto'] = dsa['Valor_Venda'] - dsa['Valores_15']
print("Média do valor de venda antes do desconto de 15%: ",dsa['Valor_Venda'].mean() )
print("Média do valor de venda depois do desconto de 15%: ",dsa['Com_desconto'].mean())





"""Qual o Média de Vendas Por Segmento, Por Ano e Por Mês? 
Demonstre o resultado através de gráfico de linha."""

print("\n\n\n**********************Média de vendas de segamento por ano****************************\n\n\n")
dsa['Data_Pedido'] = pd.to_datetime(dsa['Data_Pedido'], dayfirst=True)
dsa['Ano'] = dsa['Data_Pedido'].dt.year
Por_ano = dsa.groupby(['Segmento', 'Ano'])['Valor_Venda'].mean().unstack('Segmento')
Por_ano_formatado = Por_ano.applymap(lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
display(Por_ano_formatado)


Por_ano.plot(kind='line', marker='o')
plt.title('Média de Vendas por Segmento e Ano')
plt.xlabel('Ano')
plt.ylabel('Média do Valor de Venda')
plt.grid(True)
plt.legend(title='Segmento')
plt.show()


print("\n\n\n**********************Media de vendas de segamento por mês****************************\n\n\n")
dsa['Data_Pedido'] = pd.to_datetime(dsa['Data_Pedido'], dayfirst=True)
dsa['mês'] = dsa['Data_Pedido'].dt.month
Por_mes = dsa.groupby(['Segmento', 'mês'])['Valor_Venda'].mean().unstack('Segmento')
Por_mes_formatado = Por_mes.applymap(lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
display(Por_mes_formatado)


Por_mes.plot(kind='line', marker='o')
plt.title('Média de Vendas por Segmento e Mês')
plt.xlabel('Mês')
plt.ylabel('Média do Valor de Venda')
plt.grid(True)
plt.legend(title='Segmento')
plt.show()





"""Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 
SubCategorias? 
Demonstre tudo através de um único gráfico. """

print("\n\n\n**********************Total de Vendas Por Categoria e SubCategoria / top 12 Subcategorias****************************\n\n\n")
Total_de_vendas = dsa.groupby(['Categoria' , 'SubCategoria'])['Valor_Venda'].sum()
top12_subcats = Total_de_vendas.sort_values(ascending=False).head(12)
top12_df = top12_subcats.reset_index()
top12_df.columns = ['Categoria', 'SubCategoria', 'Total de Vendas']
top12_df['Total de Vendas'] = top12_df['Total de Vendas'].apply(lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
display(top12_df)






top12_df = top12_subcats.reset_index()
subcats = top12_df['SubCategoria']
x = range(len(subcats))
values = top12_df['Valor_Venda']
categorias = top12_df['Categoria'].unique()
cores = plt.cm.tab10.colors  
color_map = {cat: cores[i % len(cores)] for i, cat in enumerate(categorias)}
colors = top12_df['Categoria'].map(color_map)
plt.figure(figsize=(12,6))
plt.bar(x, values, color=colors)
plt.xticks(x, subcats, rotation=45, ha='right')
plt.xlabel('SubCategoria')
plt.ylabel('Total de Vendas')
plt.title('Top 12 SubCategorias com maior total de vendas por Categoria')
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color_map[cat], label=cat) for cat in categorias]
plt.legend(handles=legend_elements, title='Categoria')
plt.tight_layout()
plt.show()
#%%
