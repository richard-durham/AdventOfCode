''' From www.adventofcode.com
    Day 4 questions
'''
import hashlib
key = "iwrupvqb"


for i in range(10000000):
	this_key = key + str(i)
	response = hashlib.md5(this_key).hexdigest()
	if response[:6] == "000000":
		print "Huzah! The answer is: %d" % i
		break
	else:
		print "This is not the number you are looking for: %d" %i
		print response 


