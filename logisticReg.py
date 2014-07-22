# -*- coding: utf-8 -*-
"""
Created on Thu May 29 21:32:28 2014

@author: meschke
"""

import pandas as pd
from sklearn import linear_model
from sklearn.svm import SVC
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

#read the data in
df = pd.read_csv('/home/meschke/Desktop/TesterKaggle/AggMoreDataTrain_zeroOne.csv', 
                 header = None, low_memory=False)
df1 = pd.read_csv('/home/meschke/Desktop/TesterKaggle/AggMoreDataTest.csv', 
                 header = None, low_memory=False)

#Get some summary statistics
#print df.head()
#print df.describe() 

#Plot a histogram
#df.hist()
#pl.show()
#print df.columns


#Choose the columns to keep
cols_to_keep_train = [1,2,3,4,5,13]
cols_to_keep_test = [1,2,3,4,5,11]
#cols_to_keep = [5]
inputVals = df[cols_to_keep_train]
#inputVals[5] = 1.0
testVals = df1[cols_to_keep_test]
#testVals[5] = 1.0

testVals[[11]] = testVals[[11]].astype(np.float64)

#This works well, in 265 place with the power as .5
#.25 is doesn't work as well as .5.
#This normalizes the values.
#inputValsNorm = np.power(inputVals,.5)
#testValsNorm = np.power(testVals, .5)

#This normalizes the values.
inputValsNorm = np.log(inputVals + 1)
testValsNorm = np.log(testVals + 1)



#Plot a histogram of the values
#inputValsNorm.hist(xlabelsize = .2)
#plt.show()

#Set the model and fit it.
model = linear_model.LogisticRegression(C=1e5, penalty = 'l1')
model.fit(inputValsNorm, df[8])

#Print coefficents
print model.coef_

#Output gives us our values for the original train set.  
#.60815 non-normalized
#.614630 nomrmalized.
output = model.predict_proba(inputValsNorm)
output1 = model.predict_proba(testValsNorm)

#Plot the output for the first 1000 probabilities
plt.plot(output1[1:1000,1])
plt.plot(output[1:1000,1])
plt.show()
print max(output1[:,1])
print min(output1[:,1])
print sum(output1[:,1])/len(output1[:,1])

# Compute ROC curve and area the curve
fpr, tpr, thresholds = roc_curve(df[8], output[:,1])
roc_auc = auc(fpr, tpr)
print "Area under the ROC curve : %f" % roc_auc

# Plot ROC curve
pl.clf()
pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver operating characteristic example')
pl.legend(loc="lower right")
pl.show()


#Write to the output file.
outputTuple = zip(df1[0], output1[:,1])

with open('/home/meschke/Desktop/TesterKaggle/logSubmissionNormalLogL1.csv', 'w') as f:
    f.write("id,repeatProbability\n")    
    for tup in outputTuple:
        if(tup[0] != 'id'):
            f.write(str(tup[0]) + "," + str(tup[1]) + "\n")
            
            