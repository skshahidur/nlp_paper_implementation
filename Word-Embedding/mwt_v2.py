# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 19:42:51 2017

@author: Shahidur Rahman
"""

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
import numpy as np
import ast
#warning suppress
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#connection
engine = create_engine('mysql+pymysql://root:shahidur_123@localhost:3306/mwt')
j=0

#Data read from MySQL Server
##train for actionValue
sR_context = "select context from stringRecord limit 10;"
sR_actionValue = "select actionID from stringRecord limit 10;"
sR_rewardValue = "select rewardValue from stringRecord limit 10;"
dataX1 = pandas.read_sql_query(sql=sR_context,con=engine)
dataX1 = dataX1.values.tolist()
dataY1 = pandas.read_sql_query(sql=sR_actionValue,con=engine)
dataY1 = dataY1.values.tolist()
dataY2 = pandas.read_sql_query(sql=sR_rewardValue,con=engine)
dataY2 = dataY2.values.tolist()

X1 = [0] * 10
Y1 = [0] * 10
X2 = [0] * 10
Y2 = [0] * 10
Y = [0] * 10
#data for actionValue & rewardValue training
for i in range(0,10):
    lstX1 = ast.literal_eval(dataX1[i][0])
    lstY1 = ast.literal_eval(dataY1[i][0])
    lstY2 = ast.literal_eval(dataY2[i][0])
    X1[i], Y1[i] = [lstX1[0], lstX1[1], lstX1[2], lstX1[3], lstX1[4], lstX1[5]], lstY1
    X2[i], Y2[i] = [lstX1[0], lstX1[1], lstX1[2], lstX1[3], lstX1[4], lstX1[5], lstY1], lstY2
    
#training model for actionValue
from sklearn import svm
clf = svm.SVC(kernel='rbf')
modelActionSelection = clf.fit(X1, Y1)

#training model for rewardValue
clf = svm.SVC(kernel='rbf')
modelRewardAllocation = clf.fit(X2, Y2)

# context data for testing model
from random import randint
for i in range(0,10):
    Y[i] = [randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)]

        
for i in range(0,10):
    
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
    
    
    
    
    
    
    


        