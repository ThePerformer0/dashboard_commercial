import plotly.express as px
import pandas as pd

def sales_over_time(df: pd.DataFrame):
    """Évolution des ventes dans le temps"""
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    sales_time = df.groupby("Order Date")["Sales"].sum().reset_index()
    fig = px.line(
        sales_time,
        x="Order Date",
        y="Sales",
        title="📈 Évolution des ventes dans le temps",
        markers=True,
    )
    return fig

def sales_by_region_chart(df: pd.DataFrame):
    """Ventes totales par région"""
    sales_region = df.groupby("Region")["Sales"].sum().reset_index()
    fig = px.bar(
        sales_region,
        x="Region",
        y="Sales",
        title="🌍 Ventes par région",
        color="Sales",
        color_continuous_scale="Blues",
    )
    return fig

def sales_by_category_chart(df: pd.DataFrame):
    """Ventes par catégorie de produits"""
    sales_category = df.groupby("Category")["Sales"].sum().reset_index()
    fig = px.pie(
        sales_category,
        values="Sales",
        names="Category",
        title="🛒 Répartition des ventes par catégorie",
        hole=0.4,
    )
    return fig

def profit_vs_sales_chart(df: pd.DataFrame):
    """Relation profit vs ventes"""
    fig = px.scatter(
        df,
        x="Sales",
        y="Profit",
        color="Category",
        hover_data=["Sub-Category", "Region"],
        title="💡 Relation entre Ventes et Profits",
    )
    return fig
