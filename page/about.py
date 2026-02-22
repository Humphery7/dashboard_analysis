import streamlit as st

MUTED = "#7A7A9D"


def render_about() -> None:
    st.markdown(
        f"""
        <h1 style="margin:0;font-size:1.6rem;font-weight:700">About</h1>
        <p style="color:{MUTED};margin:6px 0 0;font-size:0.95rem">
          DataPulse helps teams monitor product performance, customer acquisition, and location insights.
        </p>
        """,
        unsafe_allow_html=True,
    )
