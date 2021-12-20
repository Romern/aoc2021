import math
from parse import parse
import itertools
from collections import Counter

def parse_input(inputdata):
	image_enhancement_algorithm, input_image = inputdata.rstrip().split("\n\n")
	return image_enhancement_algorithm, input_image.split("\n")

def solve(data, runs):
	image_enhancement_algorithm, input_image = data
	padding = runs*2

	# pad image
	cur_image = []
	for i in range(padding):
		cur_image.append(["." for i in range(padding*2+(len(input_image[0])))])
	for row in input_image:
		new_row = ["." for i in range(padding)] + list(row) + ["." for i in range(padding)]
		cur_image.append(new_row)
	for i in range(padding):
		cur_image.append(["." for i in range(padding*2+(len(input_image[0])))])

	# apply kernel
	for run in range(runs):
		cur_image_copy = [list(row) for row in cur_image]
		for j in range(1,len(cur_image)-1):
			for i in range(1,len(cur_image[0])-1):
				row1 = cur_image_copy[j-1][i-1:i+2]
				row2 = cur_image_copy[j][i-1:i+2]
				row3 = cur_image_copy[j+1][i-1:i+2]
				algo_input = int("".join("0" if c == "." else "1" for c in row1+row2+row3),2)
				cur_image[j][i] = image_enhancement_algorithm[algo_input]
#	print("\n".join("".join(row[runs*2:-runs*2]) for row in cur_image[runs*2:-runs*2]))
	return sum(c == "#" for row in cur_image[runs:-runs] for c in row[runs:-runs])

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	infile = sys.argv[1]
	data = parse_input(open(infile,"r").read())
	print(solve(data,2))
	print(solve(data,50))
