'''
Created on 20170426

@author: mao
'''
import numpy as np
import pylab as pl

def fitSLR(x,y):
    n=len(x)
    dinominator=0
    numerator=0
    for i in range(0,n):
        numerator+=(x[i]-np.mean(x))*(y[i]-np.mean(y))
        dinominator+=(x[i]-np.mean(x))**2
    print "numerator:",numerator
    print "dinominator:",dinominator
    b1=numerator/float(dinominator)
    b0=np.mean(y)/float(np.mean(x))
    return b0,b1

def predict(x,b0,b1):
    return b0+b1*x

x=[1,3,2,1,3]
y=[14,24,18,17,27]
b0,b1=fitSLR(x, y)
y_test=predict(6, b0, b1)

print "y_test:",y_test

xx=np.linspace(0,5)
yy=b0+b1*xx

pl.plot(xx,yy,'k-')
pl.scatter(x, y)
pl.axis('tight')
pl.show()


