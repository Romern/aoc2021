def part1(data):
	return min(sum(abs(chosen_pos-i) for i in data) for chosen_pos in range(max(data)))

def gaussian_sum(ub):
	# calcs sum_{k=0}^nk
	return int((ub*(ub+1))/2)

def part2(data):
	return min(sum(gaussian_sum(abs(chosen_pos-i)) for i in data) for chosen_pos in range(max(data)))

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = [int(i) for i in open(sys.argv[1]).read().rstrip("\n").split(",")]
	print(part1(data))
	print(part2(data))
