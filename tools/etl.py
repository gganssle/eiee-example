import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split


class ETLs(object):
  def __init__(self):
    pass 


  def time_format(self, df):
    df['tformat'] = df['TIME'].fillna('00:00:00')
    df['dt'] = list(map(lambda x, y: x[:10] + ' ' + y, df['SAMPLE_DATE'], df['tformat']))
    df['dt'] = pd.to_datetime(df['dt'])

    return df


  def time_feature_gen(self, df):
    df['year'] = df['dt'].dt.year
    df['month'] = df['dt'].dt.month
    df['day'] = df['dt'].dt.day
    df['hour'] = df['dt'].dt.hour

    return df


  def prep_nonsequential_data(self, df):
    X = df[['LATITUDE', 'LONGITUDE', 'year', 'month', 'day', 'hour']]
    y = df[['COUNT_', 'dt']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    idx_train = y_train['dt']
    idx_test  = y_test['dt']
    y_train.drop('dt', inplace=True, axis=1)
    y_test.drop('dt', inplace=True, axis=1)

    return X_train, X_test, y_train, y_test, idx_train, idx_test


    