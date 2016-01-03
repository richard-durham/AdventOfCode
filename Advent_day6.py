#!/usr/bin/python

'''Advent of Code - day 6 
'''

import re
import numpy as np 

grid_size = 1000

with open('day6.txt', 'r') as raw_instructions:
	list_of_instructions = raw_instructions.readlines()

light_grid = [[0 for x in range(grid_size)] for x in range(grid_size)]

'''
for testing
'''
test_lines = ("turn on 489,959 through 759,964", "turn off 820,516 through 871,914", "toggle 120,314 through 745,489")
test_lines1 = ("turn on 0,0 through 3,4", "turn off 1,0 through 1,4", "toggle 1,3 through 4,4")


def translate_instructions(instructions):
	key_data = re.match(r"([^0-9]+)([0-9]+).([0-9]+)[^0-9]+([0-9]+).([0-9]+)", instructions)

	return key_data.group(1), key_data.group(2,3), key_data.group(4,5)


def decide_action(instruct_group):
	if  instruct_group[0] == "turn on ":
		return "On"
	elif instruct_group[0] == "turn off ":
		return "Off"
	elif instruct_group[0] == "toggle ":
		return "Toggle"
	else:
		return "hinky stuff going on - try again"


def turn_on(start, end):
	''' turn on grid coordinates
	'''
	start_x = int(start[0])
	start_y = int(start[1])
	end_x = int(end[0])
	end_y = int(end[1])

	for row in range(start_x, end_x + 1):
		for column in range(start_y, end_y + 1):
			light_grid[row][column] = 1


def turn_off(start, end):
	'''turn off grid coordinates
	'''
	start_x = int(start[0])
	start_y = int(start[1])
	end_x = int(end[0])
	end_y = int(end[1])

	for row in range(start_x, end_x + 1):
		for column in range(start_y, end_y + 1):
			light_grid[row][column] = 0
			#print row, column, "set to: ", light_grid[row][column]


def toggle(start, end):
	'''if off turn on, else turn off
	'''
	start_x = int(start[0])
	start_y = int(start[1])
	end_x = int(end[0])
	end_y = int(end[1])

	for row in range(start_x, end_x + 1):
		for column in range(start_y, end_y + 1):
			if light_grid[row][column] == 0:
				light_grid[row][column] = 1
			else:
				light_grid[row][column] = 0
			#print row, column, "set to: ", light_grid[row][column]


def print_lights():
	for i in range(grid_size):
		print light_grid[i]

def count_lights():
	count = 0
	for row in light_grid:
		count += row.count(1)
	return count



'''
all_instructions = translate_instructions(test_line0)
action =  decide_action(all_instructions)
start = all_instructions[1]
end = all_instructions[2]

print action
print start
print end

for i in range(5):
	print light_grid[i]

if action == "On":
	turn_on(start,end)
elif action == "Off":
	turn_off(start,end)
elif action == "Toggle":
	toggle(start,end)
else:
	print "Houston we have a problem!"


print "Result"
for j in range(5):
	print light_grid[j]
'''


for instruction in list_of_instructions:
	#print decide_action(translate_instructions(instruction))
	all_instructions = translate_instructions(instruction)
	action =  decide_action(all_instructions)
	start = all_instructions[1]
	end = all_instructions[2]

	print "Action to take: %s" % action
	print "Start at: ", int(start[0]), int(start[1]), " Stop at:", int(end[0]), int(end[1])


	if action == "On":
		turn_on(start,end)
		#print_lights()
	elif action == "Off":
		turn_off(start,end)
		#print_lights()
	elif action == "Toggle":
		toggle(start,end)
		#print_lights()
	else:
		print "Houston we have a problem!"

print "# of lights on: ", count_lights()



