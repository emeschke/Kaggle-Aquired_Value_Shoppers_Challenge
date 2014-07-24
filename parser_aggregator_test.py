import sys
from sets import Set
import time
#To use:
#$ cat transactions1.csv | python parser_aggregator.py
#Stored in directory data/fullJoinAgg.csv

starttime = time.clock()
# input comes from STDIN
#Dictionaries to store the trainHistIDs, the lists of transactions
#that correspond with the train history ids, and the offers.
trainHistId = {}
transactions = {}
offers = {}

#Read in trainHistory and assign to dict with ID as the key
with open("testHistory.csv", "r") as f:
    read_data = f.readlines()

for line in read_data:
    split_line = line.split(",")
    trainHistId[split_line[0]] = line
    #6 spots to count category, company, brand, all three, repeats, and t/f
    transactions[split_line[0]] = [0,0,0,0]

#Read in offers and assign to a dict with offer as the key
with open("offers.csv", "r") as g:
    offer_data = g.readlines()

for line in offer_data:
    split_line = line.split(",")
    offers[split_line[0]] = line


for line in sys.stdin:
    #Get the current line by stripping the input.
    thisTrans = line.strip().split(",")
    #If the transaction is in the ID number list, get the list.
    if thisTrans[0] in transactions:
        thisHistid = trainHistId.get(thisTrans[0]).strip().split(",")
        #If the 2nd part of the histID is in offers, get the offer.
        if thisHistid[2] in offers:
            thisOffer = offers.get(thisHistid[2]).strip().split(",")
            #If the offer characteristics all match, they bought the exact
            #product in the past, this is 
            if (thisTrans[3] == thisOffer[1] and thisTrans[4] == thisOffer[3]
                and thisTrans[5] == thisOffer[5]):
                transactions[thisTrans[0]][3] += 1
            #Aggregate category
            if thisTrans[3] == thisOffer[1]:
                transactions[thisTrans[0]][0] += 1 
            #Aggregate company
            if thisTrans[4] == thisOffer[3]:
                transactions[thisTrans[0]][1] += 1
            #Aggregate brand
            if thisTrans[5] == thisOffer[5]:
                transactions[thisTrans[0]][2] += 1 

with open('data/fullJoinAgg_test.csv', 'w') as f:
    for key in transactions:
        value = transactions[key]
        f.write(str(key) + "," + str(value[0]) + "," + str(value[1]) +
                "," + str(value[2]) + "," + str(value[3]) + "," + "\n")
                
print "This took " + str(time.clock()-starttime) + " minutes."
