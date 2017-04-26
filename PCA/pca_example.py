# -*- coding: utf-8 -*-
'''
Created on 20170426

@author: mao
'''
import numpy as np

def zeroMean(dataMat):
    meanVal=np.mean(dataMat,axis=0) #按列求均值
    newData=dataMat-meanVal
    return newData,meanVal

# dataMat=[[1,2,3],[4,5,6],[7,8,9]]
# newData,meanVal=zeroMean(dataMat)
# print "newData:",newData
# print "meanVal:",meanVal
# 
# covMat=np.cov(newData,rowvar=0)
# print "covMat:",covMat
# 
# eigVals,eigVects=np.linalg.eig(np.mat(covMat)) 
# print "eigVals:",eigVals
# print "eigVects:",eigVects
def percentage2n(eigVals,percentage):  
    sortArray=np.sort(eigVals)   
    sortArray=sortArray[-1::-1]  
    arraySum=sum(sortArray)  
    tmpSum=0  
    num=0  
    for i in sortArray:  
        tmpSum+=i  
        num+=1  
        if tmpSum>=arraySum*percentage:  
            return num
        
def pca(dataMat,percentage=0.99):
    
    newData,meanVal=zeroMean(dataMat)
    covMat=np.cov(newData,rowvar=0)
    eigVals,eigVects=np.linalg.eig(np.mat(covMat))  #取得特征值，特征向量
    
    eigValIndice=np.argsort(eigVals)
    n=percentage2n(eigVals,percentage)
    n_eigValIndice=eigValIndice[-1:-(n+1):-1]
    n_eigVect=eigVects[:,n_eigValIndice]  
    lowDDataMat=newData*n_eigVect   #低维特征空间数据
    reconMat=(lowDDataMat*n_eigVect.T)+meanVal #重构数据
    return lowDDataMat,reconMat

dataMat=[[1,2,3],[4,5,6],[7,8,9]]
lowDDataMat,reconMat=pca(dataMat)
print "lowDDataMat:",lowDDataMat
print "reconMat:",reconMat





