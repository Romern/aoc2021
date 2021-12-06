# Surely, each lanternfish creates a new lanternfish once every 7 days.
# So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.
# two more days for its first cycle.
#def part1(data):
#	print(f'Initial state: {",".join(str(d) for d in data)}')
#	for day in range(80):
#		for i in range(len(data)):
#			data[i] = data[i] - 1
#			if data[i] < 0:
#				data[i] = 6
#				data += [8]
#		print(f'After {day} days: {",".join(str(d) for d in data)}')
#	return len(data)

def part2(data, days):
	lifestage = [data.count(i) for i in range(7)]
	lifestage_plus = [0,0]
	print(f'Initial state: {sum(lifestage + lifestage_plus)}')
	for day in range(days):
		# reset daycount, i.e. fish with life 0 will be life 6 and make new bebes
		temp = lifestage[0]
		lifestage = lifestage[1:] + [temp + lifestage_plus[0]]
		lifestage_plus = [lifestage_plus[1], temp]
		print(f'After {day} days: {sum(lifestage + lifestage_plus)}')
	return sum(lifestage + lifestage_plus)

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = [int(i) for i in open(sys.argv[1]).read().rstrip("\n").split(",")]
#	print(part1(data))
	print(part2(data,80))
	print(part2(data,256))
