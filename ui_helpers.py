"""
UI helpers for Streamlit components
"""
import streamlit as st


def colored_card(label: str, value: str, background: str = "#1f77b4", text_color: str = "white", width: str = "100%"):
    """Render a simple colored KPI card using inline HTML/CSS.

    Parameters:
    - label: small text label
    - value: primary value text
    - background: background color (hex or CSS color)
    - text_color: color for the text
    - width: CSS width of the card container
    """
    html = f"""
    <div style="background:{background}; color:{text_color}; padding:16px; border-radius:10px; width:{width};">
      <div style="font-size:14px; opacity:0.9">{label}</div>
      <div style="font-size:28px; font-weight:700; margin-top:6px">{value}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
