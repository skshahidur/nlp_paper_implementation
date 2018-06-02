# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:16:36 2016

@author: Shahidur Rahman
"""
from random import randint
import random
import math

#calling the library and deciding the explorer to work with
class explorers(object):
    def __init__(self,epsilon,noOfActions,policyDecision,scores):
        #print('explorer : constructor gettig called')
        self.epsilon = epsilon
        self.noOfActions = noOfActions
        self.policyDecision = policyDecision
        self.scores = scores
    def algoSelection(self):
        rand = round(random.random(),3)
        #print('explorers : inside explorers and random number generated is : '+str(rand))
        a = explorers(self.epsilon,self.noOfActions,self.policyDecision,self.scores)
        if(rand>=.000 and rand <=1.000):
            #print('explorers : epsilonGreedyMethod called')
            return a.epsilonGreedyMethod()
        if(rand>1.300 and rand <=1.600):
            #print('explorers : softMax called')
            return a.softMaxMethod()            
        if(rand>=2.600 and rand<=11.000):
            #print('explorers : generic called')
            return a.genericMethod()
         
#epsilonGreedy
#class epsilonGreedy(object):
#    def __init__(self,epsilon,noOfActions,policyDecision):
#       
#       self.epsilon = epsilon
#      self.noOfActions = noOfActions
#     self.policyDecision = policyDecision
        
    def epsilonGreedyMethod(self):
        
        global baseProb 
        baseProb = round(self.epsilon/self.noOfActions,2)
        global actionProbability
        isExplore = 0
        explorerAlgo = 'epsilonGreedy'
        
        if (self.epsilon<0 or self.epsilon>1):
            print("explorers : Epsilon should be between 0 and 1")
        if(self.policyDecision<0 or (self.noOfActions-1)<self.policyDecision):
            print("explorers : Wrong selection by policyDecision")
        else:
            if(self.epsilon<.800):
                actionProbability = 1-self.epsilon+baseProb
                actionID = self.policyDecision
                isExplore = 0
            else:
                actionID = randint(0,self.noOfActions)
                if(actionID == self.policyDecision):
                    actionProbability = 1-self.epsilon+baseProb
                else:
                    actionProbability = baseProb
                isExplore = 1
        #print('actionProbability : '+str(actionProbability)+
         #       ' actionID : '+str(actionID)+
          #      ' isExplore : '+str(isExplore))
        return {'actionProbability' : actionProbability,
                'actionID' : actionID,
                'isExplore' : isExplore,
                'explorerAlgo' : explorerAlgo
                }
        
#softMax
#class softMax(object):
#    def __init__(self,_lambda,noOfActions,policyDecision, scores):
#        self._lambda = _lambda
#       self.noOfActions = noOfActions
#        self.policyDecision = policyDecision
#        self.scores = scores

    def softMaxMethod(self):
        if (self.epsilon<0 or self.epsilon>1):
            print("explorers : Epsilon should be between 0 and 1")
        if(self.policyDecision<0 or (self.noOfActions-1)<self.policyDecision):
            print("explorers : Wrong selection by policyDecision")
        else:
            explorerAlgo = 'softMax'
            isExplore = 0
            numScores = len(self.scores)
            #print('explorer softMax numScores : '+str(numScores))
            if(self.noOfActions != numScores):
                print("explorers : The number of scores returned by the scorer must equal number of actions")
            i = 0
            maxScore = max(self.scores)
            maxIndex = self.scores.index(maxScore)
            actionProbability = 0
            actionID = 0
            if(self.epsilon>.2):
                isExplore = 1
                for i in range(0,numScores):
                    #print('softmax method i : '+str(i))
                    self.scores[i] = math.exp(self.epsilon * (self.scores[i] - maxScore))
                total = sum(self.scores)
                draw = random.random()
                #print('softmax draw : '+str(draw))
                sumScore = 0
                actionID = numScores - 1
                for i in range(0,numScores):
                    self.scores[i] = self.scores[i]/total
                    sumScore +=self.scores[i]
                    if (sumScore > draw):
                        actionID = i
                        actionProbability = self.scores[i]
                        break
            else:
                 maxScore = max(self.scores)
                 actionID = maxIndex
                 isExplore = 0
                 actionProbability = 1
                 
            #print('actionProbability : '+str(actionProbability)+
             #   ' actionID : '+str(actionID)+
              #  ' isExplore : '+str(isExplore))
            return {'actionProbability' : actionProbability,
                'actionID' : actionID,
                'isExplore' : isExplore,
                'explorerAlgo' : explorerAlgo
                }

#Generic
#class generic(object):
#    #constructor    
#    def __init__(self,_lambda,noOfActions,policyDecision, scores):
#        self._lambda = _lambda
#        self.noOfActions = noOfActions
#        self.policyDecision = policyDecision
#        self.scores = scores
    #methods

    def genericMethod(self):
        if (self.epsilon<0 or self.epsilon>1):
            print("explorers : Epsilon should be between 0 and 1")
        if(self.policyDecision<0 or (self.noOfActions-1)<self.policyDecision):
            print("explorers : Wrong selection by policyDecision")
        else:
            explorerAlgo = 'generic'
            numScores = len(self.scores)
            if(self.noOfActions != numScores):
                print("explorers : The number of scores returned by the scorer must equal number of actions")
            i = 0
            maxScore = max(self.scores)
            maxIndex = self.scores.index(maxScore)
            actionProbability = 0
            actionID = 0
            isExplore = 0
            #how should I check the exlploration chance
            #if(self.epsilon>.2):
            if(self.epsilon>.2):
                #for i in numScores:
                    #self.scores[i] = math.exp(self._lambda * (self.scores[i] - maxScore))
                total = sum(self.scores)
                draw = random.random()
                #print('generic draw : '+str(draw))
                sumScore = 0
                actionProbability = 0
                actionID = numScores - 1
                isExplore = 1
                for i in range(0,(numScores)):
                    #print('generic method i : '+str(i))
                    self.scores[i] = self.scores[i]/total
                    sumScore +=self.scores[i]
                    if (sumScore > draw):
                        actionID = i
                        actionProbability = self.scores[i]
                        break
            else:
                 maxScore = max(self.scores)
                 actionID = maxIndex
                 isExplore = 0
                 total1 = sum(self.scores)
                 actionProbability=maxScore/total1
            
            #print('actionProbability : '+str(actionProbability)+
             #   ' actionID : '+str(actionID)+
              #  ' isExplore : '+str(isExplore))
            return {'actionProbability' : actionProbability,
                'actionID' : actionID,
                'isExplore' : isExplore,
                'explorerAlgo' : explorerAlgo
                }
                
                
                