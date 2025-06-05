import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

st.title("Bem-vindo! Este é o dataset")

st.write("""
Neste aplicativo Streamlit, você poderá visualizar os dados de venda por produto.
""")

# Carrega o arquivo CSV
df = pd.read_csv(r'home/ubuntu/MS_Financial-Sample.csv', sep=';')
df.columns = df.columns.str.strip()

st.dataframe(df)

# Agrupa os dados por produto e soma as vendas
sales_by_product = df.groupby('Product')['Sales'].sum().reset_index()

# Ordena do maior para o menor
sales_by_product = sales_by_product.sort_values(by='Sales', ascending=True)

# Cria gráfico horizontal e bem maior
fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(sales_by_product['Product'], sales_by_product['Sales'], color='skyblue')
ax.set_xlabel('Vendas', fontsize=12)
ax.set_ylabel('Produto', fontsize=12)
ax.set_title('Vendas por Produto', fontsize=16)

# Formata os valores do eixo X para usar K (milhares) ou M (milhões)
formatter = mticker.FuncFormatter(lambda x, pos: f'{int(x/1000)}K')
ax.xaxis.set_major_formatter(formatter)

# Adiciona linhas de grade horizontais
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()  # Ajusta o layout automático

st.pyplot(fig)
