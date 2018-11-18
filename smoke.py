import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression


class Model:
    X = None
    Y = None
    X_train = None
    Y_train = None
    X_test = None
    Y_test = None
    
    # Importing the dataset
    def importData(self):
        dataset = pd.read_csv('smoke_data.csv')
        self.X = dataset.iloc[:, :-1].values
        self.Y = dataset.iloc[:, 1].values

    # Splitting the dataset into the Training set and Test set
    def createTestSets(self):
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y)

    def predictAge(self):
        self.importData()
        self.createTestSets()
        
        # Fitting Simple Linear Regression to the Training set
        regressor = LinearRegression()
        regressor.fit(self.X_train, self.Y_train)
        
        smokePerDay = float(raw_input("How many cigarettes do you smoke in a day? "))

        if smokePerDay > 30:
            print "You don't need ML to predict your death age, you will die very soon."
        else:
           age = regressor.predict([[smokePerDay]])
           print "Your predicted age is ", int(round(age[0])) , "Years, if you start smoking from the day one."


model = Model()
model.predictAge()
