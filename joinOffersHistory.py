from mrjob.job import MRJob
'''This code is used to merge the offer data with the trainHistory data.
In the mapper, it assigns the key as the offer number, the only bit in
common between the two data files.
In the reducer, it checks the size of the values passed from the map function.
If it is determined to be an offer, it stores it as the offer, otherwise it
stores it as a trainHistory data point.  The it merges the offer with all the
train history data for a given key and outputs it.  The formatting is not ideal.
'''

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
	line = line.split(",")
	#If the length of the split line is 6, it is an offer
	if len(line) == 6:
		line_payload = line[1::] 	
		yield (line[0], line_payload)
	#Otherwise it is a trainHistory data point	
	else: 
		line_payload = line[0:2] + line[3::]
		yield (line[2], line_payload)     
	
    def reducer(self, key, values):
	offer = []
	history = []
	#For all the values associated with the key	
	for val in values:
		#If it is an offer, append it to the offer		
		if len(val) == 5:
			offer.append(val)
		#Otherwise it is a train history data point.		
		else:
			history.append(val)
	for h in history:
		#Yield the train history + the associated offer.
		output = h + offer[0]
                output = ",".join(output)	
		output = key + "," + output	
		yield("", output)
			
		


if __name__ == '__main__':
    MRWordFrequencyCount.run()
