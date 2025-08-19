import pandas as pd

def total_sales(df: pd.DataFrame) -> float:
    """Calcule le chiffre d'affaires total"""
    return df["Sales"].sum()

def total_profit(df: pd.DataFrame) -> float:
    """Calcule le profit total"""
    return df["Profit"].sum()

def total_orders(df: pd.DataFrame) -> int:
    """Nombre de commandes uniques"""
    return df["Order ID"].nunique()

def sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Ventes totales par région"""
    return df.groupby("Region")["Sales"].sum().reset_index()

def top_products(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Top n produits par ventes"""
    return (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

def sales_growth(df: pd.DataFrame) -> float:
    """Croissance des ventes par rapport à l'année précédente"""
    if "Order Date" not in df.columns:
        return None
    df["Year"] = df["Order Date"].dt.year
    sales_by_year = df.groupby("Year")["Sales"].sum().sort_index()
    if len(sales_by_year) < 2:
        return None
    growth = (sales_by_year.iloc[-1] - sales_by_year.iloc[-2]) / sales_by_year.iloc[-2] * 100
    return round(growth, 2)
