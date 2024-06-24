import streamlit as st
from streamlit_option_menu import option_menu

import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Sales Analysis",
    page_icon=":bar_chart:",
    initial_sidebar_state="collapsed",
)

# APP COLOR PALETTE
# --primary-100:#FF6600;
# --primary-200:#ff983f;
# --primary-300:#ffffa1;
# --accent-100:#F5F5F5;
# --accent-200:#929292;
# --text-100:#FFFFFF;
# --text-200:#e0e0e0;
# --bg-100:#1D1F21;
# --bg-200:#2c2e30;
# --bg-300:#444648;
    

# Header
st.markdown(
    """
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        footer {
            background-color: #2c2e30;
            padding: 20px;
            text-align: center;
            border-radius: 10px;
        }
    </style>
    <h1 style="text-align: center;">Uçtan Uca ML Projesi</h1>      
    <p style="color: gray;text-align: center;">Satış Verilerinin Analizi ve Tahmini</p>
    """,
    unsafe_allow_html=True
    )

# Menu selection
menu = option_menu(
    menu_title=None,
    options=["Home", "Database", "Prediction", "Release", "Contact"],
    icons=["house", "database", "cpu", "book", "telephone"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {
            "width": "100vw",
            "margin": 0,
            "background-color": "#1D1F21",
            },
        "icon": {
            "color": "#FFFFFF"
            }, 
        "nav-link": {
            "font-size": "15px",
            "text-align": "center",
            "color": "#FFFFFF",
            "background-color": "#2c2e30",
            "margin": "0px 3px",
            "border-radius": "5px",
            },
        "nav-link-selected": {
            "background-color": "#FF6600",
            "color": "#FFFFFF",
            "border-radius": "10px",
            },
        "icon-selected": {
            "color": "#FFFFFF"
            }
    }
)

if menu == "Home":
    from Pages import homepage
    homepage.display_homepage()

elif menu == "Database":
    pass

elif menu == "Prediction":
    pass

elif menu == "Release":
    pass

elif menu == "Contact":
    pass

st.markdown(
    """
    <footer>
        <p style="color: white;text-align: center; padding: 50px 0px 0px 0px">&copy; 2024 Uçtan Uca ML Projesi: MIT Licence</p>
        <p style="color: #FF6601;text-align: center;">İletişim: ramazan.erduran@outlook.com.tr</p>
    </footer>
    """,
    unsafe_allow_html=True
)