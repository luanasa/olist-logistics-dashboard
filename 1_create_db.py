import pandas as pd
from sqlalchemy import create_engine

print("Iniciando a criação do Banco de Dados...")

# 1. Cria a "máquina" do banco de dados (SQLite cria um arquivo local)
engine = create_engine('sqlite:///olist.db')

def importar_csv(nome_arquivo, nome_tabela):
    print(f"Lendo {nome_arquivo}...")
    df = pd.read_csv(nome_arquivo)
    df.to_sql(nome_tabela, engine, if_exists='replace', index=False)
    print(f"--> Tabela '{nome_tabela}' criada!")

# 2. Importar as 3 tabelas
importar_csv('olist_orders_dataset.csv', 'orders')
importar_csv('olist_order_reviews_dataset.csv', 'reviews')
importar_csv('olist_customers_dataset.csv', 'customers')

print("\nSucesso! O arquivo 'olist.db' foi gerado.")