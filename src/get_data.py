# -*- coding: utf-8 -*-
import os
import pandas as pd
import sqlalchemy

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Data_dir = os.path.join(Base_dir, 'data')

str_connection = 'sqlite:///{path}'

print('Diretório do projeto: ', Base_dir)
print('Diretório dos dados: ', Data_dir)

my_files = []

files_names = [i for i in os.listdir(Data_dir) if i.endswith('.csv')]
#print(files_names)

str_connection = str_connection.format(path=os.path.join(Data_dir, 'olist.db'))
#connection = sqlalchemy.create_engine(str_connection)

for i in files_names:
    df_tmp = pd.read_csv(os.path.join(Data_dir, i))
    print(df_tmp.head())
    db_name = 'fr_' + i.strip('.csv').replace('olist_', '').replace('_dataset','')
    df_tmp.to_sql(db_name, str_connection)