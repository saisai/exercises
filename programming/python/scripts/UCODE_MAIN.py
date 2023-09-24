import pandas as pd
from pandas.io import sql
import pymysql
from sqlalchemy import create_engine
import pandas_gbq
from UCODE import Channel_Stats

API_KEY = "<API>"
channel_id = ["UCLuR42wJEtpX5I-FaTcvViA","UCnMn36GT_H0X-w5_ckLtlgQ"]


def get_stats(channel_id):
    yt = Channel_Stats(API_KEY, channel_id)
    yt.extract_all()
    t = yt.save_and_return()
    return t

##
# Data = pd.DataFrame()
# project_name = 'rock-terra-306920'
# dataset_name = 'new_dataset'
# table_name = 'table_1'

for i in channel_id:
    Data = pd.concat([Data, get_stats(i)])
##
# print(Data)
# Data.to_gbq(destination_table='{}.{}'.format(dataset_name, table_name), project_id=project_name,
#                 if_exists='replace')
# Data.to_excel('financial_ed.csv')
# print(Data)
