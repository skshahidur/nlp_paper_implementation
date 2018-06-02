# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 13:39:19 2016

@author: Shahidur Rahman
"""

#import numpy as np;

#list declaration
#a_list = []
#b_list = []

#numpy array declaration
#left = np.array([])
#right = np.array([])

#convert the list to numpy array
#a = np.array(a_list)
#b = np.array(b_list)

#call the explorer library
import explorers
import stringRecorder
import pandas
from sqlalchemy import create_engine
import random
from mmh3 import hash128
i=0
#create sql connection
engine = create_engine('mysql+pymysql://root:shahidur_123@localhost:3306/mwt')
#open file and read
f = open(r"D:\Work\MWT\Data\VW_raw\rcv1.train.raw.txt")
try:
    for line in f:
        l=line.split("|")[0]
        r=line.split("|")[1]
        #a_list.append(l)
        #b_list.append(r)
        i=i+1
        print(i)
        
        #random number generator
        epsilon = round(random.random(),3)
        #print('\n'+'mwt : epsilon'+str(epsilon))
        
        #unique key generation
        unique_key =hash128('my string of doom ', seed=1234)
        #print('mwt : unique_key '+str(unique_key))
        
        #number of actions registered
        noOfActions = 3
        #print('mwt : noOfActions : '+str(noOfActions))
        
        ######################################################
        #space for the policy action called
        #to get the actionID for default policy
        policyDecision = 3
        #print('mwt : policyDecision : '+str(policyDecision))
        scores = [1,2,3,4,5,6,7,8,9,10]
        #for j in scores:
        #   print('mwt : scores : '+str(j))
        ######################################################
    
        
        #print('mwt context : '+i)
        callExplorer = explorers.explorers(epsilon,noOfActions,policyDecision,scores)
        storeValues = callExplorer.algoSelection()
        #print('storeValues : '+str(storeValues))
        record = stringRecorder.stringRecorder(r, storeValues['actionID'], storeValues['actionProbability'], unique_key, storeValues['isExplore'], epsilon, noOfActions,policyDecision,storeValues['explorerAlgo'])
        record=record.sewStrings() 
        #print('record : '+str(record))
    
        #read data in data frame
        #print('connection built')
        colList="context,actionID,actionProbability,unique_key,isExplore,epsilon,noOfActions,policyDecision,explorerAlgo".split(',')
        c1=['col1']
        df = pandas.DataFrame(data=record,index=colList)
        df=df.T
        #print("printing panda df here")
        #print(df)
        #push data in sql
        df.to_sql(con=engine, name='stringrecord', if_exists='append',index=False)

    #close the opened file
finally:
    f.close()






























