from matplotlib import container
import streamlit as st

def display_homepage():
    
    def get_page(html_path):
        
        with open(html_path, 'r', encoding='utf-8') as f:
            home_page = f.read()

        return home_page
    
    container = st.container(
        border=True,
        height=260
    )
    
    container.markdown(
        """
        <h2> Proje Özeti </h2>

        Uçtan Uca ML Projesi, satış verilerinin analiz edilmesi, görselleştirilmesi ve tahminler yapılmasını amaçlar. Bu proje kapsamında, veriler toplanarak bir veri tabanında saklanmış, Python ile analiz edilerek ve makine öğrenmesi modelleri ile tahminler yapılmıştır. Elde edilen sonuçlar Qlik Sense ile görselleştirilip, web uygulaması aracılığıyla kullanıcılarla paylaşılmıştır. Proje, veri analizi, iş zekası entegrasyonu ve makine öğrenmesi uygulamalarını bir araya getirerek değerli içgörüler sunmayı hedefler.        
        """,
        unsafe_allow_html=True
    )
        
    brand_line = get_page("./Streamlit/HomePage/brand-line.html")   
    
    st.markdown(
       f"""
       {brand_line}
       """,
       unsafe_allow_html=True, 
    )
    
    col1, col2 = st.columns(2)
    
    with col2:
        container = st.container(
            border=True,
            height=260
        )
    
        container.markdown(
                """
                <h2> Proje Hakkında </h2>
                
                <p style='align:justify;'>
                Bu proje, satış verilerinin analizi, görselleştirilmesi ve tahminler yapılmasını amaçlayan bir uçtan uca makine öğrenmesi projesidir. Python kullanarak veri analizi, BI tool ile görselleştirme ve web uygulaması ile sonuçların sunulması gibi adımları içerir.
                </p>
                """,
                unsafe_allow_html=True
            )
        
        container = st.container()
        
        project_details = get_page("../HomePage/project-details.html")   
        
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
            <div class="container">
                {project_details}
            </div>
            """,
            unsafe_allow_html=True, 
        )
        
    with col1:
        container = st.container(
            border=True,
            height=390
        )
        
        container.markdown(
                """
                <h2> Projenin Amaçları </h2>
                
                <p style='align:justify;'>
                Uçtan Uca ML Projesi'nin temel amaçları arasında, satış verilerinin derinlemesine analizi ve bu veriler üzerinden elde edilen bilgilerin kullanıcılarla etkileşimli bir şekilde paylaşılması yer almaktadır
                </p>
                <ol>
                <li>Veri Tabanı Oluşturma ve Yönetimi</li>
                <li>Veri Analizi ve Görselleştirme</li>
                <li>Qlik Sense Entegrasyonu</li>
                <li>Makine Öğrenmesi Modelleri</li>
                <li>Web Uygulaması Geliştirme</li>
                <ol>
                """,
                unsafe_allow_html=True
            )