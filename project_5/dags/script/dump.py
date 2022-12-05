import os
import pandas as pd
import numpy as np

import psycopg2
from sqlalchemy import create_engine


if __name__ == "__main__" :
    listfile= ['bigdata_customer', 'bigdata_product', 'bigdata_transaction']
    for file in listfile :
        # read data
        path= os.getcwd()+'/data/'
        df= pd.read_csv(path+file+'.csv')

        # connection
        url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'
        engine= create_engine(url)

        # dump data
        try :
            df.to_sql(file, index=False, con=engine, if_exists='replace')
            print(f'data {file} success dump to database')
        except:
            print(f'data {file} failed')