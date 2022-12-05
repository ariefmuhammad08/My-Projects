import pandas as pd
from sqlalchemy import create_engine


database='postgres'
user= 'postgres'
password= 'postgres'
host= '127.0.0.1'
port= '5432'

# membaca csv
data_property= pd.read_csv('dataset/TR_PropertyInfo.csv')
data_user= pd.read_csv('dataset/TR_UserInfo.csv')

# mengganti nama kolom tabel
col_p= {"Prop ID":"prop_id", "PropertyCity":"property_city", "PropertyState":"property_state"}
col_u= {"UserID":"user_id", "UserSex":"user_sex", "UserDevice":"user_device"}

data_property= data_property.rename(columns=col_p)
data_user= data_user.rename(columns=col_u)

#koneksi ke postgres
conn= create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

# input data ke postgres
data_property.to_sql('property', conn, if_exists='append', index=True)
data_user.to_sql('user', conn, if_exists='append', index=True)