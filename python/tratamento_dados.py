
import pandas as pd
from sqlalchemy import create_engine
import urllib

# Ler CSV usando ;
df = pd.read_csv("../dados/vendas.csv", sep=";")

# Mostrar colunas
print(df.columns)

# Criar coluna total
df["Total"] = df["Quantidade"] * df["Valor"]

# Mostrar dados
print(df)

# Salvar arquivo tratado
df.to_csv("../dados/vendas_tratado.csv", index=False, sep=";")

print("Tratamento concluído!")



# Faturamento total
faturamento_total = df["Total"].sum()
print("\nFaturamento Total:", faturamento_total)

# Produto mais vendido
mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()
print("Produto Mais Vendido:", mais_vendido)

# Vendas por região
vendas_regiao = df.groupby("Regiao")["Total"].sum()
print("\nVendas por Região:")
print(vendas_regiao)


# Mostrar dados
print(df)

# Conexão SQL Server
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=TIT0528288W11-1\\SQLEXPRESS;"
    "DATABASE=pipeline_vendas;"
    "Trusted_Connection=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}"
)

# Padronizar nomes das colunas
df.columns = [
    "produto",
    "categoria",
    "quantidade",
    "valor",
    "regiao",
    "total"
]

# Enviar dados para SQL Server
df.to_sql(
    "vendas",
    con=engine,
    if_exists="replace",
    index=False
)

print("Dados enviados para SQL Server com sucesso!")