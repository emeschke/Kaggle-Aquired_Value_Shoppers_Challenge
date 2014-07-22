# -*- coding: utf-8 -*-
"""
Created on Thu May 29 21:41:46 2014

@author: meschke
"""
import csv

#Open the files to read
with open('/home/meschke/Desktop/TesterKaggle/AggMoreDataTrain.csv', 'r') as f:
    body = f.readlines()

dataList = []

#Read in and change t/f to 1/0
for line in body:
    new_list = line.strip().split(",")
    if(new_list[8] == 'f'):
        new_list[8] = 0
        dataList.append(new_list)
    elif(new_list[8]) == 't':
        new_list[8] = 1
        dataList.append(new_list)
    else:
        pass
    
with open('/home/meschke/Desktop/TesterKaggle/AggMoreDataTrain_zeroOne.csv', 'w') as f:
    wr = csv.writer(f)
    wr.writerows(dataList)