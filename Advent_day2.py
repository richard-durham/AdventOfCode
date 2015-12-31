''' From www.adventofcode.com
    Day 2 questions
'''

with open('day2.txt', 'r') as input_packages:
    list_of_packages = input_packages.readlines()

print len(list_of_packages)

def make_package_usable(package):
	''' split the package into seperate dimensions, convert them to int, and sort
	'''
	dimensions = package.split('x')
	int_dimensions = (int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
	sorted_package_dimensions = sorted(int_dimensions)
	return sorted_package_dimensions

def wrapping_paper(dimensions):
	''' calculate amount of wrapping paper needed 
		assumes sorted dimensions as input
	'''
	length = dimensions[0]
	width = dimensions[1]
	height = dimensions[2]

	dim1 =  2 * length * width
	dim2 = 2 * length * height
	dim3 = 2 * width * height
	extra = length * width  # assumes dimensions are sorted so height is the largest measure
	return dim1 + dim2 + dim3 + extra

def ribbon(dimensions):
	''' calculate amount of ribbon needed 
	'''
	length = dimensions[0]
	width = dimensions[1]
	height = dimensions[2]

	ribbon_only = length + length + width + width
	bow = length * width * height

	return ribbon_only + bow

paper_needed = 0
ribbon_needed = 0
for package in list_of_packages:
	dimensions = make_package_usable(package)

	paper_needed += wrapping_paper(dimensions)
	ribbon_needed += ribbon(dimensions)

print "Wrapping paper needed: %d" % paper_needed
print "and this much ribbon: %d" % ribbon_needed

