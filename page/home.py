import streamlit as st

TEAL = "#1DB489"
YELLOW = "#F5B800"
LTEAL = "#A8DFD0"
MUTED = "#7A7A9D"


def render_home() -> None:
    # --- Header ---
    st.markdown(
        f"""
        <div style="padding:24px 0 10px">
            <h1 style="margin:0;font-size:1.8rem;font-weight:800">
                Store Performance Deep-Dive
            </h1>
            <p style="color:{MUTED};margin:6px 0 0;font-size:0.95rem">
                Comparative analytics across locations and store formats
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Overview Card ---
    with st.container(border=True):
        st.markdown(
            f"""
            <h3 style="margin-bottom:8px;color:{TEAL}">What This Dashboard Does</h3>
            <p style="font-size:0.95rem;color:{MUTED};line-height:1.6">
            This analytics tool provides a structured comparison between two retail stores 
            across multiple locations. It evaluates performance using product-level demand, 
            pricing behavior, category revenue contribution, and strategic positioning.
            </p>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Analysis Breakdown ---
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown(
                f"""
                <h4 style="color:{YELLOW};margin-bottom:6px"> Demand & Pricing</h4>
                <ul style="color:{MUTED};font-size:0.9rem;line-height:1.7">
                    <li>Top products by order volume</li>
                    <li>Demand vs average price comparison</li>
                    <li>Identification of premium vs high-volume SKUs</li>
                </ul>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(
                f"""
                <h4 style="color:{TEAL};margin-bottom:6px"> Category Mix</h4>
                <ul style="color:{MUTED};font-size:0.9rem;line-height:1.7">
                    <li>Revenue share by Level 1 category</li>
                    <li>Revenue share by Level 2 category</li>
                    <li>Order contribution vs revenue contribution</li>
                </ul>
                """,
                unsafe_allow_html=True,
            )

    with col2:
        with st.container(border=True):
            st.markdown(
                f"""
                <h4 style="color:{YELLOW};margin-bottom:6px"> Strategic Positioning</h4>
                <ul style="color:{MUTED};font-size:0.9rem;line-height:1.7">
                    <li>Category volume vs price mapping</li>
                    <li>Revenue-weighted positioning</li>
                    <li>High-volume / low-price opportunities</li>
                </ul>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(
                f"""
                <h4 style="color:{TEAL};margin-bottom:6px"> Store Comparison</h4>
                <ul style="color:{MUTED};font-size:0.9rem;line-height:1.7">
                    <li>Store 1 vs Store 2 performance</li>
                    <li>Mainland vs Island breakdown</li>
                    <li>Cross-location behavioral differences</li>
                </ul>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- Call to Action ---
    st.markdown(
        f"""
        <div style="
            background:linear-gradient(90deg,{TEAL},{YELLOW});
            padding:18px;
            border-radius:14px;
            text-align:center;
            color:white;
            font-weight:600;
            font-size:0.95rem;">
            Navigate to the <b>Analytics</b> page to explore detailed store performance insights.
        </div>
        """,
        unsafe_allow_html=True,
    )