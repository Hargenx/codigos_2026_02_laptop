# 1. IMPORTAÇÕES
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 2. LEITURA DO DATASET
caminho = Path(__file__).parent / "dataset" / "Supermart Grocery Sales - Retail Analytics Dataset.csv"
df = pd.read_csv(caminho, encoding="ISO-8859-1")

print(df.head())

# 3. INSPEÇÃO INICIAL

print("Dimensões:")
print(df.shape)

print("\nColunas:")
print(df.columns)

print("\nTipos:")
print(df.dtypes)

print("\nInformações gerais:")
df.info()

# 4. ESTATÍSTICAS DESCRITIVAS

print(
    df[
        ["Sales", "Discount", "Profit"]
    ].describe()
)

# 5. VALORES AUSENTES

print(
    df.isna().sum()
)

# 6. DUPLICATAS

print(
    "Duplicatas:",
    df.duplicated().sum()
)

# 7. CONVERSÃO DA DATA

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed",
    errors="coerce"
)

print(
    df["Order Date"].head()
)

# 8. VERIFICAR DATAS QUE NÃO FORAM CONVERTIDAS

print(
    df[
        df["Order Date"].isna()
    ]
)

# 9. REMOVER DUPLICATAS

df = (
    df
    .drop_duplicates()
    .copy()
)

print(
    "Registros restantes:",
    len(df)
)

# 10. CRIAR COLUNAS DE ANO, MÊS E ANO-MÊS

df["Year"] = (
    df["Order Date"]
    .dt.year
)

df["Month"] = (
    df["Order Date"]
    .dt.month
)

df["YearMonth"] = (
    df["Order Date"]
    .dt.to_period("M")
    .astype(str)
)

print(
    df[
        [
            "Order Date",
            "Year",
            "Month",
            "YearMonth"
        ]
    ].head()
)