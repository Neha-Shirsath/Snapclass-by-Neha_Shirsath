import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""

        <div style="display:flex; flex-direction:column; justify-content:center; align-items:center; margin-bottom:6px; margin-top:10px">
            <img src="{logo_url}" style='height:90px;' />
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>  CLASS</h1>
        </div>

            """, unsafe_allow_html=True)

def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""

        <div style="display:flex; justify-content:center; align-items:center; margin-bottom:6px;">
            <img class="logo-img" src="{logo_url}" style='height:75px; margin-left:5px' />
            <h2 class="teacher-text" style="text-align:center !important; color: #5865F2 !important">SNAP<br/>  CLASS</h2>
        </div>

            """, unsafe_allow_html=True)
