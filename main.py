import streamlit as st

st.set_page_config(
    page_title="DataPulse – Analytics",
    page_icon="📊",
    layout="wide",
)

# ── Global CSS (minimal – only safe styling) ──────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #F4F6F8;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }

/* Remove default top padding */
.block-container { padding-top: 1.5rem !important; }

/* Progress bar colours */
.stProgress > div > div > div > div { border-radius: 99px; }

/* Button pill styling */
div.stButton > button {
    border-radius: 999px;
    border: 1.5px solid #DDE1E9;
    background: #ffffff;
    color: #1A1A2E;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 0.85rem;
    padding: 4px 18px;
    transition: all 0.2s;
}
div.stButton > button:hover {
    border-color: #F5B800;
    color: #F5B800;
}
div.stButton > button {
    white-space: nowrap !important;
}
</style>
""", unsafe_allow_html=True)

# ── Colour helpers ─────────────────────────────────────────────────────────────
TEAL   = "#1DB489"
YELLOW = "#F5B800"
LTEAL  = "#A8DFD0"
MUTED  = "#7A7A9D"

def colored(text, color):
    return f'<span style="color:{color};font-weight:600">{text}</span>'

def section_title(title, subtitle=None):
    st.markdown(f"<h2 style='margin:0;font-size:1.4rem;font-weight:700'>{title}</h2>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p style='color:{MUTED};margin:2px 0 12px;font-size:0.85rem'>{subtitle}</p>", unsafe_allow_html=True)

def card_start(title, menu=False):
    """Renders a card header. Card body follows inline."""
    menu_html = "<span style='float:right;color:#ccc;letter-spacing:3px;cursor:pointer'>···</span>" if menu else ""
    st.markdown(f"""
    <div style="background:#fff;border-radius:16px;padding:20px 24px 16px;
                box-shadow:0 2px 10px rgba(0,0,0,0.06);margin-bottom:16px">
      <p style="font-weight:700;font-size:1rem;margin:0 0 14px">{title}{menu_html}</p>
    """, unsafe_allow_html=True)

def card_end():
    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TOP NAV BAR
# ═══════════════════════════════════════════════════════════════════════════════
nav_left, nav_links, nav_right = st.columns([2, 5, 2])

with nav_left:
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:10px;padding:8px 0">
      <div style="background:{YELLOW};border-radius:12px;width:42px;height:42px;
                  display:flex;align-items:center;justify-content:center;font-size:1.3rem">📊</div>
      <span style="font-weight:700;font-size:1.25rem">DataPulse</span>
    </div>""", unsafe_allow_html=True)

with nav_links:
    st.markdown(f"""
    <div style="display:flex;gap:36px;align-items:center;padding:16px 0 0;
                border-bottom:2px solid #ECEEF2">
      <span style="color:{MUTED};font-size:0.92rem;cursor:pointer;padding-bottom:14px">Home</span>
      <span style="color:{MUTED};font-size:0.92rem;cursor:pointer;padding-bottom:14px">About</span>
      <span style="color:{YELLOW};font-size:0.92rem;font-weight:700;cursor:pointer;
                  padding-bottom:12px;border-bottom:2.5px solid {YELLOW}">Analytics</span>
      <span style="color:{MUTED};font-size:0.92rem;cursor:pointer;padding-bottom:14px">Contact</span>
    </div>""", unsafe_allow_html=True)

with nav_right:
    st.markdown("""
    <div style="display:flex;justify-content:flex-end;gap:16px;
                align-items:center;padding:16px 0 0;font-size:1.4rem">
      🔍 🔔
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE TITLE + LOCATION PILL TABS
# ═══════════════════════════════════════════════════════════════════════════════
title_col, pills_col = st.columns([3, 5])

with title_col:
    st.markdown(f"""
    <h1 style="margin:0;font-size:1.6rem;font-weight:700">Performance Deep-Dive</h1>
    <p style="color:{MUTED};margin:4px 0 0;font-size:0.87rem">Real-time metrics for Q3 2024</p>
    """, unsafe_allow_html=True)

# Pill tabs
if "selected_pill" not in st.session_state:
    st.session_state.selected_pill = "Abuja"

with pills_col:
    p1, p2, p3, p4, _ = st.columns([1.2, 1.2, 1.6, 1.2, 1])
    for col, label in zip([p1, p2, p3, p4], ["Abuja", "Island", "Mainland", "PHC"]):
        with col:
            active = st.session_state.selected_pill == label
            bg     = YELLOW if active else "#fff"
            fg     = "#fff"  if active else "#1A1A2E"
            border = YELLOW  if active else "#DDE1E9"
            if st.button(label, key=f"pill_{label}"):
                st.session_state.selected_pill = label
                st.rerun()
            # Override the last rendered button's style
            st.markdown(f"""
            <style>
            div[data-testid="stButton"]:has(button[kind="secondary"][data-testid*="pill_{label}"]) button {{
                background: {bg} !important;
                color: {fg} !important;
                border-color: {border} !important;
            }}
            </style>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT — 3 columns: Product Perf | Customer Acquisition | Location
# ═══════════════════════════════════════════════════════════════════════════════
col1, col2, col3 = st.columns([2.2, 1.8, 2])

# ── COLUMN 1 : Product Performance ───────────────────────────────────────────
with col1:
    with st.container(border=True):
        hdr_l, hdr_r = st.columns([5, 1])
        with hdr_l:
            st.markdown("**Product Performance**")
        with hdr_r:
            st.markdown(f"<span style='color:#ccc;letter-spacing:3px'>···</span>", unsafe_allow_html=True)

        products = [
            {"name": "Electronics",    "value": "$42,800", "pct": 85, "color": TEAL},
            {"name": "Home & Kitchen", "value": "$31,200", "pct": 63, "color": YELLOW},
            {"name": "Apparel",        "value": "$28,900", "pct": 58, "color": TEAL},
            {"name": "Beauty & Care",  "value": "$19,400", "pct": 39, "color": YELLOW},
            {"name": "Automotive",     "value": "$12,100", "pct": 24, "color": LTEAL},
        ]

        for p in products:
            label_col, val_col = st.columns([3, 1])
            with label_col:
                st.markdown(f"<span style='font-size:0.88rem;font-weight:500'>{p['name']}</span>",
                            unsafe_allow_html=True)
            with val_col:
                st.markdown(
                    f"<span style='color:{p['color']};font-weight:600;font-size:0.88rem'>{p['value']}</span>",
                    unsafe_allow_html=True)

            # Progress bar with custom color
            st.markdown(f"""
            <div style="height:7px;background:#EEF0F4;border-radius:999px;margin:-8px 0 12px">
              <div style="width:{p['pct']}%;height:100%;background:{p['color']};border-radius:999px"></div>
            </div>""", unsafe_allow_html=True)

        # ═══ INSERT YOUR PLOTLY PRODUCT CHART HERE ═══
        # st.plotly_chart(product_fig, use_container_width=True)
        # ═════════════════════════════════════════════


# ── COLUMN 2 : Customer Acquisition ──────────────────────────────────────────
with col2:
    with st.container(border=True):
        st.markdown("**Customer Acquisition**")

        # ═══ INSERT YOUR PLOTLY DONUT CHART HERE ═══
        # Replace the placeholder below with:
        # st.plotly_chart(donut_fig, use_container_width=True)
        # Recommended: set fig height ~260, transparent background
        # ════════════════════════════════════════════

        # CSS-only donut placeholder (remove once you add your Plotly chart)
        st.markdown(f"""
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
        """, unsafe_allow_html=True)

        # Legend
        legend_items = [
            ("Organic Search",   "45%", TEAL),
            ("Referral",         "30%", YELLOW),
            ("Paid Advertising", "25%", LTEAL),
        ]
        for label, pct, color in legend_items:
            dot_col, lbl_col, pct_col = st.columns([0.3, 3, 1])
            with dot_col:
                st.markdown(
                    f"<div style='width:10px;height:10px;border-radius:50%;background:{color};margin-top:6px'></div>",
                    unsafe_allow_html=True)
            with lbl_col:
                st.markdown(f"<span style='font-size:0.85rem'>{label}</span>", unsafe_allow_html=True)
            with pct_col:
                st.markdown(f"<span style='font-weight:600;font-size:0.85rem'>{pct}</span>",
                            unsafe_allow_html=True)
            st.divider()


# ── COLUMN 3 : Location Analysis ─────────────────────────────────────────────
with col3:
    hdr_l, hdr_r = st.columns([3, 1])
    with hdr_l:
        st.markdown("**Location Analysis**")
    with hdr_r:
        st.markdown(f"<span style='color:{YELLOW};font-size:0.82rem;font-weight:600;cursor:pointer'>See All ›</span>",
                    unsafe_allow_html=True)

    locations = [
        {"name": "NORTH", "pct": 78, "icon": "🧭", "bg": "#E6F7F2", "bar": TEAL},
        {"name": "SOUTH", "pct": 62, "icon": "↓",  "bg": "#FFF8E1", "bar": YELLOW},
        {"name": "EAST",  "pct": 45, "icon": "→",  "bg": "#E6F7F2", "bar": TEAL},
        {"name": "WEST",  "pct": 91, "icon": "←",  "bg": "#FFF8E1", "bar": YELLOW},
    ]

    for loc in locations:
        with st.container(border=True):
            icon_col, name_col, pct_col = st.columns([0.7, 3, 1])
            with icon_col:
                st.markdown(
                    f"<div style='background:{loc['bg']};border-radius:10px;width:38px;height:38px;"
                    f"display:flex;align-items:center;justify-content:center;font-size:1.1rem'>"
                    f"{loc['icon']}</div>",
                    unsafe_allow_html=True)
            with name_col:
                st.markdown(
                    f"<span style='font-weight:700;font-size:0.9rem;letter-spacing:0.5px'>{loc['name']}</span>",
                    unsafe_allow_html=True)
            with pct_col:
                st.markdown(
                    f"<span style='font-weight:700;font-size:0.9rem'>{loc['pct']}%</span>",
                    unsafe_allow_html=True)

            st.markdown(f"""
            <div style="height:6px;background:#EEF0F4;border-radius:999px;margin:4px 0 0">
              <div style="width:{loc['pct']}%;height:100%;background:{loc['bar']};border-radius:999px"></div>
            </div>""", unsafe_allow_html=True)

        # ═══ INSERT YOUR PLOTLY LOCATION CHART FOR {loc['name']} HERE (optional) ═══
        # st.plotly_chart(fig_{loc['name'].lower()}, use_container_width=True)
        # ══════════════════════════════════════════════════════════════════════