import streamlit as st
from streamlit_option_menu import option_menu

import warnings
warnings.filterwarnings("ignore")


st.set_page_config(
    page_title="Sales Analysis",
    page_icon=":bar_chart:",
    initial_sidebar_state="collapsed",
)

st.title('Sales Analysis')
st.markdown('<span style="color:gray">This app predicts the salesbased on the data provided.</span>', unsafe_allow_html=True)

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

