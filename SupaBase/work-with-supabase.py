# Import environment variables
from dotenv import load_dotenv
load_dotenv("SupaBase/.env")

print("="*50)
print("Environment Load Result:")
print(load_dotenv("SupaBase/.env"))
print("="*50)

# Initialize Supabase
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Read Customer database
res = supabase.from_("Customers").select("*").execute()
json_data = res.data

# Use customer datas as pandas dataframe
import pandas as pd
df = pd.DataFrame(json_data)

print(df.head())
print("="*50)