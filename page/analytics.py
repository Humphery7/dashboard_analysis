# from pathlib import Path
#
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# import streamlit as st
#
# MUTED = "#7A7A9D"
#
#
# def _load_data() -> pd.DataFrame | None:
#     # uploaded = st.file_uploader("Upload spar_analysis.csv", type=["csv"], key="analytics_csv")
#     # if uploaded is not None:
#     #     return pd.read_csv(uploaded)
#
#     default_path = Path("spar_analysis.csv")
#     if default_path.exists():
#         return pd.read_csv(default_path)
#
#     return None
#
# def _load_store_two_data() -> pd.DataFrame | None:
#     # uploaded = st.file_uploader("Upload mfc.csv (Store 2)", type=["csv"], key="store2_csv")
#     # if uploaded is not None:
#     #     return pd.read_csv(uploaded)
#
#     default_path = Path("mfc_sold.csv")
#     if default_path.exists():
#         return pd.read_csv(default_path)
#
#     return None
#
#
# def _top_products_plot(df_location: pd.DataFrame, location_name: str):
#     top_products = (
#         df_location.groupby("product_name")["order_count"]
#         .sum()
#         .sort_values(ascending=False)
#         .head(20)
#         .reset_index()
#     )
#
#     fig = px.bar(
#         top_products,
#         x="order_count",
#         y="product_name",
#         orientation="h",
#         text="order_count",
#         title=f"Top 20 Products by Order Count — {location_name}",
#         template="plotly_white",
#     )
#     fig.update_traces(hovertemplate="Product: %{y}<br>Total Orders: %{x}<extra></extra>")
#     fig.update_layout(yaxis=dict(categoryorder="total ascending"), height=600)
#     return fig
#
#
# def _demand_vs_price_plot(df_location: pd.DataFrame, location_name: str):
#     df_plot = df_location.sort_values("rank_in_location")
#
#     fig = go.Figure()
#     fig.add_trace(
#         go.Bar(
#             x=df_plot["product_name"],
#             y=df_plot["order_count"],
#             name="Order Count",
#             marker=dict(opacity=0.85),
#             hovertemplate="Product: %{x}<br>Orders: %{y}<extra></extra>",
#         )
#     )
#     fig.add_trace(
#         go.Scatter(
#             x=df_plot["product_name"],
#             y=df_plot["avg_price"],
#             name="Average Price",
#             mode="lines+markers",
#             line=dict(width=3),
#             marker=dict(size=8),
#             yaxis="y2",
#             hovertemplate="Product: %{x}<br>Avg Price: ₦%{y:.2f}<extra></extra>",
#         )
#     )
#     fig.update_layout(
#         title=dict(text=f"Demand vs Price", x=0.5, font=dict(size=20)),
#         template="plotly_white",
#         xaxis_tickangle=-45,
#         height=650,
#         yaxis=dict(title="Order Count"),
#         yaxis2=dict(title="Average Price (₦)", overlaying="y", side="right"),
#         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
#     )
#     return fig
#
#
# def _level_one_revenue_share_plot(df_location: pd.DataFrame, location_name: str):
#     category_summary = (
#         df_location.groupby("level_one")
#         .agg(
#             total_revenue=("revenue", "sum"),
#             total_orders=("order_count", "sum"),
#             avg_price=("avg_price", "mean"),
#             unique_products=("product_name", "nunique"),
#         )
#         .reset_index()
#     )
#
#     total_rev = category_summary["total_revenue"].sum()
#     total_orders = category_summary["total_orders"].sum()
#     category_summary["revenue_share_%"] = category_summary["total_revenue"] / total_rev * 100
#     category_summary["order_share_%"] = category_summary["total_orders"] / total_orders * 100
#     category_summary = category_summary.sort_values("total_revenue", ascending=False)
#
#     fig = px.pie(
#         category_summary,
#         names="level_one",
#         values="total_revenue",
#         hole=0.5,
#         title=f"Revenue Share by Level One Category — {location_name}",
#         template="plotly_white",
#     )
#     fig.update_traces(
#         textinfo="percent+label",
#         hovertemplate="Category: %{label}<br>Revenue: ₦%{value:,.0f}<br>Share: %{percent}<extra></extra>",
#     )
#     fig.update_layout(height=520)
#     return fig
#
#
# def _level_two_revenue_share_plot(df_location: pd.DataFrame, location_name: str):
#     category_summary = (
#         df_location.groupby("level_two")
#         .agg(
#             total_revenue=("revenue", "sum"),
#             total_orders=("order_count", "sum"),
#             avg_price=("avg_price", "mean"),
#             unique_products=("product_name", "nunique"),
#         )
#         .reset_index()
#     )
#
#     total_rev = category_summary["total_revenue"].sum()
#     total_orders = category_summary["total_orders"].sum()
#     category_summary["revenue_share_%"] = category_summary["total_revenue"] / total_rev * 100
#     category_summary["order_share_%"] = category_summary["total_orders"] / total_orders * 100
#     category_summary = category_summary.sort_values("total_revenue", ascending=False)
#
#     fig = px.pie(
#         category_summary,
#         names="level_two",
#         values="total_revenue",
#         hole=0.5,
#         title=f"Revenue Share by Level Two Category — {location_name}",
#         color_discrete_sequence=px.colors.sequential.Viridis,
#         template="plotly_white",
#     )
#     fig.update_traces(
#         textinfo="percent+label",
#         hovertemplate="Category: %{label}<br>Revenue: ₦%{value:,.0f}<br>Share: %{percent}<extra></extra>",
#     )
#     fig.update_layout(height=520)
#     return fig
#
#
# def _category_positioning_plot(df_location: pd.DataFrame, location_name: str):
#     position_df = (
#         df_location.groupby("level_one")
#         .agg(
#             total_orders=("order_count", "sum"),
#             total_revenue=("revenue", "sum"),
#             avg_category_price=("avg_price", "mean"),
#         )
#         .reset_index()
#     )
#
#     position_df["order_share_%"] = position_df["total_orders"] / position_df["total_orders"].sum() * 100
#     position_df["revenue_share_%"] = position_df["total_revenue"] / position_df["total_revenue"].sum() * 100
#
#     fig = px.scatter(
#         position_df,
#         x="total_orders",
#         y="avg_category_price",
#         size="total_revenue",
#         color="level_one",
#         text="level_one",
#         title=f"Category Positioning: Volume vs Price (Level One) — {location_name}",
#         size_max=70,
#         color_discrete_sequence=px.colors.sequential.Viridis,
#         template="plotly_white",
#     )
#     fig.update_traces(
#         textposition="top center",
#         hovertemplate=(
#             "Category: %{text}<br>Orders: %{x:,.0f}<br>Avg Price: ₦%{y:,.0f}<br>"
#             "Revenue: ₦%{marker.size:,.0f}<extra></extra>"
#         ),
#     )
#     fig.update_layout(height=650)
#     return fig
#
#
# def _insight(text: str) -> None:
#     st.caption(f"Insight: {text}")
#
#
# def _store_two_placeholder() -> None:
#     st.info("Store 2 placeholder — your second store plots will appear here when you share/store-select data.")
#     for i in range(1, 6):
#         st.markdown(f"**Plot {i} placeholder**")
#         st.empty()
#         st.caption("Insight placeholder: add observation for this plot when store 2 analysis is ready.")
#         st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
#
#
# def render_analytics() -> None:
#     st.markdown("<h1 style='margin:0;font-size:1.6rem;font-weight:700'>Analytics</h1>", unsafe_allow_html=True)
#     st.markdown(
#         f"<p style='color:{MUTED};margin:4px 0 12px;font-size:0.9rem'>"
#         "Select a location to view Spar analysis. MFC remains a placeholder for now."
#         "</p>",
#         unsafe_allow_html=True,
#     )
#
#     if "selected_location" not in st.session_state:
#         st.session_state.selected_location = "Abuja"
#
#     l1, l2, l3, l4, _ = st.columns([1.2, 1.2, 1.6, 1.2, 1])
#     for col, label in zip([l1, l2, l3, l4], ["Abuja", "Island", "Mainland", "PHC"]):
#         with col:
#             active = st.session_state.selected_location == label
#             bg = "#F5B800" if active else "#fff"
#             fg = "#fff" if active else "#1A1A2E"
#             border = "#F5B800" if active else "#DDE1E9"
#             if st.button(label, key=f"analytics_loc_{label}"):
#                 st.session_state.selected_location = label
#                 st.rerun()
#             st.markdown(
#                 f"""
#                 <style>
#                 div[data-testid="stButton"]:has(button[kind="secondary"][data-testid*="analytics_loc_{label}"]) button {{
#                     background: {bg} !important;
#                     color: {fg} !important;
#                     border-color: {border} !important;
#                 }}
#                 </style>
#                 """,
#                 unsafe_allow_html=True,
#             )
#
#     st.markdown("<br>", unsafe_allow_html=True)
#
#     df = _load_data()
#     df_store2 = _load_store_two_data()
#     left_col, right_col = st.columns(2, gap="large")
#
#     if df is None:
#         with left_col:
#             st.warning("No CSV loaded yet. Upload `spar_analysis.csv` to render location analytics plots.")
#         with right_col:
#             _store_two_placeholder()
#         return
#
#     required_cols = {
#         "location",
#         "product_name",
#         "level_one",
#         "level_two",
#         "avg_price",
#         "order_count",
#         "rank_in_location",
#     }
#     missing = required_cols - set(df.columns)
#     if missing:
#         st.error(f"Dataset missing required columns: {sorted(missing)}")
#         return
#
#     df["revenue"] = df["avg_price"] * df["order_count"]
#
#     location_frames = {
#         "Abuja": df[df["location"] == "Abuja"].copy(),
#         "Island": df[df["location"] == "Island"].copy(),
#         "Mainland": df[df["location"] == "Mainland"].copy(),
#         "PHC": df[df["location"] == "PHC"].copy(),
#     }
#
#     selected_location = st.session_state.selected_location
#     selected_df = location_frames[selected_location]
#
#     if selected_df.empty:
#         st.warning(f"No records found for {selected_location} in the dataset.")
#         return
#
#     with left_col:
#         st.subheader(f"Spar — {selected_location}")
#
#         st.plotly_chart(_top_products_plot(selected_df, selected_location), use_container_width=True)
#         _insight(f"Spar Mainland has milk&butter bread as the top item, and also has healthier distribution across products.")
#         st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
#
#         st.plotly_chart(_demand_vs_price_plot(selected_df, selected_location), use_container_width=True)
#         _insight("This compares demand (orders) against pricing to spot high-volume and premium items.")
#         st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
#
#         st.plotly_chart(_level_one_revenue_share_plot(selected_df, selected_location), use_container_width=True)
#         _insight(f"This shows which level-one categories contribute the most to {selected_location} revenue.")
#         st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
#
#         st.plotly_chart(_level_two_revenue_share_plot(selected_df, selected_location), use_container_width=True)
#         _insight("This gives deeper category mix visibility at level-two granularity.")
#         st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
#
#         st.plotly_chart(_category_positioning_plot(selected_df, selected_location), use_container_width=True)
#         _insight("This positions categories by volume, price, and revenue weight for strategic prioritization.")
#
#     # with right_col:
#     #     st.subheader("Store 2 — Placeholder")
#     #     _store_two_placeholder()
#
#     with right_col:
#         st.subheader(f"MFC — {selected_location}")
#
#         if df_store2 is None:
#             st.info("Upload mfc.csv to render Store 2 analytics.")
#             return
#
#         required_cols_store2 = {
#             "location",
#             "product_name",
#             "level_one",
#             "level_two",
#             "avg_price",
#             "order_count",
#             "rank_in_location",
#         }
#
#         missing_store2 = required_cols_store2 - set(df_store2.columns)
#         if missing_store2:
#             st.error(f"Store 2 dataset missing required columns: {sorted(missing_store2)}")
#             return
#
#         # Add revenue
#         df_store2["revenue"] = df_store2["avg_price"] * df_store2["order_count"]
#
#         # Correct filtering using location values
#         df_island = df_store2[df_store2["location"] == "LOSF1"].copy()
#         df_mainland = df_store2[df_store2["location"] == "MNLF1"].copy()
#
#         store2_location_frames = {
#             "Island": df_island,
#             "Mainland": df_mainland,
#         }
#
#         if selected_location not in store2_location_frames:
#             st.warning("Store 2 only available for Mainland and Island.")
#             return
#
#         selected_store2_df = store2_location_frames[selected_location]
#
#         if selected_store2_df.empty:
#             st.warning(f"No Store 2 records found for {selected_location}.")
#             return
#
#         # ---- SAME PIPELINE AS STORE 1 ----
#
#         st.plotly_chart(_top_products_plot(selected_store2_df, selected_location), use_container_width=True)
#         _insight(f"Top demand products for Store 2 in {selected_location}.")
#         st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
#
#         st.plotly_chart(_demand_vs_price_plot(selected_store2_df, selected_location), use_container_width=True)
#         _insight("Demand vs pricing distribution for Store 2.")
#         st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
#
#         st.plotly_chart(_level_one_revenue_share_plot(selected_store2_df, selected_location), use_container_width=True)
#         _insight("Revenue contribution by level-one category for Store 2.")
#         st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
#
#         st.plotly_chart(_level_two_revenue_share_plot(selected_store2_df, selected_location), use_container_width=True)
#         _insight("Revenue contribution by level-two category for Store 2.")
#         st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
#
#         st.plotly_chart(_category_positioning_plot(selected_store2_df, selected_location), use_container_width=True)
#         _insight("Category positioning for Store 2 based on volume and price.")


























from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

MUTED = "#7A7A9D"


# ===============================
# DATA LOADERS
# ===============================

def _load_data() -> pd.DataFrame | None:
    default_path = Path("spar_analysis.csv")
    if default_path.exists():
        return pd.read_csv(default_path)
    return None


def _load_store_two_data() -> pd.DataFrame | None:
    default_path = Path("mfc_sold.csv")
    if default_path.exists():
        return pd.read_csv(default_path)
    return None


def _load_store_three_data() -> pd.DataFrame | None:
    default_path = Path("super_saver.csv")  # rename to your real file
    if default_path.exists():
        return pd.read_csv(default_path)
    return None



# ===============================
# PLOTS
# ===============================

# def _top_products_plot(df_location: pd.DataFrame, store_location_name: str):
#
#     top_products = (
#         df_location.groupby("product_name")["order_count"]
#         .sum()
#         .sort_values(ascending=False)
#         .head(20)
#         .reset_index()
#     )
#
#     fig = px.bar(
#         top_products,
#         x="order_count",
#         y="product_name",
#         orientation="h",
#         text="order_count",
#         title=f"Top 20 Products — {store_location_name}",
#         template="plotly_white",
#     )
#
#     fig.update_traces(hovertemplate="Product: %{y}<br>Orders: %{x}<extra></extra>")
#     fig.update_layout(yaxis=dict(categoryorder="total ascending"), height=650)
#
#     return fig



def _top_products_plot(df_location: pd.DataFrame, store_location_name: str):

    top_products = (
        df_location.groupby(
            ["product_name", "level_one", "level_two"]
        )["order_count"]
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
        title=f"Top 20 Products — {store_location_name}",
        template="plotly_white",
    )

    # ⭐ Add richer hover info WITHOUT changing visuals
    fig.update_traces(
        hovertemplate="""
        Product: %{y}<br>
        Level One: %{customdata[0]}<br>
        Level Two: %{customdata[1]}<br>
        Orders: %{x:,.0f}
        <extra></extra>
        """,
        customdata=top_products[["level_one", "level_two"]].values
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        height=650
    )

    return fig



def _demand_vs_price_plot(df_location: pd.DataFrame, store_location_name: str):

    df_plot = df_location.sort_values("rank_in_location")

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df_plot["product_name"],
            y=df_plot["order_count"],
            name="Order Count",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_plot["product_name"],
            y=df_plot["avg_price"],
            name="Average Price",
            mode="lines+markers",
            yaxis="y2",
        )
    )

    fig.update_layout(
        title=f"Demand vs Price — {store_location_name}",
        template="plotly_white",
        height=700,
        xaxis_tickangle=-45,
        yaxis=dict(title="Order Count"),
        yaxis2=dict(title="Average Price (₦)", overlaying="y", side="right"),
        legend=dict(orientation="h", y=1.02, x=1, xanchor="right"),
    )

    return fig


def _level_one_revenue_share_plot(df_location: pd.DataFrame, store_location_name: str):

    category_summary = (
        df_location.groupby("level_one")
        .agg(total_revenue=("revenue", "sum"))
        .reset_index()
        .sort_values("total_revenue", ascending=False)
    )

    fig = px.pie(
        category_summary,
        names="level_one",
        values="total_revenue",
        hole=0.5,
        title=f"Level One Revenue Share — {store_location_name}",
        template="plotly_white",
    )

    fig.update_traces(
                textinfo="percent+label",
                hovertemplate="Category: %{label}<br>Revenue: ₦%{value:,.0f}<br>Share: %{percent}<extra></extra>",
        )
    fig.update_layout(height=520)
    return fig

    # fig.update_layout(height=600)
    # return fig


def _level_two_revenue_share_plot(df_location: pd.DataFrame, store_location_name: str):

    category_summary = (
        df_location.groupby("level_two")
        .agg(total_revenue=("revenue", "sum"))
        .reset_index()
        .sort_values("total_revenue", ascending=False)
    )

    fig = px.pie(
        category_summary,
        names="level_two",
        values="total_revenue",
        hole=0.5,
        title=f"Level Two Revenue Share — {store_location_name}",
        color_discrete_sequence=px.colors.sequential.Viridis,
        template="plotly_white",
    )


    fig.update_traces(
                textinfo="percent+label",
                hovertemplate="Category: %{label}<br>Revenue: ₦%{value:,.0f}<br>Share: %{percent}<extra></extra>",
        )
    fig.update_layout(height=520)
    return fig


def _category_positioning_plot(df_location: pd.DataFrame, store_location_name: str):

    position_df = (
        df_location.groupby("level_one")
        .agg(
            total_orders=("order_count", "sum"),
            total_revenue=("revenue", "sum"),
            avg_category_price=("avg_price", "mean"),
        )
        .reset_index()
    )

    fig = px.scatter(
        position_df,
        x="total_orders",
        y="avg_category_price",
        size="total_revenue",
        color="level_one",
        text="level_one",
        title=f"Category Positioning — {store_location_name}",
        color_discrete_sequence=px.colors.sequential.Viridis,
        template="plotly_white",
        size_max=70,
    )

    # fig.update_layout(height=700)
    # return fig
    fig.update_traces(
        textposition="middle center",
        textfont=dict(
            color="black",
            size=13,
            family="Inter, Arial, sans-serif"
        ),
        marker=dict(line=dict(width=1, color="white"))
    )

    fig.update_layout(
        height=700,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    return fig
# ===============================
# STORE PANEL RENDERER
# ===============================

def _render_store_panel(df_store: pd.DataFrame, store_name: str, location_name: str):

    store_location_name = f"{store_name} {location_name}"

    if df_store.empty:
        st.warning(f"No records found for {store_location_name}")
        return

    st.markdown(f"## {store_location_name}")

    st.plotly_chart(_top_products_plot(df_store, store_location_name), use_container_width=True)

    st.plotly_chart(_demand_vs_price_plot(df_store, store_location_name), use_container_width=True)

    st.plotly_chart(_level_one_revenue_share_plot(df_store, store_location_name), use_container_width=True)

    st.plotly_chart(_level_two_revenue_share_plot(df_store, store_location_name), use_container_width=True)

    st.plotly_chart(_category_positioning_plot(df_store, store_location_name), use_container_width=True)

# ===============================
# MAIN RENDER
# ===============================

def render_analytics() -> None:

    st.markdown(
        "<h1 style='font-size:1.6rem;font-weight:700'>Analytics</h1>",
        unsafe_allow_html=True,
    )

    if "selected_location" not in st.session_state:
        st.session_state.selected_location = "Abuja"

    # -------------------------
    # Location selector
    # -------------------------

    cols = st.columns(4)
    for col, label in zip(cols, ["Abuja", "Island", "Mainland", "PHC"]):
        with col:
            if st.button(label):
                st.session_state.selected_location = label
                st.rerun()

    selected_location = st.session_state.selected_location

    # -------------------------
    # Load datasets
    # -------------------------

    df1 = _load_data()
    df2 = _load_store_two_data()
    df3 = _load_store_three_data()

    if df1 is None:
        st.warning("Upload spar_analysis.csv")
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

    if not required_cols.issubset(df1.columns):
        st.error("Store 1 dataset missing required columns.")
        return

    df1["revenue"] = df1["avg_price"] * df1["order_count"]

    # Store 1 filtering
    store1_df = df1[df1["location"] == selected_location].copy()

    # Store 2 filtering (code mapping)
    store2_df = None
    if df2 is not None and required_cols.issubset(df2.columns):

        df2["revenue"] = df2["avg_price"] * df2["order_count"]

        store2_map = {
            "Island": df2[df2["location"] == "LOSF1"],
            "Mainland": df2[df2["location"] == "MNLF1"],
        }

        store2_df = store2_map.get(selected_location)

    # Store 3 filtering
    store3_df = None
    if df3 is not None and required_cols.issubset(df3.columns):

        df3["revenue"] = df3["avg_price"] * df3["order_count"]

        store3_df = df3[df3["location"] == selected_location].copy()

    # -------------------------
    # Metric Plots List
    # -------------------------

    metric_functions = [
        ("Top Products", _top_products_plot),
        ("Demand vs Price", _demand_vs_price_plot),
        ("Revenue Share Level 1", _level_one_revenue_share_plot),
        ("Revenue Share Level 2", _level_two_revenue_share_plot),
        ("Category Positioning", _category_positioning_plot),
    ]

    # ==========================
    # STORE LABELS
    # ==========================

    store_configs = []

    # Store 1
    if not store1_df.empty:
        store_configs.append(("Spar", store1_df))

    # Store 2
    if store2_df is not None and not store2_df.empty:
        store_configs.append(("MFC", store2_df))

    # Store 3
    if store3_df is not None and not store3_df.empty:
        store_configs.append(("Supersaver", store3_df))

    # ==========================
    # RENDER METRIC ROWS
    # ==========================

    # ==========================
    # RENDER METRIC ROWS
    # ==========================

    insight_map = {
        "Top Products": {
            "Spar": {
                "Abuja": "Milk & bread products dominate demand in Abuja.",
                "Island": "Milk & Bread products dominate demand in Island, while water variants also contributing a substantial amount. Unlike the other stores, the top 20 is heavily populated by raw ingredients",
                "Mainland": "Balanced SKU demand across categories.",
                "PHC": "Smaller SKU basket but high loyalty demand."
            },

            "MFC": {
                "Abuja": "Demand is more spread across SKUs.",
                "Island": "Demand is more spread with main drivers coming from Cway bottle water and bread",
                "Mainland": "Higher order traffic compared to other locations.",
                "PHC": "Moderate SKU diversity."
            },

            "Supersaver": {
                "Abuja": "Premium items dominate demand.",
                "Island": "Low demand across products compared to other stores, either supersaver has a smaller footprint or caters to a more exclusive customer base .",
                "Mainland": "Growing demand in beverages.",
                "PHC": "Value SKUs perform better."
            }
        },

        "Demand vs Price": {
            "Spar": {
                "Abuja": "Pricing closely follows demand volume.",
                "Island": "Some premium pricing zones exist.",
                "Mainland": "Strong price sensitivity.",
                "PHC": "Budget pricing preference."
            },

            "MFC": {
                "Abuja": "Premium pricing segments visible.",
                "Island": "Higher price elasticity observed.",
                "Mainland": "Balanced price strategy.",
                "PHC": "Competitive pricing required."
            },

            "Supersaver": {
                "Abuja": "Strong premium price positioning.",
                "Island": "Price elasticity is high.",
                "Mainland": "Mixed pricing strategy.",
                "PHC": "Value pricing performs better."
            }
        }
    }

    for metric_name, metric_fn in metric_functions:

        st.markdown(f"## {metric_name}")

        # Section divider line
        st.markdown(
            """
            <div style="
                display:flex;
                width:100%;
                height:10px;
                margin:15px 0 30px 0;
                border-radius:20px;
                overflow:hidden;
                box-shadow: 0px 2px 6px rgba(0,0,0,0.12);
            ">
                <div style="width:50%; background:#F5B800;"></div>
                <div style="width:50%; background:#1DB489;"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Render each store side-by-side
        for store_name, store_df in store_configs:
            st.markdown('<div style="min-width:900px">', unsafe_allow_html=True)

            store_title = f"{store_name} {selected_location}"

            # Plot
            st.plotly_chart(
                metric_fn(store_df, store_title),
                use_container_width=True
            )

            # Insight under plot
            insight_text = insight_map.get(metric_name, {}) \
                .get(store_name, {}) \
                .get(selected_location, "No insight available.")

            st.markdown(
                f"""
                <p style="
                    color:#111111;
                    font-weight:600;
                    font-size:0.92rem;
                    font-style:italic;
                    margin-top:8px;
                ">
                Insight — {store_name}: {insight_text}
                </p>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Section separation line (very important for readability)
        st.divider()