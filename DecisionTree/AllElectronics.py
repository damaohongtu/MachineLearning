'''
Created on 20170424
@author: mao
'''
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
from __builtin__ import str
#open the csv file
allElectronicsData=open(r'F:\WORKPLACE\java\decision_tree\data\test.csv','rb')
reader=csv.reader(allElectronicsData)
headers=reader.next()
print(headers)

featureList=[]
labelList=[]

for row in reader:
    labelList.append(row[len(row)-1])
    rowDict={}
    for i in range(1,len(row)-1):
        rowDict[headers[i]]=row[i]
    featureList.append(rowDict)
print(featureList)

vec=DictVectorizer()
dummyX=vec.fit_transform(featureList).toarray()
print("dummyX:"+str(dummyX))
print(vec.get_feature_names())
print("labelList:"+str(labelList))
    
lb=preprocessing.LabelBinarizer()
dummyY=lb.fit_transform(labelList)
print("dummyY:"+str(dummyY))

clf=tree.DecisionTreeClassifier(criterion='entropy')
clf=clf.fit(dummyX,dummyY)
print("clf:"+str(clf))

with open("test.dot",'w')as f:
    f=tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)

#predict
oneRowX=dummyX[0,:]
print("oneRowX:"+str(oneRowX))

newRowX=oneRowX
newRowX[0]=1  
newRowX[1]=0  
print("newRowX:"+str(newRowX))
predictedY=clf.predict(newRowX)
print("predictedY:"+str(predictedY))






    