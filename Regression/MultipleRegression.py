'''
Created on 20170426

@author: mao
'''
from numpy import genfromtxt
import numpy as np
from sklearn import datasets,linear_model
dataPath=r"F:\WORKPLACE\java\decision_tree\data\regression_data.csv"
deliverData=genfromtxt(dataPath,delimiter=',')
print "data"
print deliverData

X=deliverData[:,:-1]
Y=deliverData[:,-1]
print "X:"
print X
print "Y:"
print Y

regr=linear_model.LinearRegression()
regr.fit(X, Y)
print "coefficients:"
print regr.coef_

print "intercept:"
print regr.intercept_

xPred=[102,6]
yPred=regr.predict(xPred)
print "yPred:"
print yPred





