# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 15:31:30 2014

@author: meschke
"""
import pandas as pd
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

#read the data in
df = pd.read_csv('/home/meschke/Desktop/TesterKaggle/fullJoinAgg_zeroOne.csv', header = None)
df1 = pd.read_csv('/home/meschke/Desktop/TesterKaggle/fullJoinAgg_test.csv', header = None)

#Choose the columns to keep
cols_to_keep = [1,2,3,4]
#cols_to_keep = [4]
inputVals = df[cols_to_keep]
#inputVals[5] = 1.0
testVals = df1[cols_to_keep]
#testVals[5] = 1.0

#Normalize the inputs by the log
inputValsNorm = np.log(inputVals + 1)
testValsNorm = np.log(testVals + 1)

clf = AdaBoostClassifier(n_estimators=25)
clf.fit(inputVals, df[6])

#Normalized output gets .539292 in AUC Roc
#Non-normalized gets .560582
output = clf.predict_proba(inputVals)
output1 = clf.predict_proba(testVals)



print output[1:15]

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

with open('/home/meschke/Desktop/TesterKaggle/ADASubmission.csv', 'w') as f:
    f.write("id,repeatProbability\n")    
    for tup in outputTuple:
        if(tup[0] != 'id'):
            f.write(str(tup[0]) + "," + str(tup[1]) + "\n")