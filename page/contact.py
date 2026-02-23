import streamlit as st

MUTED = "#7A7A9D"


def render_contact() -> None:
    st.markdown(
        f"""
        <h1 style="margin:0;font-size:1.6rem;font-weight:700">Contact</h1>
        <p style="color:{MUTED};margin:6px 0 0;font-size:0.95rem">
          Reach us at <a href="mailto:support@datapulse.example">support@datapulse.example</a>.
        </p>
        """,
        unsafe_allow_html=True,
    )
