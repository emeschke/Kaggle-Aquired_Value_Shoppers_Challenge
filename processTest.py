# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:07:46 2014

@author: meschke
"""

#Open the files to read
with open('/home/meschke/Desktop/TesterKaggle/fullJoinAgg_test.csv', 'r') as f:
    body = f.readlines()

#Variables for the counts for the marginal distributions
total = 0
buy = 0
nobuy = 0
repeatProb = 0.4278867102
nonRepeat = 0.2039023598

#Determine the total count and each of the marginals
#Also write to file
with open('/home/meschke/Desktop/TesterKaggle/probSubmit1.csv', 'w') as g:
    g.write("id,repeatProbability\n")    
    for line in body:    
        split_line = line.split(",")
        #print split_line[6].split()        
        item_count = int(split_line[4])        
        output = ""        
        if item_count > 0:
            buy += 1
            output = split_line[0] + "," + str(repeatProb) + "\n"
        elif item_count <= 0:
            nobuy += 1
            output = split_line[0] + "," + str(nonRepeat) + "\n"
        if split_line[0] != 'id':
            g.write(output)
            total += 1
#Print the marginal distributions as a matrix
print total
print str(buy) + "  " + str(nobuy) + "   " + str(buy + nobuy)