import streamlit as st

def display_contact():
    def get_page(html_path):
        
        with open(html_path, 'r', encoding='utf-8') as f:
            home_page = f.read()
            
        return home_page
    
    contact_form = get_page("./ContactPage/contact.html")
    
    container = st.container(
        border=False,
        height=700
    )
    
    container.markdown(
        """
        <style>
        .container {
                padding: 40px;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    container.markdown(
        f"""
        <div class="container"/>
        {contact_form}
        """,
        unsafe_allow_html=True, 
    )