'''
Created on 20170425
test xor
@author: mao
'''
import numpy as np
from NeuralNetwork.nn import NeuralNetwork
nn=NeuralNetwork([2,2,1],'tanh')

X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([0,1,1,0])
#X=np.atleast_2d()
print X.shape[0]
print X.shape[1]
temp=np.ones([X.shape[0],X.shape[1]+1])
print temp
nn.fit(X, y)
for i in [[0,0],[0,1],[1,0],[1,1]]:
    print(i,nn.predict(i))