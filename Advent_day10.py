#!/usr/bin/python

'''Advent of Code - day 10 
'''

from itertools import groupby

input_string = "111312213"
input_list = [1,1,1,3,1,2,2,1,1,3]
current_list = input_list
next_list = []
answer = ''

def look(current_list):
	''' determine run of same number
	'''
	breakdown = [(len(list(number)),count) for count, number in groupby(current_list)]

	return breakdown


def say(next_list):
	''' enter count and number of run
	'''
	new_list = []
	for combo in next_list:
		for item in  combo:
			new_list.append(item)

	return new_list


#now for the time consuming part
for turn in range(40):
	next_list = say(look(current_list))
	current_list = next_list

	print "Turn: ", turn + 1
	print len(next_list)




