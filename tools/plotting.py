import numpy as np
import pandas as pd 
from pandas.tseries.offsets import DateOffset
import matplotlib.pyplot as plt 


class plotter(object):
  def __init__(self):
    pass 


  def plot_top_locations(self, df):
    topsamplelocs = df.groupby('LOCATION').count().sort_values('X', ascending=False).head(20).index

    fig, ax = plt.subplots(1, 1, figsize=(25,5), facecolor='white')
    ax.set_title('algae blooms', fontsize=20)

    for location in topsamplelocs:
        df[df['LOCATION'] == location].set_index('dt')['COUNT_'].plot(ax=ax, label=location)

    ax.set_ylabel('cell count')
    ax.legend()
    ax.grid()

    plt.show()


  def plot_predictions_against_groundtruth(self, X_test, y_test, model, idx_test):
    assert model.trained == True 

    y_test['dt'] = idx_test 
    y_test.sort_values('dt', inplace=True)
    preds = pd.DataFrame({'COUNT_': model.predict(X_test), 'dt': idx_test})
    preds.sort_values('dt', inplace=True)

    fig, ax = plt.subplots(1, 1, figsize=(25,5), facecolor='white')

    ax.plot(y_test.set_index('dt'))
    ax.plot(preds.set_index('dt'))

    ax.grid()
    plt.show()


  def forecast(self, X, y, model, idx):
    def dater(year, month, day, hour):
      date = pd.to_datetime(year, format='%Y')
      date += DateOffset(months=month-1)
      date += DateOffset(days=day-1)
      date += DateOffset(hours=hour)
      
      return date

    X = X.copy(deep=True)
    X['year'] = X['year'] + 2
    X = X[X['year'] >= 2020]

    y['dt'] = idx 
    y.sort_values('dt', inplace=True)
    preds = pd.DataFrame({'COUNT_': model.predict(X)})
    preds['dt'] = list(map(dater, X['year'], X['month'], X['day'], X['hour']))
    preds.sort_values('dt', inplace=True)

    fig, ax = plt.subplots(1, 1, figsize=(25,10), facecolor='white')
    ax.set_title('forecasted algae bloom', fontsize=20)

    ax.plot(y.set_index('dt'), label='historical blooms')
    ax.plot(preds.set_index('dt'), label='forecasted blooms')

    ax.set_ylabel('cell count')
    ax.grid()
    ax.legend()

    plt.show()

