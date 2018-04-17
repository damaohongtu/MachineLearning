import matplotlib.pyplot as plt
import math
import numpy as np
#CREATE A RANDOM DATASET
def createDateSet(nData):
    #-1-1之间产生100个点
    xGrid=linespace(-1,1,100)
    #随机产生nData个x轴的坐标
    x=2*(np.randn(nData)-0.5)
    #matlab的inline函数，python的lamabda函数
    #DEFINE AND TARGET FUNCTION f(x)
    f=lamabda
    y=f(x)+noiseSTD*randn(len(x))
    return x,y

#多项式拟合，返回参数
def fitPolyNomial(x,y):
    degreee=[1,3,10]
    #建立字典用来保存参数
    theta={}
    for iD in range(len(degreee)):
        theta[iD]=polyfit(x,y,degreee[iD])
    return theta
