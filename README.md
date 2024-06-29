# Uçtan Uca ML Projesi

## Proje Hakkında 
Bu proje, satış verilerinin analizi, görselleştirilmesi ve tahminler yapılmasını amaçlayan bir uçtan uca makine öğrenmesi projesidir. Python kullanarak veri analizi, Qlik Sense ile görselleştirme ve web uygulaması ile sonuçların sunulması gibi adımları içerir.

| Dashboard | Web Application|
|:---------:|:--------------:|
| ![Dashboard](https://github.com/AshNumpy/Sales-End-to-End-ML-Project/blob/main/Qlik/dashboard%20mockup.png?raw=true) | ![Web Application](https://github.com/AshNumpy/Sales-End-to-End-ML-Project/blob/main/Qlik/web%20application%20mockup.png?raw=true)
| | |

<details>
    <summary><b>DASHBOARD EKRAN GÖRÜNTÜLERİ İÇİN TIKLAYINIZ</b></summary>

![Genel Bakış](https://github.com/AshNumpy/Sales-End-to-End-ML-Project/blob/main/Qlik/Screenshots/genel%20bakış.png?raw=true)
![Ürün Performansı](https://github.com/AshNumpy/Sales-End-to-End-ML-Project/blob/main/Qlik/Screenshots/ürün%20performansı.png?raw=true)
![Müşteri Analizi](https://github.com/AshNumpy/Sales-End-to-End-ML-Project/blob/main/Qlik/Screenshots/müşteri%20analizi.png?raw=true)

</details>

## Proje Özeti 
Bu proje, satış verilerinin analiz edilmesi, görselleştirilmesi ve tahminler yapılmasını amaçlar. Bu proje kapsamında, veriler toplanarak bir veri tabanında saklanmış, Python ile analiz edilerek ve makine öğrenmesi modelleri ile tahminler yapılmıştır. Elde edilen sonuçlar Qlik Sense ile görselleştirilip, web uygulaması aracılığıyla kullanıcılarla paylaşılmıştır. Proje, ver  analizi, iş zekası entegrasyonu ve makine öğrenmesi uygulamalarını bir araya getirerek değerli içgörüler sunmayı hedefler.

## Projenin Amaçları 
Uçtan Uca ML Projesi'nin temel amaçları arasında, satış verilerinin derinlemesine analizi ve bu veriler üzerinden elde edilen bilgilerin kullanıcılarla etkileşimli bir şekilde paylaşılması yer almaktadır

1. Veri Tabanı Oluşturma ve Yönetimi
1. Veri Analizi ve Görselleştirme
1. Qlik Sense Entegrasyonu
1. Makine Öğrenmesi Modelleri
1. Web Uygulaması Geliştirme

## Veriler Hakkında
Bu projede, satış verileri `./sales_data_sample.csv` dosyasından toplanarak veritabanı yapısına uyarlanmış ve farklı tablolar halinde organize edilmiştir. Tabloların ve sütunların tanımları, DBML sorgusu ile belirtilmiş olup, bu sorgular `./PostgreSQL/schema_dbml.sql` dosyasında bulunmaktadır.

## Model İnşa Süreci
Bu sayfada, satış verilerinin tahmini için oluşturulan makine öğrenmesi modellerinin sonuçlarını bulabilirsiniz. Çeşitli Zaman serisi analizler, derin öğrenme ile yapılan satış tahminlemeleri yapılmış en iyi performansı gösteren model, GradientBoostingRegressor ve XGBRegressor ile stack edilmiş LinearRegression olmuştur.

Aşağıda modelin hiperparametreleri ve performans metriklerine ilişkin detayları bulabilirsiniz.

## Hiperparametreler
En iyi hiperparametreleri bulma sürecinde hedef değişken üzerinde çeşitli oynamalar yapılmış, özellik çıkarım mühendisliği uygulanmış, ensemble tahminler stacked modeller gibi çeşitli süreçler incelenmiştir. En iyi modeli bulma sürecindeki yapılan çalışmaların detayına proje dosyasında bulunan `./Mahine-Learning/customer-purchase-prediction.ipynb` uzantısından ulaşabilirsiniz.

<br>
<br>
<br>
<p align="right">
<a href="https://sales-analysis-machine-learning.streamlit.app" target=_blank>
<B>
    Web application için tıklayınız
</B>
</a>
<br>
    Ramazan ERDURAN
</P>
