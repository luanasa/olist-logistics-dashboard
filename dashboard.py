import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Configuração da página 
st.set_page_config(layout="wide", page_title="Logística Olist")

# Conectar ao banco de dados
engine = create_engine('sqlite:///olist.db')

st.title("📦 Olist: Impacto da Logística na Satisfação dos Clientes")

query = """
SELECT 
    o.order_id,
    c.customer_state,
    r.review_score,
    -- Cálculo de dias: Data Entrega - Data Compra
    (julianday(o.order_delivered_customer_date) - julianday(o.order_purchase_timestamp)) as dias_entrega
FROM orders o
JOIN reviews r ON o.order_id = r.order_id
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
  AND dias_entrega IS NOT NULL
"""

# Carregar dados
with st.spinner('Consultando Banco de Dados...'):
    df = pd.read_sql(query, engine)

# Limpeza simples
df['dias_entrega'] = df['dias_entrega'].astype(int)

# -----------------------------------------------------------
# VISUALIZAÇÃO
# -----------------------------------------------------------

# GRÁFICO 1: A Prova Real
st.subheader("1. Quem espera mais, avalia pior?")
st.markdown("*Média de dias de entrega por nota de avaliação (1 a 5)*")

# Agrupar dados
media_por_nota = df.groupby('review_score')['dias_entrega'].mean().reset_index()

fig1 = px.bar(media_por_nota, 
             x='review_score', 
             y='dias_entrega',
             color='dias_entrega',
             color_continuous_scale='rdbu_r', # Vermelho se demorar muito
             text_auto='.1f',
             title="Dias de Entrega vs Nota")
st.plotly_chart(fig1, use_container_width=True)

# GRÁFICO 2: Onde estão os problemas?
st.subheader("2. Ranking de Atraso por Estado")

media_por_estado = df.groupby('customer_state')['dias_entrega'].mean().reset_index()
media_por_estado = media_por_estado.sort_values('dias_entrega', ascending=False) # Do pior pro melhor

fig2 = px.bar(media_por_estado, 
              x='customer_state', 
              y='dias_entrega',
              color='dias_entrega',
              title="Tempo Médio de Entrega por Estado (Sigla)")
st.plotly_chart(fig2, use_container_width=True)