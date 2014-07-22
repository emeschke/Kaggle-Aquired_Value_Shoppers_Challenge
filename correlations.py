# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:07:46 2014

@author: meschke
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr

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
    
#Change all to ints rather than strings.    
dataList = [[float(j) for j in i] for i in dataList]   

lists = np.array(dataList)

#Sample output for lists:
#[498084392         1        12         5         1         0         0]

x = lists[0:1000,1]
y = lists[0:1000,2] 

print pearsonr(lists[:,1], lists[:,7])