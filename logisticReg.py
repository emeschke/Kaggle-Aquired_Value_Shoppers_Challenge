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

#read the data in
df = pd.read_csv('/home/meschke/Desktop/TesterKaggle/fullJoinAgg_zeroOne.csv', header = None)
df1 = pd.read_csv('/home/meschke/Desktop/TesterKaggle/fullJoinAgg_test.csv', header = None)

#Get some summary statistics
#print df.head()
#print df.describe() 

#Plot a histogram
#df.hist()
#pl.show()
#print df.columns

#Choose the columns to keep
cols_to_keep = [1,2,3,4]
#cols_to_keep = [4]
inputVals = df[cols_to_keep]
inputVals[5] = 1.0
testVals = df1[cols_to_keep]
testVals[5] = 1.0

#This works well, in 265 place with the power as .5
#.25 is doesn't work as well as .5.
#This normalizes the values.
inputValsNorm = np.power(inputVals,.5)
testValsNorm = np.power(testVals, .5)

#inputValsNorm.describe()

#Plot a histogram of the values
#inputValsNorm.hist(xlabelsize = .2)
#plt.show()

#Set the model and fit it.
model = linear_model.LogisticRegression(C=1e5)
model.fit(inputVals, df[6])

#Print coefficents
print model.coef_

#Output gives us our values for the original train set.  
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
fpr, tpr, thresholds = roc_curve(df[6], output[:,1])
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

with open('/home/meschke/Desktop/TesterKaggle/logSubmission.csv', 'w') as f:
    f.write("id,repeatProbability\n")    
    for tup in outputTuple:
        if(tup[0] != 'id'):
            f.write(str(tup[0]) + "," + str(tup[1]) + "\n")