# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:42:17 2016

@author: Shahidur Rahman
"""

import explorers
import stringRecorder
import pandas
from sqlalchemy import create_engine
import random
from mmh3 import hash128
#from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

engine = create_engine('mysql+pymysql://root:shahidur_123@localhost:3306/mwt')
j=0

#Data generation 
import numpy as np
#import pdb;pdb.set_trace()
mu, sigma = 0, 1
actionValue = np.random.normal(mu, sigma, 200000)
#type(actionValue)
minVal = np.amin(actionValue)
maxVal = np.amax(actionValue)
trainData = np.random.normal(mu, sigma, 200000)
testValue = np.random.normal(mu, sigma, 200000)
#s1 = np.empty(2000, dtype=np.int)
for i in range(0,200000):
    #reward generation
    trainData[i] = int(round(0 + (trainData[i]-minVal)*(1-0)/(maxVal-minVal),0))
    #action generation
    actionValue[i] = int(round(1 + (actionValue[i]-minVal)*(10-1)/(maxVal-minVal),0))
    #testData
    testValue[i] = int(round(1 + (testValue[i]-minVal)*(10-0)/(maxVal-minVal),0))

X = [0] * 200000
Y = [0] * 200000
X1 = [0] * 200000
y1 = [0] * 200000

from random import randint
for i in range(0,200000):
    X[i] = [randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), actionValue[i]]
    Y[i] = [randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)]

#train data set up actionValue
for i in range(0,200000):
    X1[i], y1[i] = [np.asarray(X[i])[0], np.asarray(X[i])[1], np.asarray(X[i])[2], np.asarray(X[i])[3], 
        np.asarray(X[i])[4], np.asarray(X[i])[5]], actionValue[i]

#train data setup rewardValue
X2, y2 = X, trainData

#model action selection
from sklearn import svm
clf = svm.SVC(kernel='rbf')
modelActionSelection = clf.fit(X1, y1)

#model reward allocation
clf = svm.SVC(kernel='rbf')
modelRewardAllocation = clf.fit(X2, y2)

for i in range(0,200000):
    
    #epsilon
    epsilon = round(random.random(),3)
    
    #unique number generator 
    unique_key =hash128('my string of doom ', seed=1234)
    
    ##of actions
    noOfActions = 10
    print(i)
    #policy decision 
    policyDecision = modelActionSelection.predict(Y[i])
    
    #print("predict["+str(i)+"] is "+str(predict))
    for x in policyDecision:
        policyDecision = int(x)
        
    #scores
    scores = [.2,.5,.3]
    
    callExplorer = explorers.explorers(epsilon,noOfActions,policyDecision,scores)
    storeValues = callExplorer.algoSelection()
    
    #reward check dataset
    rewardCheckData = [np.asarray(Y[i])[0], np.asarray(Y[i])[1], np.asarray(Y[i])[2], np.asarray(Y[i])[3], 
        np.asarray(Y[i])[4], np.asarray(Y[i])[5], storeValues['actionID']]
    rewardValue = int(modelRewardAllocation.predict(rewardCheckData))
    
    record = stringRecorder.stringRecorder(str(Y[i]), str(storeValues['actionID']),str(storeValues['actionProbability']), str(unique_key), str(storeValues['isExplore']), str(epsilon), str(noOfActions),str(policyDecision),str(storeValues['explorerAlgo']), str(rewardValue))
    record = record.sewStrings()
    #print('record : '+str(record))
    
    colList="context,actionID,actionProbability,unique_key,isExplore,epsilon,noOfActions,policyDecision,explorerAlgo,rewardValue".split(',')
    #c1=['col1']
    df = pandas.DataFrame(data=record,index=colList)
    #transpose the data
    df=df.T
    #print("printing panda df here")
    #print(df)
    #push data in sql
    #rf = pandas.DataFrame(data=['10',1,2,'62019057582468709482189373788949966293',4,5,6,7,'8'],index=colList)
    #rf=rf.T
    #rf.to_sql(con=engine, name='stringrecord', if_exists='append', index=False)
    df.to_sql(con=engine, name='stringrecord', if_exists='append', index=False)
    df.to_sql(con=engine, name='stringrecord_test', if_exists='append', index=False)
    
    
    
    
    
    
    
    