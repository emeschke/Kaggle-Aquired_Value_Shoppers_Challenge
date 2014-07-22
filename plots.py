# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:07:46 2014

@author: meschke
"""
import numpy as np
import matplotlib.pyplot as plt

#Open the files to read
with open('/home/meschke/Desktop/TesterKaggle/fullJoinAgg.csv', 'r') as f:
    body = f.readlines()

dataList = []

#Read in and change t/f to 1/0
for line in body:
    new_list = line.strip().split(",")
    if(new_list[6] == 'f'):
        new_list[6] = 0
        dataList.append(new_list)
    elif(new_list[6]) == 't':
        new_list[6] = 1
        dataList.append(new_list)
    else:
        pass
    
#Change all to ints rather than strings.    
dataList = [[int(j) for j in i] for i in dataList]   

lists = np.array(dataList)

print lists[0]

x = lists[0:1000,4]
y = lists[0:1000,6] 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x, y)
plt.show()
