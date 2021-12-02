def part1(inputdata):
	# What do you get if you multiply your final horizontal position by your final depth?
	hpos = 0
	depth = 0
	for cmd, i in inputdata:
		if cmd == "forward":
			hpos += i
		elif cmd == "up":
			depth -= i
		elif cmd == "down":
			depth += i
	return hpos * depth

def part2(inputdata):
	# What do you get if you multiply your final horizontal position by your final depth?
	hpos = 0
	depth = 0
	aim = 0
	for cmd, i in inputdata:
		if cmd == "forward":
			hpos += i
			depth += aim * i
		elif cmd == "up":
			aim -= i
		elif cmd == "down":
			aim += i
	return hpos * depth

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	inputdata = [(lambda c: (c[0], int(c[1])))(s.split(" ")) for s in open(sys.argv[1]).readlines()]
	print(part1(inputdata))
	print(part2(inputdata))
