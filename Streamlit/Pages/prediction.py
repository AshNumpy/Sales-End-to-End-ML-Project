import streamlit as st
import pandas as pd 
import numpy as np 
import holidays
import pickle
import warnings

warnings.filterwarnings("ignore")

with open('./MachineLearning/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
with open('./MachineLearning/scaler.pkl', 'rb') as f:
    sc = pickle.load(f)
    
with open('./MachineLearning/ohe.pkl', 'rb') as f:
    ohe = pickle.load(f)
    
with open('./MachineLearning/customer_map.pkl', 'rb') as f:
    customer_map = pickle.load(f)
    
with open('./MachineLearning/cluster_productline_map.pkl', 'rb') as f:
    cluster_productline_map = pickle.load(f)
    
with open('./MachineLearning/segment_map.pkl', 'rb') as f:
    segment_map = pickle.load(f)


us_holidays = holidays.US()
def extract_date_features(df, date_column, holidays_list):
    ''''extract_date_features' işlevi bir DataFrame, bir tarih sütunu ve bir tatil listesi alır ve orijinal
    tarih sütununu kaldırırken DataFrame'e tarihle ilgili çeşitli özellikler ekler.
    
    Parameters
    ----------
    df
        Tarih özelliklerini çıkarmak istediğiniz verileri içeren bir pandas DataFrame.
    date_column
        'date_column' parametresi, DataFrame'de ("df"), özellikleri çıkarmak istediğiniz tarih değerlerini
    içeren sütunun adıdır.
    holidays_list
        'holidays_list' parametresi, tatilleri temsil eden tarihlerin listesidir. Bu tarihler, veri
    kümesindeki belirli bir tarihin tatil olup olmadığını belirlemek için kullanılacaktır.
    
    Returns
    -------
        'extract_date_features' işlevi, belirtilen 'date_column'dan tarihle ilgili çeşitli özellikleri
    çıkardıktan ve bunları DataFrame'e yeni sütunlar olarak ekledikten sonra DataFrame 'df'yi
    döndürüyor. İşlev aynı zamanda orijinal "date_column"u geri döndürmeden önce DataFrame'den çıkarır.
    
    '''
    df[date_column] = pd.to_datetime(df[date_column])
    
    df['Year'] = df[date_column].dt.year
    df['Month'] = df[date_column].dt.month
    df['Day'] = df[date_column].dt.day
    df['Weekday'] = df[date_column].dt.weekday
    df['DayOfYear'] = df[date_column].dt.dayofyear
    df['Quarter'] = df[date_column].dt.quarter
    df['WeekOfYear'] = df[date_column].dt.isocalendar().week
    df['IsMonthStart'] = df[date_column].dt.is_month_start.astype(int)
    df['IsMonthEnd'] = df[date_column].dt.is_month_end.astype(int)
    df['IsHoliday'] = df[date_column].isin(holidays_list).astype(int)
    
    df.drop(date_column, axis=1, inplace=True)

    return df


def OHEHandler(fitted_encoder, df, col):
    ''''OHEHandler' işlevi, girdi olarak takılı bir kodlayıcıyı, bir veri çerçevesini ve bir sütun adını
    alır, belirtilen sütunda bir sıcak kodlama gerçekleştirir ve orijinal sütun çıkarılmış ve bir sıcak
    kodlanmış sütunlar eklenmiş olarak güncellenmiş veri çerçevesini döndürür.
    
    Parameters
    ----------
    fitted_encoder
        'Fitted_encoder' parametresi muhtemelen scikit-learn'den takılmış bir OneHotEncoder örneğidir. Bu
    kodlayıcı zaten bazı veriler üzerinde eğitildi ve şimdi yeni verileri dönüştürmek için kullanılıyor.
    df
        Tek seferde kodlanacak sütunu içeren DataFrame
    col
        'OHEHandler' işlevindeki 'col' parametresi, DataFrame 'df'de, takılı kodlayıcı 'fitted_encoder'ı
    kullanarak tek seferde kodlamak istediğiniz sütunun adını temsil eder.
    
    Returns
    -------
        'OHEHandler' işlevi, takılı kodlayıcı kullanılarak belirtilen 'col' one-hot sütunuyla birlikte
    DataFrame 'df'yi döndürür.
    
    '''
    encoded_col = fitted_encoder.transform(df[col].values.reshape(-1, 1))
    
    encoded_df = pd.DataFrame(encoded_col.tolist(), 
                              columns=fitted_encoder.get_feature_names_out(), 
                              index=df.index)

    df = pd.concat([df.drop(columns=[col]), encoded_df], axis=1)
    
    return df


def make_single_prediction(date, productline, customer):
    '''"make_single_prediction" işlevi, kullanıcı giriş verilerini alır, bunları önceden işler, özellik
    mühendisliği uygular, verileri ölçeklendirir, bir makine öğrenimi modeli kullanarak tahmin yapar ve
    giriş verileriyle birlikte tahmini satış değerini döndürür.
    
    Parameters
    ----------
    date
        Siparişin tarihi 'YYYY-AA-GG' biçiminde.
    productline
        Ürün yelpazesi, bir şirketin sunduğu belirli kategoriyi veya ürün türünü ifade eder. Ürünlerin
    özelliklerine veya kullanım amaçlarına göre düzenlenmesine ve sınıflandırılmasına yardımcı olur.
    Ürün gruplarına örnek olarak elektronik, giyim, ev aletleri ve otomotiv ürünleri verilebilir.
    customer
        'Müşteri' parametresi, satış tahmini yapmak istediğiniz müşterinin adını ifade eder. Bu bilgi,
    geçmiş verilere ve o müşteriyle ilişkili diğer ilgili özelliklere dayalı bir satış tahmini
    oluşturmak için tahmin modelinde kullanılacaktır.
    
    Returns
    -------
        'make_single_prediction' işlevi, verilen tarih, ürün grubu ve müşteri için öngörülen satış
    değeriyle birlikte girdi verilerini içeren bir DataFrame 'df' döndürür.
    
    '''
    # KULLANICIDAN GELEN VERİLERİ VERİ SETİNE DÖNÜŞTÜRME
    user_data = pd.DataFrame({
        'ORDERDATE': [pd.to_datetime(date)],
        'PRODUCTLINE': [productline],
        'CUSTOMERNAME': [customer]
    })

    df = user_data.copy()
    
    # MÜŞTERİ SEGMENTLERİNİN ENTEGRESİ
    user_data['SEGMENT'] = user_data['CUSTOMERNAME'].map(segment_map)

    # MÜŞTERİLERİN ENCODE EDİLMESİ
    user_data['CUSTOMERNAME'] = user_data['CUSTOMERNAME'].map(customer_map)

    # KÜMELEME SONUÇLARININ ENTEGRESİ
    user_data['CLUSTER-PRODUCTLINE'] = user_data['PRODUCTLINE'].map(cluster_productline_map)

    # OHE UYGULAMA
    user_data = OHEHandler(ohe, user_data, 'PRODUCTLINE')

    # TARİHTEN ÖZELLİK ÇIKARIMI
    user_data = extract_date_features(user_data, 'ORDERDATE', us_holidays)

    # STANDARTLAŞTIRMA
    user_data_scaled = sc.transform(user_data)

    # TAHMİN YAPMA
    y_pred = model.predict(user_data_scaled)

    # VERİ SETİNİN SON HALİ
    y_pred = np.round(y_pred,0)
    df['SALES'] = np.round(y_pred,0)
    
    return df


def display_prediction(segment_map=segment_map, customer_map=customer_map, cluster_productline_map=cluster_productline_map, ohe=ohe, us_holidays=us_holidays, model=model, sc=sc):

    container = st.container(
        border=True,
        height=250
    )
    
    container.markdown(
        """
        ## Model İnşa Süreci

        Bu sayfada, satış verilerinin tahmini için oluşturulan makine öğrenmesi modellerinin sonuçlarını bulabilirsiniz. Çeşitli Zaman serisi analizler, derin öğrenme ile yapılan satış tahminlemeleri yapılmış 
        en iyi performansı gösteren model, **GradientBoostingRegressor** ve **XGBRegressor** ile stack edilmiş **LinearRegression** olmuştur.
        
        Aşağıda modelin hiperparametreleri ve performans metriklerine ilişkin detayları bulabilirsiniz.
        """
    )
    
    col1, col2 = st.columns((2,1))
    
    with col1: 
        container = st.container(
            border=True,
            height=290
        )
        
        container.markdown(
            """
            ## Hiperparametreler

            En iyi hiperparametreleri bulma sürecinde hedef değişken üzerinde çeşitli oynamalar yapılmış,
            özellik çıkarım mühendisliği uygulanmış, ensemble tahminler stacked modeller gibi çeşitli süreçler incelenmiştir. 
            En iyi modeli bulma sürecindeki yapılan çalışmaların detayına
            [buradaki](https://github.com/AshNumpy/Sales-End-to-End-ML-Project) proje dosyasında bulunan 
            `./Mahine-Learning/customer-purchase-prediction.ipynb` uzantısından ulaşabilirsiniz.            
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        container = st.container(
            border=True,
            height=290
        )
        
        container.markdown(
            """
            ## Metrikler
            
            🎷 Ortalama Mutlak Hata
            
            <p style="
                    font-weight: bold;
                    color: white;
                    padding: 5px 10px 5px 10px;
                    background-color: #2C2E30;
                    border-radius: 10px;
                    text-align: center
                    ">$848.13</p>
                    
            🎺 Ortalama Hata Yüzdesi
            
            <p style="
                    font-weight: bold;
                    color: white;
                    padding: 5px 10px 5px 10px;
                    background-color: #2C2E30;
                    border-radius: 10px;
                    text-align: center
                    ">29.3%</p>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown(
        """
            <details>
                <summary 
                style="
                    font-weight: bold;
                    color: white;
                    padding: 5px 10px 5px 10px;
                    background-color: #2C2E30;
                    border-radius: 10px
                    ">Hiperparametrelerin detayları</summary>
                    
            ```python
            StackingRegressor(
                estimators=[
                    (
                    'gbr', GradientBoostingRegressor(
                        learning_rate=0.01,
                        max_depth=7,
                        n_estimators=300,
                        subsample=0.8)
                    ),
                    (
                    'xgb', XGBRegressor(
                        base_score=None,
                        booster=None,
                        callbacks=None,
                        colsample_bylevel=None,
                        colsample_bynode=None,
                        colsample_bytree=0.9, device=None,
                        early_stopping_rounds=None,
                        enable_categorical=False,
                        eval_metric=None,
                        feature_type...
                        importance_type=None,
                        interaction_constraints=None,
                        learning_rate=0.05, max_bin=None,
                        max_cat_threshold=None,
                        max_cat_to_onehot=None,
                        max_delta_step=None, max_depth=7,
                        max_leaves=None, min_child_weight=1,
                        missing=nan,
                        monotone_constraints=None,
                        multi_strategy=None,
                        n_estimators=100, n_jobs=None,
                        num_parallel_tree=None,
                        random_state=None, ...)
                    )
                ],
                final_estimator=LinearRegression()
            )            
            ```
            
            </details>
            <br>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        container = st.container(
            border=False,
            height=170
        )
        
        container.markdown(
            """
            <style>
            .container {
                text-align: center;
                justify-content: center;
            }
            .container svg {
                transition: transform 0.7s ease;
                margin: 5px;
            }
            .container svg:hover {
                transform: scale(1.3);
            }
            </style>
            <div class="container">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-calendar-week-fill" viewBox="0 0 16 16">
                    <path d="M4 .5a.5.5 0 0 0-1 0V1H2a2 2 0 0 0-2 2v1h16V3a2 2 0 0 0-2-2h-1V.5a.5.5 0 0 0-1 0V1H4zM16 14V5H0v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2M9.5 7h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5m3 0h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5M2 10.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5zm3.5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5"/>
                </svg>
                <p style="
                    margin: 10px;
                    font-size: 28px; 
                    font-weight: 600; 
                    background-color: transparent;
                    border: 2px solid currentColor;
                    border-radius: 50px;
                    ">Tarih</p> 
            </div>
            
            """,
            unsafe_allow_html=True
        )
        import datetime
        
        date_select = container.date_input(
            'Tarih',
            min_value=datetime.date(2003, 1, 6),
            max_value=datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day),
            value=datetime.date(2005, 6, 1),
            format='YYYY-MM-DD',
            label_visibility='collapsed',
            help="Belirlenen modelin eğitildiği tarihler 2003'den 2005'e kadardır."
        )

    with col2:
        container = st.container(
            border=False,
            height=170
        )
        
        container.markdown(
            """
            <style>
            .container {
                text-align: center;
                justify-content: center;
            }
            .container svg {
                transition: transform 0.7s ease;
            }
            .container svg:hover {
                transform: scale(1.3);
                
            }
            </style>
            <div class="container">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill=currentColor class="bi bi-archive-fill" viewBox="0 0 16 16" style="">
                    <path d="M12.643 15C13.979 15 15 13.845 15 12.5V5H1v7.5C1 13.845 2.021 15 3.357 15zM5.5 7h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1 0-1M.8 1a.8.8 0 0 0-.8.8V3a.8.8 0 0 0 .8.8h14.4A.8.8 0 0 0 16 3V1.8a.8.8 0 0 0-.8-.8z"/>
                </svg>
                <p style="
                    margin: 10px;
                    font-size: 28px; 
                    font-weight: 600; 
                    background-color: transparent;
                    border: 2px solid currentColor;
                    border-radius: 50px;
                    ">Ürün</p> 
            </div>
            
            """,
            unsafe_allow_html=True
        )
        
        product_select = container.selectbox(
            'Ürün',
            options=cluster_productline_map.keys(),
            label_visibility='collapsed',
            index=None
        )

    with col3:
        container = st.container(
            border=False,
            height=170
        )
        
        container.markdown(
            """
            <style>
            .container {
                text-align: center;
                justify-content: center;
            }
            .container svg {
                transition: transform 0.7s ease;
            }
            .container svg:hover {
                transform: scale(1.3);
                
            }
            </style>
            <div class="container">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-people-fill" viewBox="0 0 16 16">
                    <path d="M7 14s-1 0-1-1 1-4 5-4 5 3 5 4-1 1-1 1zm4-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6m-5.784 6A2.24 2.24 0 0 1 5 13c0-1.355.68-2.75 1.936-3.72A6.3 6.3 0 0 0 5 9c-4 0-5 3-5 4s1 1 1 1zM4.5 8a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5"/>
                </svg>
                <p style="
                    margin: 10px;
                    font-size: 28px; 
                    font-weight: 600; 
                    background-color: transparent;
                    border: 2px solid currentColor;
                    border-radius: 50px;
                    ">Müşteri</p> 
            </div>  
            """,
            unsafe_allow_html=True
        )
        
        customer_select = container.selectbox(
            'Müşteri',
            options=segment_map.keys(),
            label_visibility='collapsed',
            index=None
        )
        
    try: 
        results = make_single_prediction(date_select, product_select, customer_select)
        
        st.toast("Tahminleme işlemi tamamlandı.", icon="✅")
        
        container = st.container(
            border=True,
            height=210
        )
        
        container.markdown(
            f"""
            ### Yorum
            
            Tahmini olarak **{date_select}** Tarihinde, müşterilerimizden
            **{customer_select}**, ürün gruplarımızdan **{product_select}** grubundan
            **${int(results['SALES'][0])}** kadar satın alım gerçekleştirecektir.
            """,
            unsafe_allow_html=True
        )
        
        container.markdown(
            """
            <style>
                .Btn {
                    width: 130px;
                    height: 40px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background-color: #2c2e30;
                    border: none;
                    color: white;
                    font-weight: 600;
                    gap: 8px;
                    cursor: pointer;
                    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.103);
                    position: relative;
                    overflow: hidden;
                    transition-duration: .3s;
                }
                
                .svgIcon {
                    width: 16px;
                }
                
                .Btn::before {
                    width: 130px;
                    height: 130px;
                    position: absolute;
                    content: "";
                    background-color: white;
                    border-radius: 50%;
                    left: -100%;
                    top: 0;
                    transition-duration: .3s;
                    mix-blend-mode: difference;
                }
                
                .Btn:hover::before {
                    transition-duration: .3s;
                    transform: translate(100%,-50%);
                    border-radius: 0;
                }
                
                .Btn:active {
                    transform: translate(5px,5px);
                    transition-duration: .3s;
                }
            </style> 
            """,
            unsafe_allow_html=True
        )
        
        container.markdown(
            f"""
            <button class="Btn">
                ${int(results['SALES'][0])}
            <svg class="svgIcon" viewBox="0 0 576 512" fill="currentColor"><path d="M512 80c8.8 0 16 7.2 16 16v32H48V96c0-8.8 7.2-16 16-16H512zm16 144V416c0 8.8-7.2 16-16 16H64c-8.8 0-16-7.2-16-16V224H528zM64 32C28.7 32 0 60.7 0 96V416c0 35.3 28.7 64 64 64H512c35.3 0 64-28.7 64-64V96c0-35.3-28.7-64-64-64H64zm56 304c-13.3 0-24 10.7-24 24s10.7 24 24 24h48c13.3 0 24-10.7 24-24s-10.7-24-24-24H120zm128 0c-13.3 0-24 10.7-24 24s10.7 24 24 24H360c13.3 0 24-10.7 24-24s-10.7-24-24-24H248z"></path></svg>
            </button>
            """,
            unsafe_allow_html=True
        )
    
    except:
        st.warning('Lütfen Ürün ve Müşteri Seçiniz', icon="⚠️")
        