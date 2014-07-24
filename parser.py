import sys
from sets import Set
import time

# input comes from STDIN
#Dictionaries to store the trainHistIDs, the lists of transactions
#that correspond with the train history ids, and the offers.
trainHistId = {}
transactions = {}
offers = {}

#starttime = time.clock()

#Read in trainHistory and assign to dict with ID as the key
with open("testHistory.csv", "r") as f:
    read_data = f.readlines()

for line in read_data:
    split_line = line.split(",")
    trainHistId[split_line[0]] = line
    transactions[split_line[0]] = []

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
            if (thisTrans[3] == thisOffer[1] or thisTrans[4] == thisOffer[3]
                or thisTrans[5] == thisOffer[5]):
                print (str(thisTrans).strip('[]') + "," + str(thisHistid).strip('[]')
                + "," + str(thisOffer).strip('[]'))
                
#print "This took " + str(time.clock()-starttime) + " minutes."
