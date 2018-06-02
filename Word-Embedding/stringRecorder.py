# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:39:38 2016

@author: Shahidur Rahman
"""

#stringRecorder
class stringRecorder(object):
    def __init__(self,context, actionID, actionProbability, unique_key, isExplore, epsilon,
                 noOfActions,policyDecision, explorerAlgo, rewardValue):
        self.context = context
        self.actionID = actionID
        self.actionProbability = actionProbability
        self.unique_key = unique_key
        self.isExplore = isExplore
        self.epsilon = epsilon
        self.noOfActions = noOfActions
        self.policyDecision = policyDecision
        self.explorerAlgo = explorerAlgo
        self.rewardValue = rewardValue
        
    def sewStrings(self):
        stringRecord = []
        stringRecord.append(self.context)
        stringRecord.append(self.actionID)
        stringRecord.append(self.actionProbability)
        stringRecord.append(self.unique_key)
        stringRecord.append(self.isExplore)
        stringRecord.append(self.epsilon)
        stringRecord.append(self.noOfActions)
        stringRecord.append(self.policyDecision)
        stringRecord.append(self.explorerAlgo)
        stringRecord.append(self.rewardValue)
        
        return stringRecord
        
    
    
