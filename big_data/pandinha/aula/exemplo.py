import pandas as pd


df = pd.DataFrame({
    "produto": ["A", "B", "C"],
    "qtd": [2, 1, 4],
    "preco": [10.0, 25.0, 7.5],
})

df["total"] = df["qtd"] * df["preco"]

print(df)