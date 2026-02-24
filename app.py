import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("superstore.csv")
df.dropna(inplace=True)

engine = create_engine("postgresql://admin:admin@db:5432/superstore")

df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("Data uploaded successfully!")