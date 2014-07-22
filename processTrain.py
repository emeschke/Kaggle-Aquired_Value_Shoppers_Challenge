# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/meschke/.spyder2/.temp.py
"""

#Open the files to read
with open('/home/meschke/Desktop/TesterKaggle/fullJoinAgg.csv', 'r') as f:
    body = f.readlines()

#Variables for the counts for the marginal distributions
total = 0
buy_repeat = 0
nobuy_repeat = 0
buy_norepeat = 0
nobuy_norepeat = 0

#Determine the total count and each of the marginals
for line in body:
    total += 1    
    split_line = line.split(",")
    #print split_line[6].split()    
    boolTF = split_line[6].strip()    
    item_count = int(split_line[4])        
    if boolTF == 't' and item_count > 0:
        buy_repeat += 1
    elif boolTF == 't' and item_count <= 0:
        nobuy_repeat += 1
    elif boolTF == 'f' and item_count > 0:
        buy_norepeat += 1
    elif boolTF == 'f' and item_count <= 0:
        nobuy_norepeat += 1
    else:
        print "Error"
        print split_line

#Print the marginal distributions as a matrix
print str(buy_repeat) + "  " + str(nobuy_repeat) + "   " + str(buy_repeat + nobuy_repeat)
print str(buy_norepeat) + "   " + str(nobuy_norepeat) + "   " + str(buy_norepeat + nobuy_norepeat)
print str(buy_repeat + buy_norepeat) + "   " + str(nobuy_repeat + nobuy_norepeat) + "   " + str(buy_repeat + nobuy_repeat + buy_norepeat + nobuy_norepeat)