import sqlite3
import pandas as pd

conn = sqlite3.connect('E-commerce Customer Behavior - Sheet1.db')

df = pd.read_csv('E-commerce Customer Behavior - Sheet1.csv')
df.to_sql('ecomm', conn, if_exists='replace', index=False)

conn.commit()
conn.close()