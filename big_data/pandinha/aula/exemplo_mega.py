import pandas as pd


df = pd.DataFrame({
    "pedido_id": [101, 102, 103, 104, 105, 106],
    "cliente_id": [1, 2, 1, 3, 4, 2],
    "produto_id": [10, 11, 12, 10, 13, 11],
    "nome": ["Ana", "Bruno", "Ana", "Carla", "Diego", "Bruno"],
    "ativo": [True, True, False, True, True, True],
    "salario": [3500, 1800, 4200, 2500, 1900, 5100],
    "regiao": ["RJ", "SP", "RJ", "MG", "ES", "SP"],
    "estado": [" rj", "SP ", "rj", "mg", "ES", "sp"],
    "produto": ["Teclado", "Mouse", "Monitor", "Teclado", "Headset", "Mouse"],
    "qtd": [2, 3, 1, 4, 2, 1],
    "preco": [150.00, 80.00, 1200.00, 150.00, 220.00, 80.00],
    "valor": [300.00, 240.00, 1200.00, 600.00, 440.00, 80.00],
    "data": pd.to_datetime([
        "2026-01-05",
        "2026-01-06",
        "2026-02-10",
        "2026-02-11",
        "2026-03-01",
        "2026-03-15"
    ])
})

# LOC / ILOC

ativos = df.loc[
    df["ativo"],
    ["nome", "salario"]
]

primeiras = df.iloc[:5, [0, 2]]

df.loc[
    df["salario"] < 2000,
    "faixa"
] = "entrada"

print("Ativos:")
print(ativos)

print("\nPrimeiras linhas:")
print(primeiras)


# FILTROS

filtro = (
    (df["regiao"] == "RJ")
    & (df["valor"] >= 1000)
)

rj = df.loc[filtro]

rj2 = df.query(
    "regiao == 'RJ' and valor >= 1000"
)

limite = 1000

rj3 = df.query(
    "regiao == 'RJ' and valor >= @limite"
)

print("\nFiltro com loc:")
print(rj)

print("\nFiltro com query:")
print(rj2)

print("\nFiltro com variável externa:")
print(rj3)


# TRANSFORMAÇÃO

resultado = (
    df
    .assign(
        total=lambda d:
            d["qtd"] * d["preco"]
    )
    .rename(
        columns={
            "qtd": "quantidade"
        }
    )
    .sort_values(
        ["total", "produto"],
        ascending=[False, True]
    )
)

print("\nResultado transformado:")
print(resultado)


# GROUPBY

resumo = (
    df
    .groupby(
        "regiao",
        as_index=False,
        observed=True
    )
    .agg(
        vendas=("valor", "sum"),
        ticket_medio=("valor", "mean"),
        pedidos=("pedido_id", "nunique")
    )
    .sort_values(
        "vendas",
        ascending=False
    )
)

print("\nResumo por região:")
print(resumo)


# MERGE

pedidos = pd.DataFrame({
    "pedido_id": [101, 102, 103, 104],
    "cliente_id": [1, 2, 1, 3],
    "valor": [300, 240, 1200, 600]
})

clientes = pd.DataFrame({
    "cliente_id": [1, 2, 3],
    "segmento": [
        "Premium",
        "Regular",
        "Premium"
    ]
})

pedidos_com_clientes = pedidos.merge(
    clientes[
        ["cliente_id", "segmento"]
    ],
    on="cliente_id",
    how="left",
    validate="many_to_one"
)

print("\nResultado do merge:")
print(pedidos_com_clientes)


# CONCAT

jan = pd.DataFrame({
    "mes": ["Jan", "Jan"],
    "produto": ["Mouse", "Teclado"],
    "valor": [800, 1200]
})

fev = pd.DataFrame({
    "mes": ["Fev", "Fev"],
    "produto": ["Mouse", "Teclado"],
    "valor": [950, 1400]
})

mar = pd.DataFrame({
    "mes": ["Mar", "Mar"],
    "produto": ["Mouse", "Teclado"],
    "valor": [1100, 1350]
})

todos = pd.concat(
    [jan, fev, mar],
    ignore_index=True
)

print("\nResultado do concat:")
print(todos)

df_despesas = pd.DataFrame({
    "mes": ["Jan", "Fev", "Mar"],
    "alimentacao": [800, 850, 900],
    "moradia": [1500, 1500, 1500],
    "transporte": [400, 450, 420]
})

print("DataFrame original:")
print(df_despesas)


# WIDE -> LONG
long = df_despesas.melt(
    id_vars=["mes"],
    value_vars=[
        "alimentacao",
        "moradia",
        "transporte"
    ],
    var_name="categoria",
    value_name="valor"
)

print("\nResultado do melt:")
print(long)


# LONG -> WIDE
wide = long.pivot_table(
    index="mes",
    columns="categoria",
    values="valor",
    aggfunc="sum"
)

print("\nResultado do pivot_table:")
print(wide)

# Evite
for i, linha in df.iterrows():
    df.loc[i, "total"] = linha["qtd"] * linha["preco"]

# Prefira
df["total"] = df["qtd"] * df["preco"]

# Condicional vetorizado
df["faixa"] = pd.cut(df["valor"], bins=[0, 100, 500, float("inf")], labels=["baixo", "medio", "alto"])

# Evite: atribuição encadeada
df[df["valor"] < 0]["valor"] = 0

# Prefira
df.loc[df["valor"] < 0, "valor"] = 0

# Transformação explícita
filtrado = df.loc[df["regiao"] == "RJ"].copy()

print("\nDataFrame filtrado com cópia:")
print(filtrado)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(resumo["regiao"], resumo["vendas"])
ax.set(
    title="Vendas por região",
    xlabel="Região",
    ylabel="Vendas (R$)",
)
fig.tight_layout()
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(
    data=df, x="regiao", y="valor",
    estimator="mean", errorbar=None, ax=ax
)
ax.set_title("Ticket médio por região")
plt.show()

#---
# Corrigindo o DataFrame mensal para conter dados de vendas mensais por região
#---

df["mes"] = (
    df["data"]
    .dt.to_period("M")
    .astype(str)
)

mensal = (
    df
    .groupby(
        ["mes", "regiao"],
        as_index=False
    )
    .agg(
        vendas=("valor", "sum")
    )
)

print(mensal)


import plotly.express as px

fig = px.line(
    mensal,
    x="mes",
    y="vendas",
    color="regiao",
    markers=True,
    title="Vendas mensais por região",
)
fig.update_layout(xaxis_title="Mês", yaxis_title="Vendas (R$)")
fig.show()

# =========================
# ALTAIR
# =========================

import altair as alt

alt.renderers.enable("browser")

chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(x=alt.X("regiao:N", title="Região"),
            y=alt.Y("sum(valor):Q", title="Vendas (R$)"),
        tooltip=[alt.Tooltip("regiao:N", title="Região"),
            alt.Tooltip("sum(valor):Q", title="Vendas", format=".2f")
        ]
    )
    .properties(title="Vendas por região", width=600, height=350)
)

chart.show()