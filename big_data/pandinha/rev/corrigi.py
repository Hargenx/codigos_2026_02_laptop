def limpar_valor_monetario(valor: str) -> float:
    """Converte texto monetário simples para float."""
    limpo = valor.replace("R$", "").replace(".", "").replace(",", ".")
    return float(limpo.strip())

print(limpar_valor_monetario("R$ 1.234,56"))


import pandas as pd

df = pd.read_csv(
    "vendas.csv",
    usecols=["data", "regiao", "valor"],
    parse_dates=["data"],
    dtype={"regiao": "string"},
    na_values=["", "NA", "N/A", "-"]
)


df.shape
df.head()
df.sample(5, random_state=42)
df.info()
df.describe(include="all")
df.isna().sum()
df.nunique()
df.duplicated().sum()


df = df.convert_dtypes()
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

df.isna().mean().sort_values(ascending=False)

# Exemplo conservador: remove apenas linhas sem chave essencial
df = df.dropna(subset=["cliente_id"])

# Duplicata exata
mascara = df.duplicated(keep=False)

# Duplicata pela chave de negócio
dups = df.duplicated(
    subset=["pedido_id", "produto_id"],
    keep=False
)

# Só remova depois de validar a regra
df = df.drop_duplicates(subset=["pedido_id", "produto_id"])


df["data"] = pd.to_datetime(df["data"], errors="coerce")

df["ano"] = df["data"].dt.year
df["mes"] = df["data"].dt.to_period("M")
df["dia_semana"] = df["data"].dt.day_name()

mensal = df.groupby("mes", observed=True)["valor"].sum()



df["estado"] = (
    df["estado"]
      .astype("string")
      .str.strip()
      .str.upper()
)

validos = {"RJ", "SP", "MG", "ES"}
invalidos = ~df["estado"].isin(validos)