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
            "background-color": "#2c2e30",
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
    from Pages import database
    database.display_database()

elif menu == "Prediction":
    from Pages import prediction
    prediction.display_prediction()

elif menu == "Release":
    pass

elif menu == "Contact":
    from Pages import contact
    contact.display_contact()

st.markdown(
    """
<footer style="padding: 70px 0px 70px 0px; text-align: center;">
    <p style="color: white;">&copy; 2024 Uçtan Uca ML Projesi: MIT Licence</p>
    <p style="color: #FF6601;">İletişim: ramazan.erduran@outlook.com.tr</p>
    <div style="margin-top: 10px;">
        <a href="https://www.linkedin.com/in/ramazan-erduran" target="_blank" class="linkedin-link" style="margin: 0 10px; display: inline-block; transform-origin: center; transition: transform 0.5s;">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="#FF6600" class="bi bi-linkedin" viewBox="0 0 16 16" style="cursor: pointer;">
                <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
            </svg>
        </a>
        <a href="https://www.github.com/AshNumpy" target="_blank" class="linkedin-link" style="margin: 0 10px; display: inline-block; transform-origin: center; transition: transform 0.5s;">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="#FF6600" class="bi bi-github" viewBox="0 0 16 16" style="cursor: pointer;">
                <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
            </svg>
        </a> 
        <a href="https://ramazan-erduran.super.site" target="_blank" class="linkedin-link" style="margin: 0 10px; display: inline-block; transform-origin: center; transition: transform 0.5s;">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="#FF6600" class="bi bi-box-arrow-up-right" viewBox="0 0 16 16" style="cursor: pointer;">
                <path fill-rule="evenodd" d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5"/>
                <path fill-rule="evenodd" d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0z"/>
            </svg>
        </a>
    </div>
</footer>

<style>
    .linkedin-link:hover {
        transform: scale(1.3);
    }
</style>
    """,
    unsafe_allow_html=True
)