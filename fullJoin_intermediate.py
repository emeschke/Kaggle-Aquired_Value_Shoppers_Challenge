from mrjob.job import MRJob
'''This code is used to merge the historyANDoffers.csv and the transactions.csv data.
In the mapper, it assigns the key as the conusmerID number, the only bit in
common between the two data files.

In the reducer, it checks the size of the values passed from the map function.
If it is determined to be an offer, it stores it as the offer, otherwise it
stores it as a trainHistory data point.  The it merges the offer with all the
train history data for a given key and outputs it.  The formatting is not ideal.
'''

class MRWordFrequencyCount(MRJob):

    offers = {'1221665': ['1221665', '7205', '1', '103700030', '1.5', '4294'],
              '1200578': ['1200578', '1703', '1', '104460040', '1.5', '7668'],
              '1200579': ['1200579', '1703', '1', '104460040', '1.5', '7668'],
              '1194044': ['1194044', '9909', '1', '107127979', '1', '6732'],
              '1221667': ['1221667', '7205', '1', '103700030', '2', '4294'],
              '1219903': ['1219903', '799', '1', '1076211171', '1.5', '17286'],
              '1219900': ['1219900', '799', '1', '1076211171', '1.5', '17286'],
              '1208329': ['1208329', '2119', '1', '108079383', '1', '6926'],
              '1203439': ['1203439', '5122', '1', '107106878', '1.5', '17311'],
              '1221663': ['1221663', '7205', '1', '103700030', '1.5', '4294'],
              '1208252': ['1208252', '2202', '1', '104460040', '3', '3718'],
              '1204576': ['1204576', '5616', '1', '104610040', '1', '15889'],
              '1204822': ['1204822', '5619', '1', '107717272', '1.5', '102504'],
              '1204821': ['1204821', '5619', '1', '107717272', '1.5', '102504'],
              '1213242': ['1213242', '5824', '1', '105190050', '2', '26456'],
              '1208501': ['1208501', '6202', '1', '1087744888', '1.5', '64486'],
              '1208503': ['1208503', '6202', '1', '1087744888', '1.5', '64486'],
              '1221666': ['1221666', '7205', '1', '103700030', '1.5', '4294'],
              '1208251': ['1208251', '2202', '1', '104460040', '2', '3718'],
              '1197502': ['1197502', '3203', '1', '106414464', '0.75', '13474'],
              '1203052': ['1203052', '9909', '1', '1089520383', '1', '28840'],
              '1230218': ['1230218', '706', '1', '104127141', '1', '26189'],
              '1198275': ['1198275', '5558', '1', '107120272', '1.5', '5072'],
              '1198274': ['1198274', '5558', '1', '107120272', '1.5', '5072'],
              '1198273': ['1198273', '5558', '1', '107120272', '1.5', '5072'],
              '1198272': ['1198272', '5558', '1', '107120272', '1.5', '5072'],
              '1198271': ['1198271', '5558', '1', '107120272', '1.5', '5072'],
              '1190530': ['1190530', '9115', '1', '108500080', '5', '93904'],
              '1200988': ['1200988', '3509', '1', '103320030', '2', '875'],
              '1200581': ['1200581', '1726', '1', '104460040', '1.25', '7668'],
              '1221658': ['1221658', '7205', '2', '103700030', '3', '4294'],
              '1200582': ['1200582', '1726', '1', '104460040', '1.25', '7668'],
              '1200584': ['1200584', '3504', '1', '104460040', '1.25', '7668'],
              '1199258': ['1199258', '4401', '1', '105100050', '2', '13791'],
              '1220503': ['1220503', '4517', '1', '105450050', '1.5', '1322'],
              '1220502': ['1220502', '4517', '1', '105450050', '1.5', '1322'],
              '1199256': ['1199256', '4401', '1', '105100050', '2', '13791']}

    
    def mapper(self, _, line):
	line = line.split(",")
	#If the length of the split line is 11, it is a transaction
	if len(line) == 11:
		line_payload = line[1::] 	
		yield (line[0], line_payload)
	#Otherwise it is a trainHistory data point	
	else: 
		line_payload = line[1::]
		yield (line[0], line_payload)  

    def reducer(self, key, values):
        trans = []
        history = []
        #For all the values associated with the key 
        for val in values:
            #If it is a transaction, append it to transactions.             
            if len(val) == 10:
                trans.append(val)
            #Otherwise it is a train history data point.        
            else:
                history.append(val)
        global offers
        if len(history) > 0:
            #Offer info is a lookup of the offer from the hashtable.
            offer = offers[history[0][1]]
        #If both the trans and history are greater than zero, join        
        if len(trans) > 0 and len(history) > 0:
            for t in trans:
                output = key + str(history[0] + offer + t).strip("[]").replace("'", "")
                yield ("", output)
        #Else, just output the key
        #If this is included, only the yield below "yields", the one above doesn't
        elif len(history) > 0:
            output = key + str(history[0] + offer).strip("[]").replace("'", "")
            yield ("",  output)
            


if __name__ == '__main__':
    MRWordFrequencyCount.run()
