# 📊 Pipeline de Análise de Vendas

## 🚀 Visão Geral do Projeto

Este projeto simula um **pipeline completo de dados de vendas**, desde a ingestão e tratamento até a análise e visualização em dashboard.

O objetivo é demonstrar habilidades práticas em **Engenharia de Dados e Análise de Dados**, aplicando conceitos de ETL, modelagem e visualização.

---

## 🧠 Problema de Negócio

A empresa precisa responder perguntas como:

- Como estão evoluindo as vendas ao longo do tempo?
- Quais produtos têm melhor desempenho?
- Qual o impacto do frete nas vendas?
- Quais são os principais indicadores (KPIs)?

---

## 🏗️ Arquitetura do Pipeline

Fluxo do projeto:

**CSV (dados brutos) → Python (tratamento) → SQL (estruturação) → Análise → Power BI (dashboard)**

---

## 🛠️ Tecnologias Utilizadas

- Python (Pandas) → tratamento e transformação de dados  
- SQL Server → modelagem, criação de tabelas e consultas SQL  
- Power BI → visualização e dashboard interativo  
- Excel / CSV → origem e armazenamento dos dados  
- Microsoft Visio → modelagem do pipeline de dados e arquitetura  
- Git & GitHub → versionamento do projeto  

---

## 📂 Estrutura do Projeto

```
pipeline-analise-vendas/
│
├── dados/
│   ├── vendas.csv
│   ├── vendas_tratado.csv
│
├── dashboard/
│   ├── analise de vendas.pbix
│   ├── dashboard.png
│
├── diagrama/ 
│   ├── pipeline de dados.png
│   ├── pipeline de dados.vsdx
│ 
├── python/
│   ├── tratamento_dados.py
│
├── sql/
│   ├── create_database.sql
│   ├── create_table.sql
│   ├── consultas.sql
│
└── README.md
```

---

## ⚙️ Etapas do Projeto

### 1. Ingestão de Dados
Importação dos dados brutos via arquivos CSV.

### 2. Tratamento de Dados (Python)
- Limpeza de dados
- Padronização de colunas
- Tratamento de valores nulos
- Criação de dataset final

### 3. Modelagem e Banco de Dados (SQL)
- Criação de banco de dados
- Criação de tabelas
- Inserção de dados
- Queries analíticas

### 4. Análise de Dados
- Análise de vendas por período
- Identificação de produtos mais vendidos
- KPIs de desempenho

### 5. Visualização (Power BI)
- Dashboard interativo
- Indicadores de performance
- Insights de negócio

---

## 📊 Principais Insights

- Identificação dos produtos com maior volume de vendas  
- Análise do impacto do frete no valor final  
- Evolução das vendas ao longo do tempo  
- Visão consolidada de performance comercial  

---

## 📌 Destaques Técnicos

✔ Pipeline completo de dados (ETL)  
✔ Integração Python + SQL + Power BI  
✔ Estrutura próxima de ambiente corporativo  
✔ Projeto focado em resolução de problema de negócio  

---

## 👨‍💻 Autor

MARCOS VINÍCIUS DE JESUS DA SILVA  
Estudante de Análise de Dados / BI  
Foco em Engenharia de Dados e Business Intelligence  

---

## 📌 Observação

Este projeto foi desenvolvido com foco em portfólio profissional, simulando um cenário real de análise de dados em ambiente corporativo.
