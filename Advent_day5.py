''' From www.adventofcode.com
    Day 5 questions
'''

import re

with open('day5.txt', 'r') as input_words:
    list_of_words = input_words.readlines()

nice_words = 0
naughty_words = 0
count = 0
vowls = 0
letters_2x = 0
naughty_letters = 0


def illegal_letters(word):
	if 'ab' in word or 'cd' in word or 'pq' in word or 'xy' in word:
		return True
	else:
		return False

def double_letters(word):
	for i in range(0, len(word) - 1):
		if word[i] == word[i + 1]:
			return True
	else:
		return False

def three_vowls(word):
	vowls_count = 0
	for char in word:
		if char in 'aeiou':
			vowls_count += 1
	return vowls_count

for word in list_of_words:
	if illegal_letters(word) == True:
		continue

	if three_vowls(word) < 3:
		continue

	if double_letters(word) == True:
		nice_words += 1

print "Nice words: %d" %nice_words

