import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
password =quote_plus("@lfeshahzeb")
engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/Ecommerce"
)
list_csvs=[
    ('customers','customers.csv'),
    ('geolocation','geolocation.csv'),
    ('order_items','order_items.csv'),
    ('orders','orders.csv'),
    ('payments','payments.csv'),
    ('products','products.csv'),
    ('sellers','sellers.csv')
]
for table,file in list_csvs:
    filepath=f"./file/{file}"
    df = pd.read_csv(filepath)
    df.columns=df.columns.str.replace(" ","_")
    df.to_sql(
        name=table,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"Imported {file} successfully into {table}")
engine.dispose() 

