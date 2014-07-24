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

    def mapper(self, _, line):
        line = line.split(",")
        print len(line)
        #If the length of the split line is 11, it is a transaction.
        #Id is in the 4th column (with zero ordering)
        if len(line) == 11:
            line_payload = line[1::]                    
            key = str(line[0].strip())
            print "trans" + str(len(key))
            yield (key, line_payload)
        #Otherwise it is a data point for the Train/History set.
        #Id is in the second column    
        elif len(line) == 7: 
            line_payload = line[1::]        
            key = str(line[0].strip())
            print "th" + str((key))
            yield (key, line_payload)     

    def reducer(self, key, values):
        #print key + str(values)
        trans = []
        couponUser = []
        #For all the values associated with the key 
        for val in values:
            #If it is an offer, append it to the offer              
            if len(val) == 10:
                trans.append(val)
            #Otherwise it is a train history data point.        
            else:
                couponUser.append(val)
        #There can only be one coupon user for this key.    
        thisCouponUser = couponUser
        #print str(len(trans)) + "***" + str(len(couponUser))
        #If there are no transactions associated with a coupon redeemer.        
        if len(trans) == 0:
            pass
            #yield ("", key + str(couponUser))   
        #Otherwise, output the joined string if the product/brand/company match     
        elif len(couponUser) == 0: 
            pass
        else:   
            print "*************************" + str(thisCouponUser)
            for t in trans:
                #if thisCouponUser[6] == t[2] or thisCouponUser[8] == t[3] or thisCouponUser[10] == t[4]:
                    output = "***" + str(key) + str(thisCouponUser) + str(t)       
                    #print str(thisCouponUser) + "***" + str(trans)
                    yield("", output)
        #yield (len(trans), len(couponUser))


if __name__ == '__main__':
    MRWordFrequencyCount.run()
