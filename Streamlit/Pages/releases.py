import streamlit as st 

def display_releases():
    container = st.container(
        border=True
    )
    
    container.markdown(
        """
        ## 🚀 Initial Release - v1.0.0 (26.06.2024)

        Selamlar,

        Bu ay boyunca yoğun bir çalışma sürecinin ardından geliştirdiğimiz projemizin web uygulaması ayağını tamamladık. İşte ilk yayınımızın detayları:

        ### Yenilikler
        - Web uygulaması, 5 ana sayfadan oluşacak şekilde tasarlandı:
        - **Anasayfa**: Proje hakkında hızlı bir genel bakış sağlar.
        - **Database**: Veritabanı yapısı ve içeriği hakkında detaylı bilgi sunar.
        - **Prediction**: Belirli tarihlerde müşterilerin tahmini satın alma davranışlarını görselleştirir.
        - **Release**: Yayınlanan güncellemelerin ayrıntılarını içerir.
        - **Contact**: Kullanıcıların bizimle iletişime geçebileceği bir iletişim sayfasıdır.

        ### İyileştirmeler
        - **Anasayfa**: KPI'lar için infinite band line eklendi ve projeye erişim butonu güncellendi.
        - **Database**: Veritabanı şeması, iframe ile daha detaylı bir şekilde sunulmaktadır.
        - **Prediction**: Kullanıcıların boş tahminler yapmaması için geliştirilmiş bir kullanıcı arayüzü sağlandı.

        ### Düzeltmeler
        - **Contact**: Gereksiz animasyonlar kaldırıldı, kullanıcı deneyimi iyileştirildi.

        ### Bilinen Sorunlar
        - **Database**: İçerik yükleme süresi, iframe'lerin performansından kaynaklı olarak yavaş olabilir. Cache kullanımı önerilir.
        - **Mobil Uyum**: Bazı mobil cihazlarda uyumluluk sorunları rapor edildi, üzerinde çalışıyoruz.
        - **Contact Form**: Formun POST methodu bazı durumlarda yavaş çalışabilir, performans iyileştirmeleri devam etmektedir.

        ![Release](https://img.shields.io/badge/release-v1.0.0-orange?style=flat-square&link=https%3A%2F%2Fgithub.com%2FAshNumpy%2FSales-End-to-End-ML-Project)
        ![GitHub commit activity](https://img.shields.io/github/commit-activity/t/AshNumpy/Sales-End-to-End-ML-Project?style=flat-square&logo=github&color=orange)
        ![GitHub repo size](https://img.shields.io/github/repo-size/AshNumpy/Sales-End-to-End-ML-Project?style=flat-square&logo=Github&color=orange)
        """
    )