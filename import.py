import pandas as pd
import numpy as np
from datetime import datetime as dt
from sqlalchemy import create_engine
import urllib
import openpyxl
import csv

params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=database_source;DATABASENAME;Trusted_Connection=yes")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params,fast_executemany=True)
engine.connect()

tables1 = ['TABLE_A', 'TABLE_B', 'TABLE_C']
for table1 in tables1:
  sql_df = f'SELECT * FROM datasource ..{table1}'
  df = pd.read_sql(sql_df,engine)
  df.to_excel(f'{table1}.xlsx', sheet_name='sheet1', index=False)
  
  
# you can use 'to_excel' or 'to_csv'
