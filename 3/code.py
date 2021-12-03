def gamma_rate(inputdata):
	return "".join(str("0" if sum(b[i] == "0" for b in inputdata) > sum(b[i] == "1" for b in inputdata) else "1") for i in range(len(inputdata[0])))

def epsilon_rate(gamma_rate):
	return "".join("0" if i == "1" else "1" for i in gamma_rate)

def part1(inputdata):
	gr = gamma_rate(inputdata)
	er = epsilon_rate(gr)
	return int(gr,2)*int(er,2)

def oxygen_generator_rating(inputdata, i):
	counts = [sum(b[i] == "0" for b in inputdata),sum(b[i] == "1" for b in inputdata)]
	most_common = "0" if counts[0] > counts[1] else "1"
	return [b for b in inputdata if b[i] == most_common]

def co2_scrubber_rating(inputdata, i):
	counts = [sum(b[i] == "0" for b in inputdata),sum(b[i] == "1" for b in inputdata)]
	least_common = "0" if counts[0] <= counts[1] else "1"
	return [b for b in inputdata if b[i] == least_common]

def part2(inputdata):
	cur = inputdata
	i = 0
	while len(cur) != 1 and i < len(inputdata):
		cur = oxygen_generator_rating(cur,i)
		i += 1
	oxy = cur[0]
	cur = inputdata
	i = 0
	while len(cur) != 1 and i < len(inputdata):
		cur = co2_scrubber_rating(cur,i)
		i += 1
	co2 = cur[0]
	return int(oxy,2)*int(co2,2)

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	inputdata = open(sys.argv[1]).read().strip("\n").split("\n")
	print(part1(inputdata))
	print(part2(inputdata))
