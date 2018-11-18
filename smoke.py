# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:13:59 2018, linear regression algorithm machine learning
@author: SHASHANK
"""
import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression


class Model:
    X = None
    Y = None
    
    # Importing the dataset
    def importData(self):
        dataset = pd.read_csv('smoke_data.csv')
        self.X = dataset.iloc[:, :-1].values
        self.Y = dataset.iloc[:, 1].values

    def predictAge(self):
        self.importData()
        
        # Fitting the Simple Linear Regression to the Training set
        regressor = LinearRegression()
      
        regressor.fit(self.X, self.Y)
        
        smokePerDay = float(raw_input("How many cigarettes do you smoke in a day? "))

        if smokePerDay > 30:
            print "You don't need ML to predict your death age, you will die very soon."
        else:
           age = regressor.predict([[smokePerDay]])
           print "Your predicted age is ", int(round(age[0])) , "Years, if you start smoking from the day one."


model = Model()
model.predictAge()
