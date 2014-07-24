from mrjob.job import MRJob
#To filter the file and export the from the user file the amount of times
#the user id purchased the category, company, brand, and product and how
#many times the user was a repeat customer, the boolean for repeat customer,
#and(cat/comp/brand)
#This is a list--[category, company, brand, union, count repeat, bool repeat]

#Checking to see whether category/company/brand is equal is done within the
#mapper task.  

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
	line = line.split(",")
        #The key is the userID
	key = line[0]
	product = 0
	category = 0
	company = 0
	brand = 0
        #Check if category, company and brand are equal between the offer/trans
	#This represents an identical product.
	if (line[3] == line[19] and line[4] == line[21] and line[5] == line[23]):
            product = 1
        #Check if category is equal
        if line[3] == line[19]:
            category = 1
        #Check if the company is equal
        if line[4] == line[21]:
            company = 1
        #Check if the brand is equal
        if line[5] == line[23]:
            brand = 1
        #Set those characteristics as the tuple and output it
        value = [category, company, brand, product, line[15], line[16]]
        yield (key, value)

    def reducer(self, key, values):
        agg_list = [0,0,0,0]
        count_repeat = 0
        bool_repeat = ""
        #Aggregate the count for the user
	for val in values:
	    agg_list[0] += val[0]
	    agg_list[1] += val[1]
	    agg_list[2] += val[2]
	    agg_list[3] += val[3]
	    #Set the values for count and repeat.  These are the same across all.
	    count_repeat = val[4]
            bool_repeat = val[5]
        #Format the output and output
        output = (str(count_repeat) + "," + str(bool_repeat) + "," + str(agg_list[0]) +
                  "," + str(agg_list[1]) + "," + str(agg_list[2]) + "," +
                  str(agg_list[3]))
	yield(key, output)
			
		


if __name__ == '__main__':
    MRWordFrequencyCount.run()
