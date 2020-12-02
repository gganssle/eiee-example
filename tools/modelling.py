import numpy as np
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


class rf(object):
  def __init__(self):
    self.model = RandomForestRegressor(n_jobs=-1)
    self.trained = False


  def fit(self, X_train, y_train):
    self.model.fit(X_train, y_train)
    self.trained = True

  
  def predict(self, X):
    return self.model.predict(X)


  def accuracy(self, X_test, y_test):
    assert self.trained == True
    return r2_score(y_test, self.model.predict(X_test))