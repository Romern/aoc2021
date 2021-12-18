import math
import json

def four_nested_pair(inline):
	open = 0
	i = 0
	l = inline
	while i < len(l):
		v = l[i]
		if open == 5:
			begin = i
			# we can apparently assume, that at this level only regular numbers are here
			explode_length = 1
			if l[i+1].isnumeric(): # number > 9 has 2 digits
				left = int(l[i:i+2])
				i += 3 # skip comma
				explode_length += 3
			else:
				left = int(l[i])
				i += 2 # skip comma
				explode_length += 2
			if l[i+1].isnumeric(): # number > 9 has 2 digits
				right = int(l[i:i+2])
				i += 2
				explode_length += 2
			else:
				right = int(l[i])
				i += 1
				explode_length += 1

			# get first left and right natural numbers
			left_add_pos = next((begin-j-1 for j,c in enumerate(l[:begin][::-1]) if c.isnumeric()),None)
			right_add_pos = next((i+j for j,c in enumerate(l[i:]) if c.isnumeric()),None)


			# add to left and right number
			newl = l[:begin-1]
			if left_add_pos:
				if l[left_add_pos-1].isnumeric(): # number > 9 has 2 digits
					newleft = int(l[left_add_pos-1:left_add_pos+1]) + left
					newl = l[:left_add_pos-1] + str(newleft) + l[left_add_pos+1:begin-1]
				else:
					newleft = int(l[left_add_pos]) + left
					newl = l[:left_add_pos] + str(newleft) + l[left_add_pos+1:begin-1]

			if right_add_pos:
				if l[right_add_pos+1].isnumeric(): # number > 9 has 2 digits
					newright = int(l[right_add_pos:right_add_pos+2]) + right
					newl += "0" + l[begin+explode_length:right_add_pos] + str(newright) + l[right_add_pos+2:]
				else:
					newright = int(l[right_add_pos]) + right
					newl += "0" + l[begin+explode_length:right_add_pos] + str(newright) + l[right_add_pos+1:]
			else:
				newl += "0" + l[begin+explode_length:]
			return newl
		if v == "[":
			open += 1
		elif v == "]":
			open -= 1
		i += 1
	return inline

def split_ten_or_greater(inline):
	res = next(((i,i+2) for i in range(len(inline)-1) if inline[i:i+2].isnumeric()),None)
	if res:
		num = int(inline[res[0]:res[1]])
		return inline[:res[0]] + f"[{math.floor(num/2)},{math.ceil(num/2)}]" + inline[res[1]:]
	return inline

def magnitude(line):
	if isinstance(line,int):
		return line
	return 3*magnitude(line[0])+2*magnitude(line[1])

def add_snailfish(s1,s2):
	begin_cur = f"[{s1},{s2}]"
#	print(f"Initial:       {begin_cur}")
	while True:
		cur = four_nested_pair(begin_cur)
#		if begin_cur != cur:
#			print(f"After explode: {cur}")
		if begin_cur == cur:
			cur = split_ten_or_greater(cur)
#			if begin_cur != cur:
#				print(f"After split:   {cur}")
		if begin_cur == cur:
			return begin_cur
		else:
			begin_cur = cur

def part1(data):
	cur_res = data[0]
	for i in range(1,len(data)):
		prev_cur = cur_res
		cur_res = add_snailfish(cur_res,data[i])
#		print(f"  {prev_cur}\n+ {data[i]}\n= {cur_res}")
	return magnitude(json.loads(cur_res))

def part2(data):
	return max(magnitude(json.loads(add_snailfish(data[i],data[j]))) for i in range(len(data)) for j in range(len(data)))

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	infile = sys.argv[1]
	#infile = "example4.txt"
	data = open(infile,"r").read().rstrip().split("\n")
	print(part1(data))
	print(part2(data))
