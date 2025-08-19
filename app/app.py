import streamlit as st
from data_loader import load_data
from kpi_calculator import *
from charts import *
import pandas as pd

# Charger FontAwesome
st.markdown(
    """
    <link rel="stylesheet"
     href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """,
    unsafe_allow_html=True
)

st.title("📊 Dashboard Commercial - Sample Superstore")

# Charger les données
df = load_data()
df["Order Date"] = pd.to_datetime(df["Order Date"])

# --- Sidebar (Filtres) ---
st.sidebar.header("🔍 Filtres")

# Filtre Année
years = sorted(df["Order Date"].dt.year.unique())
year = st.sidebar.selectbox("Année :", options=["Toutes"] + list(map(str, years)))

# Filtre Région
regions = sorted(df["Region"].unique())
region = st.sidebar.multiselect("Régions :", options=regions, default=regions)

# Filtre Catégorie
categories = sorted(df["Category"].unique())
category = st.sidebar.multiselect("Catégories :", options=categories, default=categories)

# --- Appliquer les filtres ---
df_filtered = df.copy()

if year != "Toutes":
    df_filtered = df_filtered[df_filtered["Order Date"].dt.year == int(year)]

df_filtered = df_filtered[df_filtered["Region"].isin(region)]
df_filtered = df_filtered[df_filtered["Category"].isin(category)]

# --- KPI Section ---
st.subheader("Indicateurs Clés")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="💰 Chiffre d'affaires", value=f"${total_sales(df_filtered):,.0f}")

with col2:
    st.metric(label="📦 Commandes", value=f"{total_orders(df_filtered):,}")

with col3:
    st.metric(label="📈 Profit", value=f"${total_profit(df_filtered):,.0f}")

# --- Visualisations ---
st.subheader("📊 Visualisations")

tab1, tab2, tab3, tab4 = st.tabs(
    ["📈 Ventes dans le temps", "🌍 Ventes par région", "🛒 Ventes par catégorie", "💡 Profit vs Ventes"]
)

with tab1:
    st.plotly_chart(sales_over_time(df_filtered), use_container_width=True)

with tab2:
    st.plotly_chart(sales_by_region_chart(df_filtered), use_container_width=True)

with tab3:
    st.plotly_chart(sales_by_category_chart(df_filtered), use_container_width=True)

with tab4:
    st.plotly_chart(profit_vs_sales_chart(df_filtered), use_container_width=True)

# --- Top produits ---
st.subheader("🏆 Top Produits")
st.write(top_products(df_filtered, 5))
