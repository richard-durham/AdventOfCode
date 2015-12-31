# Advent of Code - day 5 - question 2

import re

with open('day5.txt', 'r') as input_words:
    list_of_words = input_words.readlines()

nice_words = 0

def repeat_letter(word):
	match = re.findall(r"(.).\1", word)
	if len(match) > 0:
		return True
	else:
		return False

def twin_pairs(word):
	match = re.findall(r"(..).*\1", word)
	if len(match) > 0:
		return True
	else:
		return False

count = sum(
		1 for word in list_of_words
		if repeat_letter(word) == True
		and twin_pairs(word) == True
		)

print count


