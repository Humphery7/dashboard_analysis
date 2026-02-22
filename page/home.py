import streamlit as st

TEAL = "#1DB489"
YELLOW = "#F5B800"
LTEAL = "#A8DFD0"
MUTED = "#7A7A9D"


def render_home() -> None:
    title_col, pills_col = st.columns([3, 5])

    with title_col:
        st.markdown(
            f"""
            <h1 style="margin:0;font-size:1.6rem;font-weight:700">Performance Deep-Dive</h1>
            <p style="color:{MUTED};margin:4px 0 0;font-size:0.87rem">Real-time metrics for Q3 2024</p>
            """,
            unsafe_allow_html=True,
        )

    if "selected_pill" not in st.session_state:
        st.session_state.selected_pill = "Abuja"

    with pills_col:
        p1, p2, p3, p4, _ = st.columns([1.2, 1.2, 1.6, 1.2, 1])
        for col, label in zip([p1, p2, p3, p4], ["Abuja", "Island", "Mainland", "PHC"]):
            with col:
                active = st.session_state.selected_pill == label
                bg = YELLOW if active else "#fff"
                fg = "#fff" if active else "#1A1A2E"
                border = YELLOW if active else "#DDE1E9"
                if st.button(label, key=f"pill_{label}"):
                    st.session_state.selected_pill = label
                    st.rerun()

                st.markdown(
                    f"""
                    <style>
                    div[data-testid="stButton"]:has(button[kind="secondary"][data-testid*="pill_{label}"]) button {{
                        background: {bg} !important;
                        color: {fg} !important;
                        border-color: {border} !important;
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True,
                )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2.2, 1.8, 2])

    with col1:
        with st.container(border=True):
            hdr_l, hdr_r = st.columns([5, 1])
            with hdr_l:
                st.markdown("**Product Performance**")
            with hdr_r:
                st.markdown("<span style='color:#ccc;letter-spacing:3px'>···</span>", unsafe_allow_html=True)

            products = [
                {"name": "Electronics", "value": "$42,800", "pct": 85, "color": TEAL},
                {"name": "Home & Kitchen", "value": "$31,200", "pct": 63, "color": YELLOW},
                {"name": "Apparel", "value": "$28,900", "pct": 58, "color": TEAL},
                {"name": "Beauty & Care", "value": "$19,400", "pct": 39, "color": YELLOW},
                {"name": "Automotive", "value": "$12,100", "pct": 24, "color": LTEAL},
            ]

            for product in products:
                label_col, val_col = st.columns([3, 1])
                with label_col:
                    st.markdown(
                        f"<span style='font-size:0.88rem;font-weight:500'>{product['name']}</span>",
                        unsafe_allow_html=True,
                    )
                with val_col:
                    st.markdown(
                        f"<span style='color:{product['color']};font-weight:600;font-size:0.88rem'>{product['value']}</span>",
                        unsafe_allow_html=True,
                    )

                st.markdown(
                    f"""
                    <div style="height:7px;background:#EEF0F4;border-radius:999px;margin:-8px 0 12px">
                      <div style="width:{product['pct']}%;height:100%;background:{product['color']};border-radius:999px"></div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    with col2:
        with st.container(border=True):
            st.markdown("**Customer Acquisition**")

            st.markdown(
                f"""
                <div style="display:flex;justify-content:center;align-items:center;padding:20px 0 10px">
                  <div style="
                      width:160px;height:160px;border-radius:50%;
                      background:conic-gradient({TEAL} 0% 45%, {YELLOW} 45% 75%, {LTEAL} 75% 100%);
                      display:flex;align-items:center;justify-content:center;">
                    <div style="width:106px;height:106px;border-radius:50%;background:#fff;
                                display:flex;flex-direction:column;align-items:center;justify-content:center">
                      <span style="font-weight:700;font-size:1.3rem">12.4k</span>
                      <span style="font-size:0.65rem;color:{MUTED};letter-spacing:1.5px;margin-top:2px">TOTAL</span>
                    </div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            legend_items = [
                ("Organic Search", "45%", TEAL),
                ("Referral", "30%", YELLOW),
                ("Paid Advertising", "25%", LTEAL),
            ]
            for label, pct, color in legend_items:
                dot_col, lbl_col, pct_col = st.columns([0.3, 3, 1])
                with dot_col:
                    st.markdown(
                        f"<div style='width:10px;height:10px;border-radius:50%;background:{color};margin-top:6px'></div>",
                        unsafe_allow_html=True,
                    )
                with lbl_col:
                    st.markdown(f"<span style='font-size:0.85rem'>{label}</span>", unsafe_allow_html=True)
                with pct_col:
                    st.markdown(f"<span style='font-weight:600;font-size:0.85rem'>{pct}</span>", unsafe_allow_html=True)
                st.divider()

    with col3:
        hdr_l, hdr_r = st.columns([3, 1])
        with hdr_l:
            st.markdown("**Location Analysis**")
        with hdr_r:
            st.markdown(
                f"<span style='color:{YELLOW};font-size:0.82rem;font-weight:600;cursor:pointer'>See All ›</span>",
                unsafe_allow_html=True,
            )

        locations = [
            {"name": "NORTH", "pct": 78, "icon": "🧭", "bg": "#E6F7F2", "bar": TEAL},
            {"name": "SOUTH", "pct": 62, "icon": "↓", "bg": "#FFF8E1", "bar": YELLOW},
            {"name": "EAST", "pct": 45, "icon": "→", "bg": "#E6F7F2", "bar": TEAL},
            {"name": "WEST", "pct": 91, "icon": "←", "bg": "#FFF8E1", "bar": YELLOW},
        ]

        for location in locations:
            with st.container(border=True):
                icon_col, name_col, pct_col = st.columns([0.7, 3, 1])
                with icon_col:
                    st.markdown(
                        f"<div style='background:{location['bg']};border-radius:10px;width:38px;height:38px;"
                        f"display:flex;align-items:center;justify-content:center;font-size:1.1rem'>"
                        f"{location['icon']}</div>",
                        unsafe_allow_html=True,
                    )
                with name_col:
                    st.markdown(
                        f"<span style='font-weight:700;font-size:0.9rem;letter-spacing:0.5px'>{location['name']}</span>",
                        unsafe_allow_html=True,
                    )
                with pct_col:
                    st.markdown(
                        f"<span style='font-weight:700;font-size:0.9rem'>{location['pct']}%</span>",
                        unsafe_allow_html=True,
                    )

                st.markdown(
                    f"""
                    <div style="height:6px;background:#EEF0F4;border-radius:999px;margin:4px 0 0">
                      <div style="width:{location['pct']}%;height:100%;background:{location['bar']};border-radius:999px"></div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
