def part1(inputdata):
	# the number of times a depth measurement increases
	return sum(inputdata[i-1] < inputdata[i] for i in range(1,len(inputdata)))


def part2(inputdata):
	# the number of times the sum of measurements in this three-measurement sliding window increases
	return sum(inputdata[i-2]+inputdata[i-1]+inputdata[i] < inputdata[i-1]+inputdata[i]+inputdata[i+1] for i in range(2,len(inputdata)-1))

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	inputdata = [int(i) for i in open(sys.argv[1],"r").read().strip("\n").split("\n")]
	print(part1(inputdata))
	print(part2(inputdata))
