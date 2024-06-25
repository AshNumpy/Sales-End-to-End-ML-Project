##################
#### GET DATA ####
##################

# Initialize Supabase
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL", "https://mxnrqdursjketupxahqc.supabase.co")
key: str = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im14bnJxZHVyc2prZXR1cHhhaHFjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTg0NDMzNDIsImV4cCI6MjAzNDAxOTM0Mn0.5dovWWqwyngMKPR1WLeihw60Uqgw-SqNRsQn9nbSpRc")
supabase: Client = create_client(url, key)

# Read database
orders_json = supabase.from_("Orders").select("*").execute().data
order_items_json = supabase.from_("Order_Items").select("*").execute().data
product_json = supabase.from_("Products").select("*").execute().data
customers_json = supabase.from_("Customers").select("*").execute().data

# Convert to pandas
import pandas as pd
import numpy as np

orders = pd.DataFrame(orders_json)
order_items = pd.DataFrame(order_items_json)
products = pd.DataFrame(product_json)
customers = pd.DataFrame(customers_json)

df = order_items.merge(
    orders, on = 'ORDERNUMBER', how='left'
    ).merge(
        products, on = 'PRODUCTCODE', how='left'
        ).merge(
            customers, left_on = 'CUSTOMER-ID', right_on='ID', how='left'
            )
        
df = df[['ORDERDATE', 'SALES', 'PRODUCTLINE', 'CLUSTER-PRODUCTLINE', 'CUSTOMERNAME', 'SEGMENT']]

print(df.head(3))
print("="*100)


####################################
#### CREATE CLASS AND FUNCTIONS ####
####################################

# CUSTOMER MAP
df['CUSTOMERNAME-CODED'] = df['CUSTOMERNAME'].astype('category').cat.codes
customer_map = df[['CUSTOMERNAME', 'CUSTOMERNAME-CODED']].drop_duplicates().set_index('CUSTOMERNAME').to_dict()['CUSTOMERNAME-CODED']
df.drop(['CUSTOMERNAME-CODED'], axis=1, inplace=True)

# CLUSTER-PRODUCTLINE MAP
cluster_productline = df.groupby(['PRODUCTLINE'])['CLUSTER-PRODUCTLINE'].mean().reset_index(name="CLUSTER-PRODUCTLINE")
cluster_productline_map = cluster_productline.set_index('PRODUCTLINE').to_dict()['CLUSTER-PRODUCTLINE']
df.drop('CLUSTER-PRODUCTLINE', axis=1, inplace=True)

# DATE EXTRACTION PART
import holidays

us_holidays = holidays.US()

def extract_date_features(df, date_column, holidays_list):
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

# OH ENCODER
def OHEHandler(fitted_encoder, df, col):    
    
    encoded_col = fitted_encoder.transform(df[col])
    encoded_df = pd.DataFrame(encoded_col.toarray(), columns=fitted_encoder.get_feature_names_out())
    
    return encoded_df


###########################
#### PREPARE THE MODEL ####
###########################

# EXTRACT AND ENCODE THE DATA
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
df = df.astype({'SEGMENT': 'int'})

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def OHEHandler(fitted_encoder, df, col):
    # Encoded column
    encoded_col = fitted_encoder.transform(df[col].values.reshape(-1, 1))
    
    # Convert to DataFrame and keep original index
    encoded_df = pd.DataFrame(encoded_col.tolist(), 
                              columns=fitted_encoder.get_feature_names_out(), 
                              index=df.index)
    
    # Drop the original column and concatenate the encoded DataFrame
    df = pd.concat([df.drop(columns=[col]), encoded_df], axis=1)
    
    return df

# DATE EXTRACTION
df = extract_date_features(df, 'ORDERDATE', us_holidays)

# CUSTOMER MAP
df = df.replace({'CUSTOMERNAME': customer_map})

# CLUSTER IMPLEMENTATION
df['CLUSTER-PRODUCTLINE'] = df['PRODUCTLINE'].map(cluster_productline_map)

# Fitting OneHotEncoder
ohe = OneHotEncoder(handle_unknown='infrequent_if_exist', drop='first', sparse_output=False)
ohe.fit(df['PRODUCTLINE'].values.reshape(-1, 1))

# Transforming DataFrame
df = OHEHandler(ohe, df, 'PRODUCTLINE')

# SPLIT DATA 
from sklearn.model_selection import train_test_split

X = df.drop(['SALES'], axis=1).values
y = df['SALES']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# SCALER
from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler(feature_range=(0, 1))
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#####################
### TAHMİN YAPMA ####
#####################

from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import StackingRegressor

# En iyi GBR parametreleri
gbr_params = {
    'learning_rate': 0.01,
    'max_depth': 7, 
    'min_samples_leaf': 1, 
    'min_samples_split': 2, 
    'n_estimators': 300, 
    'subsample': 0.8
    }

# En iyi XGBoost parametreleri    
xgb_params = {
    'colsample_bytree': 0.9, 
    'learning_rate': 0.05, 
    'max_depth': 7, 
    'min_child_weight': 1, 
    'n_estimators': 100, 
    'subsample': 0.9
    }

# Base modelleri tanımlama
base_models = [
    ('gbr', GradientBoostingRegressor(**gbr_params)),
    ('xgb', XGBRegressor(**xgb_params))
]

# Meta modeli tanımlama
meta_model = LinearRegression()

# Stacking regressor
stacking_model = StackingRegressor(estimators=base_models, final_estimator=meta_model)

# Stacking modelini eğitme
stacking_model.fit(X_train, y_train)

y_pred = stacking_model.predict(X_test)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Performans metriklerini hesaplama
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
r2 = r2_score(y_test, y_pred)

# Sonuçları yazdırma
results = pd.DataFrame({
    'Model': ['StackingRegressor'],
    'Hiperparametreler': ['GradientBoostingRegressor, XGBRegressor, LinearRegression'],
    'RMSE': [rmse],
    'MAE': [mae],
    'MAPE': [mape],
    'R2': [r2]
})

print("="*100)
print(results)
print("="*100)

###############################
#### SON KULLANICI TAHMİNİ ####
###############################

# Kullanıcıdan veri alma
date = input("Tarih girin (YYYY-MM-DD): ")
productline = input("Urun kategorisi girin: ")
customer = input("Müşteri adını girin: ")

# Verileri işleme
user_data = pd.DataFrame({
    'ORDERDATE': [pd.to_datetime(date)],
    'PRODUCTLINE': [productline],
    'CUSTOMERNAME': [customer]
})

# DATE EXTRACTION
user_data = extract_date_features(user_data, 'ORDERDATE', us_holidays)

# CUSTOMER MAP
user_data['CUSTOMERNAME'] = user_data['CUSTOMERNAME'].map(customer_map)

# CLUSTER IMPLEMENTATION
user_data['CLUSTER-PRODUCTLINE'] = user_data['PRODUCTLINE'].map(cluster_productline_map)

# OneHotEncoding
user_data = OHEHandler(ohe, user_data, 'PRODUCTLINE')

# DataFrame tamamlamak için eksik sütunları doldurma
for col in df.drop(columns=['SALES']).columns:
    if col not in user_data.columns:
        user_data[col] = 0

# Verileri sıralama
user_data = user_data[df.drop(columns=['SALES']).columns]

# Scaling
user_data = sc.transform(user_data)

# Tahmin yapma
tahmin = stacking_model.predict(user_data)

print("Tahmin edilen satış: ", tahmin[0])