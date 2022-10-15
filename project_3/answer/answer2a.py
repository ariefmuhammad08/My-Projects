from distutils import errors
import json
import psycopg2 as pg
from zipfile import ZipFile
import pandas as pd
from sqlalchemy import create_engine

schema_json= 'sql/schemas/user_address.json'
zip_file= 'temp/dataset-small.zip'
file_name= 'dataset-small.csv'

database='shipping_orders'
user= 'postgres'
password= 'postgres'
host= '127.0.0.1'
port= '5432'

table_name='user_address_2018_snapshots'

# membaca json
with open(schema_json,'r') as schema:
        content= json.loads(schema.read())


# membuat schema dari json
list_schema= []
for c in content:
    col_name= c['column_name']
    col_type= c['column_type']
    constraint= c['is_null_able']
    ddl_list= [col_name, col_type, constraint]
    list_schema.append(ddl_list)


# membuat schema menjadi tuple
list_schema2= []
for l in list_schema:
    s= ' '.join(l)
    list_schema2.append(s)


# membuat ddl sql query dari tuple
create_schema_sql = """create table user_address_2018_snapshots {};"""
create_schema_sql_final = create_schema_sql.format(tuple(list_schema2)).replace("'", "")


# koneksi ke postgres
conn= pg.connect(database=database,
                    user=user,
                    password=password,
                    host=host,
                    port=port)

conn.autocommit= True
cursor= conn.cursor()


# eksekusi command ddl
try:
    cursor.execute(create_schema_sql_final)
    print('DDL schema created succesfully...')
except pg.errors.DuplicateTable:
    print('table already created...')


# load zipped file ke dataframe
zf= ZipFile(zip_file)
df= pd.read_csv(zf.open(file_name), header=None)

col_name_df= [c['column_name'] for c in content]
df.columns= col_name_df


# filter data sebelum input ke database
df_filtered= df[(df['created_at']>='2018-02-01')&(df['created_at']<'2018-12-31')]


# create engine (digunakan untuk bulk insert)
engine= create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')


# insert data ke database
df_filtered.to_sql(table_name, engine, if_exists='append', index=False)
print(f'Total inserted rows:{len(df_filtered)}')
print(f'Initial created at:{df_filtered.created_at.min()}')
print(f'Last created at:{df_filtered.created_at.max()}')


# link github :
# https://github.com/ariefmuhammad08/digitalskola