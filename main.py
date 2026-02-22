import streamlit as st

from page import render_about, render_analytics, render_contact, render_home

st.set_page_config(
    page_title="DataPulse – Analytics",
    page_icon="📊",
    layout="wide",
)

if "page" not in st.query_params:
    st.query_params["page"] = "home"

current_page = st.query_params.get("page", "home").lower()
if current_page not in {"home", "about", "analytics", "contact"}:
    current_page = "home"
    st.query_params["page"] = "home"

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
    home_active = current_page == "home"
    about_active = current_page == "about"
    analytics_active = current_page == "analytics"
    contact_active = current_page == "contact"

    st.markdown(
        f"""
    <div style="display:flex;gap:36px;align-items:center;padding:16px 0 0;
                border-bottom:2px solid #ECEEF2">
      <a href="?page=home" target="_self" style="text-decoration:none;color:{YELLOW if home_active else MUTED};font-size:0.92rem;
         font-weight:{700 if home_active else 500};cursor:pointer;padding-bottom:14px;
         {'border-bottom:2.5px solid ' + YELLOW if home_active else ''}">Home</a>
      <a href="?page=about" target="_self" style="text-decoration:none;color:{YELLOW if about_active else MUTED};font-size:0.92rem;
         font-weight:{700 if about_active else 500};cursor:pointer;padding-bottom:14px;
         {'border-bottom:2.5px solid ' + YELLOW if about_active else ''}">About</a>
      <a href="?page=analytics" target="_self" style="text-decoration:none;color:{YELLOW if analytics_active else MUTED};font-size:0.92rem;
         font-weight:{700 if analytics_active else 500};cursor:pointer;padding-bottom:12px;
         {'border-bottom:2.5px solid ' + YELLOW if analytics_active else ''}">Analytics</a>
      <a href="?page=contact" target="_self" style="text-decoration:none;color:{YELLOW if contact_active else MUTED};font-size:0.92rem;
         font-weight:{700 if contact_active else 500};cursor:pointer;padding-bottom:14px;
         {'border-bottom:2.5px solid ' + YELLOW if contact_active else ''}">Contact</a>
    </div>""",
        unsafe_allow_html=True,
    )

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
