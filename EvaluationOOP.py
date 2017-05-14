#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:08:06 2017

@author: Mengru Ding, Zhanruo Qu, Helen Vernon
"""

class Emotion:
    def __init__(self ,list_gold, list_prediction, emotion):
        self.emotion = emotion
        self.tp = 0
        self.tn = 0
        self.fp = 0
        self.fn = 0
        self.accuracy = 0
        self.precision = 0
        self.recall = 0
        self.F1 = 0
        self.list_gold = list_gold
        self.list_prediction = list_prediction
        
    def evaluation(self):
        for i in range(len(self.list_gold)):
            if self.list_gold[i] == self.list_prediction[i] and self.list_gold[i] == self.emotion:
                self.tp += 1
            elif list_prediction[i] == self.emotion and list_gold[i] != self.emotion:
                self.fp += 1
            elif list_gold[i] == self.emotion and list_prediction[i] != self.emotion:
                self.fn += 1
            else:
                self.tn += 1
                
        self.accuracy = (self.tp + self.tn) / (self.tp + self.tn + self.fp + self.fn) * 100
        self.precision = self.tp /(self.tp + self.fp) * 100
        self.recall = self.tp / (self.tp + self.fn) * 100
        self.F1 = 2 * self.precision * self.recall / (self.precision + self.recall)
        
    def print_result(self):
        print ("| {0:8} | {1:9.2f} | {2:6.2f} | {3:8.2f} | {4:8.2f} |".format( self.emotion, self.precision, self.recall, self.accuracy, self.F1))

fileg = open('dev-gold.csv')
filep = open('dev-predicted.csv')
lineg = fileg.readline()
linep = filep.readline()
list_gold = []
list_prediction = []
while lineg:
    list_gold.append(lineg.strip())
    list_prediction.append(linep.strip())
    lineg = fileg.readline()
    linep = filep.readline()

print ("=" * 55+"\n|   Label  | Precision | Recall | Accuracy | F1-Score |\n" + "=" * 55)

for e in set(list_gold):
    emo = Emotion(list_gold, list_prediction, e)
    emo.evaluation()
    emo.print_result()

print ('=' * 55)