'''
Created on 20170424

@author: mao
'''
import csv
import random
import operator
import math 


def loadDataset(filename,split,trainset=[],testset=[]):
    with open(filename,'rb')as csvfile:
        lines=csv.reader(csvfile)
        dataset=list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y]=float(dataset[x][y])
            if random.random()<split:
                trainset.append(dataset[x])
            else:
                testset.append(dataset[x])

def enclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(distance)

def getNeighbors(trainset,testInstance,k):
    distance=[]
    length=len(testInstance)-1
    for x in range(len(trainset)):
        dist=enclideanDistance(testInstance, trainset[x], length)
        distance.append((trainset[x],dist))
    distance.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distance[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response]=1
    sortedVotes=sorted(classVotes.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet,prediction):
    correct=0
    for x in range(len(testSet)):
        if testSet[x][-1]==prediction[x]:
            correct+=1
    return (correct/float(len(testSet)))*100
        

def main():
    trainSet=[]
    testSet=[]
    split=0.67
    loadDataset(r'F:\WORKPLACE\java\decision_tree\data\iris.data.txt', split, trainSet, testSet)
    print 'Train set:'+repr(len(trainSet))
    print 'Test set:'+repr(len(testSet))    
    prediction=[]
    k=3
    for x in range(len(testSet)):
        neighbors=getNeighbors(trainSet, testSet[x], k)
        result=getResponse(neighbors)
        prediction.append(result)
    accuracy=getAccuracy(testSet, prediction)
    print('Accuracy:'+repr(accuracy))
main()