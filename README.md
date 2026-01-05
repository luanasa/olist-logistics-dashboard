# 📦 Olist Logistics Analysis: SQL & Dashboards

![Python](https://img.shields.io/badge/Python-Analytics-blue.svg)
![SQL](https://img.shields.io/badge/SQL-Advanced-orange.svg)
![Plotly](https://img.shields.io/badge/Data-Viz-red.svg)

> **Acesse o Dashboard:** [🔗 Link do seu Streamlit Aqui](https://olist-logistics-dashboard-834cmsnmkntpnbmgeuodsb.streamlit.app/)

## 💼 O Desafio de Negócio
A Olist, maior plataforma de e-commerce do Brasil, precisava investigar as causas da insatisfação de clientes. A hipótese da diretoria era de que atrasos logísticos estavam correlacionados com notas baixas (Reviews), mas faltavam dados concretos para provar isso e localizar os gargalos regionais.

## 📊 A Solução
Desenvolvi um Dashboard interativo de Business Intelligence para cruzar dados de vendas, logística e feedback de clientes.

**Principais Insights Descobertos:**
1.  **Correlação Comprovada:** Clientes que avaliam com **Nota 1** esperam, em média, **20.8 dias** pelo produto. Já clientes que dão **Nota 5** recebem em **10.2 dias**. O atraso dobra a chance de insatisfação.
2.  **Gargalos Regionais:** O dashboard mapeia os estados com maior tempo médio de entrega, permitindo ações corretivas focadas geograficamente.

## 🛠️ Tech Stack & Metodologia
* **SQL (SQLAlchemy):** Modelagem de dados e queries complexas (`JOINs`, agregação e cálculo de datas `JulianDay` direto no banco) para performance.
* **Python (Pandas):** Refinamento e tratamento de dados.
* **Plotly:** Visualização de dados interativa para exploração pelo usuário final.
* **Streamlit:** Framework para publicação do Data App.

## 📂 Estrutura do Projeto
O projeto simula um pipeline de ELT (Extract, Load, Transform):
1.  `1_create_db.py`: Ingestão de arquivos CSV brutos para um Data Warehouse SQL local.
2.  `dashboard.py`: Conexão com o banco, execução de queries analíticas e renderização dos KPIs.

---
## 👩‍💻 Autora
**Luana Sá**
[LinkedIn](https://www.linkedin.com/in/luamartins/) 
