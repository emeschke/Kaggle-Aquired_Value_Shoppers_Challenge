from mrjob.job import MRJob
from sets import Set

'''To filter the transactions, it is a map/reduce on only the transactions file.
Map the transaction with the userID (this is arbitrary, the key doesn't matter)
if the category/company/brand is a valid one for the offer.  Reduce passes 
straight through.'''

category = Set(["706","799", "1703", "1726", "2119", "2202", "3203", "3504",
                "3509", "4401", "4517", "5122", "5558", "5616", "5619", "5824",
                "6202", "7205", "9115", "9909"])
company = Set(["103320030", "103700030", "104127141", "104460040","104610040",
               "105100050", "105190050", "105450050", "106414464", "107106878",
               "107120272", "107127979", "107717272", "108079383", "108500080",
               "1076211171", "1087744888", "1089520383"])
brand = Set(["875", "1322", "3718", "4294", "5072", "6732", "6926", "7668",
             "13474", "13791", "15889", "17286", "17311", "26189", "26456",
             "28840", "64486", "93904", "102504"])

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
	line = line.split(",")
	#If it is in the category/company/brand keep it.
	if line[3] in category or line[4] in company or line[5] in brand:	
		yield (line[0], line[1::])     

    def reducer(self, key, values):
	#For all the values associated with the key	
	for val in values:		
                output = ",".join(val)	
		output = key + "," + output		
		yield("", output)
			
		


if __name__ == '__main__':
    MRWordFrequencyCount.run()
