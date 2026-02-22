import streamlit as st

from page import render_about, render_analytics, render_contact, render_home

st.set_page_config(
    page_title="DataPulse – Analytics",
    page_icon="📊",
    layout="wide",
)

if "active_page" not in st.session_state:
    st.session_state.active_page = "home"

current_page = st.session_state.active_page

YELLOW = "#F5B800"
MUTED = "#7A7A9D"

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #F4F6F8;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; }
.stProgress > div > div > div > div { border-radius: 99px; }

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
""",
    unsafe_allow_html=True,
)

nav_left, nav_links, nav_right = st.columns([2, 5, 2])

with nav_left:
    st.markdown(
        f"""
    <div style="display:flex;align-items:center;gap:10px;padding:8px 0">
      <div style="background:{YELLOW};border-radius:12px;width:42px;height:42px;
                  display:flex;align-items:center;justify-content:center;font-size:1.3rem">📊</div>
      <span style="font-weight:700;font-size:1.25rem">DataPulse</span>
    </div>""",
        unsafe_allow_html=True,
    )

with nav_links:
    st.markdown(
        """
        <style>
        div[data-testid="stButton"]:has(button[data-testid*="nav_"]) button {
            border: none !important;
            border-radius: 0 !important;
            background: transparent !important;
            min-height: 0 !important;
            padding: 0 0 12px !important;
            white-space: nowrap !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    nav_cols = st.columns([1, 1, 1, 1], gap="small")
    for col, label in zip(nav_cols, ["Home", "About", "Analytics", "Contact"]):
        page_key = label.lower()
        with col:
            if st.button(label, key=f"nav_{page_key}"):
                st.session_state.active_page = page_key
            is_active = current_page == page_key
            st.markdown(
                f"""
                <style>
                div[data-testid="stButton"]:has(button[data-testid*="nav_{page_key}"]) button {{
                    color: {YELLOW if is_active else MUTED} !important;
                    font-size: 0.92rem !important;
                    font-weight: {700 if is_active else 500} !important;
                    {'border-bottom:2.5px solid ' + YELLOW + ' !important;' if is_active else 'border-bottom: none !important;'}
                }}
                </style>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("<div style='border-bottom:2px solid #ECEEF2;margin-top:-2px'></div>", unsafe_allow_html=True)

with nav_right:
    st.markdown(
        """
    <div style="display:flex;justify-content:flex-end;gap:16px;
                align-items:center;padding:16px 0 0;font-size:1.4rem">
      🔍 🔔
    </div>""",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

PAGE_RENDERERS = {
    "home": render_home,
    "about": render_about,
    "analytics": render_analytics,
    "contact": render_contact,
}

PAGE_RENDERERS[current_page]()
