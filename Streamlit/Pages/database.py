import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL", "https://mxnrqdursjketupxahqc.supabase.co")
key: str = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im14bnJxZHVyc2prZXR1cHhhaHFjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTg0NDMzNDIsImV4cCI6MjAzNDAxOTM0Mn0.5dovWWqwyngMKPR1WLeihw60Uqgw-SqNRsQn9nbSpRc")
supabase: Client = create_client(url, key)

orders_json = supabase.from_("Orders").select("*").execute().data
order_items_json = supabase.from_("Order_Items").select("*").execute().data
product_json = supabase.from_("Products").select("*").execute().data
customers_json = supabase.from_("Customers").select("*").execute().data

import pandas as pd
import numpy as np

orders = pd.DataFrame(orders_json)
order_items = pd.DataFrame(order_items_json)
products = pd.DataFrame(product_json)
customers = pd.DataFrame(customers_json)

import streamlit as st

def display_database():
    def get_page(html_path):
        
        with open(html_path, 'r', encoding='utf-8') as f:
            home_page = f.read()
            
        return home_page
    
    col1, col2 = st.columns(2)
    
    with col1:
        container = st.container(
            border=True,
            height=316
        )
        
        container.markdown(
            """
            ## Veriler Hakkında
            
            Bu projede, satış verileri `./sales_data_sample.csv` dosyasından toplanarak veritabanı yapısına uyarlanmış
            ve farklı tablolar halinde organize edilmiştir. Tabloların ve sütunların tanımları,
            DBML sorgusu ile belirtilmiş olup, bu sorgular `./PostgreSQL/schema_dbml.sql` dosyasında bulunmaktadır.
            """
        )
        
    with col2:
        container = st.container(
            border=True,
            height=100
        )
        
        container.markdown(
            """
            <style>
            .container {
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container img {
                transition: transform 0.3s ease;
            }
            .container img:hover {
                transform: scale(1.3);
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        container.markdown(
            f"""
            <a href="https://www.kaggle.com/datasets/kyanyoga/sample-sales-data" target="_blank">
                <div class="container">
                    <img src="https://www.vectorlogo.zone/logos/kaggle/kaggle-ar21.svg" width="100">
                </div>
            </a>
            """,
            unsafe_allow_html=True, 
        )
        
        container = st.container(
            border=True,
            height=200
        )
        
        container.markdown(
            """
            Veritabanı tasarımı, verilerin daha etkili ve organize bir şekilde yönetilmesini
            sağlar ve bu veriler üzerinden yapılacak analizler ve tahminler için temel oluşturur.
            Aşağıdaki görsel, veritabanı şemasını detaylı olarak göstermektedir.
            """
        )
    
    container = st.container(
        border=False,
        height=250
    )
    
    db_relation = get_page("./Database/db-relation.html")
    
    container.markdown(
       f"""
        {db_relation}
       """,
       unsafe_allow_html=True, 
    )
    
    container = st.container(
        border=False,
        height=400
    )
    database = container.selectbox(
        '',
        ["Orders", "Order Items", "Products", "Customers"],
        index=3,
        placeholder="Ön Gösterim İçin Bir Database Seçin"
    )
    
    if database == "Orders":
        container.dataframe(orders, use_container_width=True, hide_index=True)
    elif database == "Order Items":
        container.dataframe(order_items, use_container_width=True, hide_index=True)
    elif database == "Products":
        container.dataframe(products, use_container_width=True, hide_index=True)
    elif database == "Customers":
        container.dataframe(customers, use_container_width=True, hide_index=True)