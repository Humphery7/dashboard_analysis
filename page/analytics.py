from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

MUTED = "#7A7A9D"


def _load_data() -> pd.DataFrame | None:
    # uploaded = st.file_uploader("Upload spar_analysis.csv", type=["csv"], key="analytics_csv")
    # if uploaded is not None:
    #     return pd.read_csv(uploaded)

    default_path = Path("spar_analysis.csv")
    if default_path.exists():
        return pd.read_csv(default_path)

    return None


def _top_products_plot(df_abuja: pd.DataFrame):
    top_products = (
        df_abuja.groupby("product_name")["order_count"]
        .sum()
        .sort_values(ascending=False)
        .head(20)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="order_count",
        y="product_name",
        orientation="h",
        text="order_count",
        title="Top 20 Products by Order Count — Abuja",
        template="plotly_white",
    )
    fig.update_traces(hovertemplate="Product: %{y}<br>Total Orders: %{x}<extra></extra>")
    fig.update_layout(yaxis=dict(categoryorder="total ascending"), height=600)
    return fig


def _demand_vs_price_plot(df_abuja: pd.DataFrame):
    df_plot = df_abuja.sort_values("rank_in_location")

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=df_plot["product_name"],
            y=df_plot["order_count"],
            name="Order Count",
            marker=dict(opacity=0.85),
            hovertemplate="Product: %{x}<br>Orders: %{y}<extra></extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df_plot["product_name"],
            y=df_plot["avg_price"],
            name="Average Price",
            mode="lines+markers",
            line=dict(width=3),
            marker=dict(size=8),
            yaxis="y2",
            hovertemplate="Product: %{x}<br>Avg Price: ₦%{y:.2f}<extra></extra>",
        )
    )
    fig.update_layout(
        title=dict(text="Abuja: Top Products — Demand vs Price", x=0.5, font=dict(size=20)),
        template="plotly_white",
        xaxis_tickangle=-45,
        height=650,
        yaxis=dict(title="Order Count"),
        yaxis2=dict(title="Average Price (₦)", overlaying="y", side="right"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


def _level_one_revenue_share_plot(df_abuja: pd.DataFrame):
    category_summary = (
        df_abuja.groupby("level_one")
        .agg(
            total_revenue=("revenue", "sum"),
            total_orders=("order_count", "sum"),
            avg_price=("avg_price", "mean"),
            unique_products=("product_name", "nunique"),
        )
        .reset_index()
    )

    total_rev = category_summary["total_revenue"].sum()
    total_orders = category_summary["total_orders"].sum()
    category_summary["revenue_share_%"] = category_summary["total_revenue"] / total_rev * 100
    category_summary["order_share_%"] = category_summary["total_orders"] / total_orders * 100
    category_summary = category_summary.sort_values("total_revenue", ascending=False)

    fig = px.pie(
        category_summary,
        names="level_one",
        values="total_revenue",
        hole=0.5,
        title="Revenue Share by Level One Category — Abuja",
        template="plotly_white",
    )
    fig.update_traces(
        textinfo="percent+label",
        hovertemplate="Category: %{label}<br>Revenue: ₦%{value:,.0f}<br>Share: %{percent}<extra></extra>",
    )
    fig.update_layout(height=520)
    return fig


def _level_two_revenue_share_plot(df_abuja: pd.DataFrame):
    category_summary = (
        df_abuja.groupby("level_two")
        .agg(
            total_revenue=("revenue", "sum"),
            total_orders=("order_count", "sum"),
            avg_price=("avg_price", "mean"),
            unique_products=("product_name", "nunique"),
        )
        .reset_index()
    )

    total_rev = category_summary["total_revenue"].sum()
    total_orders = category_summary["total_orders"].sum()
    category_summary["revenue_share_%"] = category_summary["total_revenue"] / total_rev * 100
    category_summary["order_share_%"] = category_summary["total_orders"] / total_orders * 100
    category_summary = category_summary.sort_values("total_revenue", ascending=False)

    fig = px.pie(
        category_summary,
        names="level_two",
        values="total_revenue",
        hole=0.5,
        title="Revenue Share by Level Two Category — Abuja",
        color_discrete_sequence=px.colors.sequential.Viridis,
        template="plotly_white",
    )
    fig.update_traces(
        textinfo="percent+label",
        hovertemplate="Category: %{label}<br>Revenue: ₦%{value:,.0f}<br>Share: %{percent}<extra></extra>",
    )
    fig.update_layout(height=520)
    return fig


def _category_positioning_plot(df_abuja: pd.DataFrame):
    position_df = (
        df_abuja.groupby("level_one")
        .agg(
            total_orders=("order_count", "sum"),
            total_revenue=("revenue", "sum"),
            avg_category_price=("avg_price", "mean"),
        )
        .reset_index()
    )

    position_df["order_share_%"] = position_df["total_orders"] / position_df["total_orders"].sum() * 100
    position_df["revenue_share_%"] = position_df["total_revenue"] / position_df["total_revenue"].sum() * 100

    fig = px.scatter(
        position_df,
        x="total_orders",
        y="avg_category_price",
        size="total_revenue",
        color="level_one",
        text="level_one",
        title="Category Positioning: Volume vs Price (Level One)",
        size_max=70,
        color_discrete_sequence=px.colors.sequential.Viridis,
        template="plotly_white",
    )
    fig.update_traces(
        textposition="top center",
        hovertemplate=(
            "Category: %{text}<br>Orders: %{x:,.0f}<br>Avg Price: ₦%{y:,.0f}<br>"
            "Revenue: ₦%{marker.size:,.0f}<extra></extra>"
        ),
    )
    fig.update_layout(height=650)
    return fig


def _insight(text: str) -> None:
    st.caption(f"Insight: {text}")


def _store_two_placeholder() -> None:
    st.info("Store 2 placeholder — your second store plots will appear here when you share/store-select data.")
    for i in range(1, 6):
        st.markdown(f"**Plot {i} placeholder**")
        st.empty()
        st.caption("Insight placeholder: add observation for this plot when store 2 analysis is ready.")
        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)


def render_analytics() -> None:
    st.markdown("<h1 style='margin:0;font-size:1.6rem;font-weight:700'>Analytics</h1>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='color:{MUTED};margin:4px 0 12px;font-size:0.9rem'>"
        "Abuja analysis for Store 1, with a structured placeholder for Store 2 comparison." 
        "</p>",
        unsafe_allow_html=True,
    )

    df = _load_data()
    left_col, right_col = st.columns(2, gap="large")

    if df is None:
        with left_col:
            st.warning("No CSV loaded yet. Upload `spar_analysis.csv` to render Abuja analytics plots.")
        with right_col:
            _store_two_placeholder()
        return

    required_cols = {
        "location",
        "product_name",
        "level_one",
        "level_two",
        "avg_price",
        "order_count",
        "rank_in_location",
    }
    missing = required_cols - set(df.columns)
    if missing:
        st.error(f"Dataset missing required columns: {sorted(missing)}")
        return

    df["revenue"] = df["avg_price"] * df["order_count"]
    df_abuja = df[df["location"] == "Abuja"].copy()

    if df_abuja.empty:
        st.warning("No Abuja records found in the dataset.")
        return

    with left_col:
        st.subheader("Store 1 — Abuja")

        st.plotly_chart(_top_products_plot(df_abuja), use_container_width=True)
        _insight("This highlights the highest-demand products by total order count in Abuja.")
        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

        st.plotly_chart(_demand_vs_price_plot(df_abuja), use_container_width=True)
        _insight("This compares demand (orders) against pricing to spot high-volume and premium items.")
        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

        st.plotly_chart(_level_one_revenue_share_plot(df_abuja), use_container_width=True)
        _insight("This shows which level-one categories contribute the most to Abuja revenue.")
        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

        st.plotly_chart(_level_two_revenue_share_plot(df_abuja), use_container_width=True)
        _insight("This gives deeper category mix visibility at level-two granularity.")
        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

        st.plotly_chart(_category_positioning_plot(df_abuja), use_container_width=True)
        _insight("This positions categories by volume, price, and revenue weight for strategic prioritization.")

    with right_col:
        st.subheader("Store 2 — Placeholder")
        _store_two_placeholder()
