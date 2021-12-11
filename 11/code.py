def print_board(data):
	for l in data:
		print("".join(str(d) for d in l))

def part2(data):
	return part1(data,10000000,holdonsynchronizedflash=True)

def part1(datain,steps, holdonsynchronizedflash=False, doprint=False):
	data = [[d for d in l] for l in datain] # copy array
	flashes = 0
	for step in range(steps):
		if doprint:
			print(f"Before step {step}")
			print_board(data)
		for i in range(len(data)):
			for j in range(len(data[i])):
				data[i][j] += 1
		increased = True
		flashes_before = flashes
		while increased:
			increased = False
			for i in range(len(data)):
				for j in range(len(data[i])):
					if data[i][j] > 9:
						for ai in [-1,0,1]:
							for aj in [-1,0,1]:
								if i+ai < len(data) and j+aj < len(data[i+ai]) and i+ai >= 0 and j+aj >= 0 and data[i+ai][j+aj] >= 0:
									data[i+ai][j+aj] += 1
									increased = True
						data[i][j] = -1000
						flashes += 1
		for i in range(len(data)):
			for j in range(len(data[i])):
				if data[i][j] < 0:
					data[i][j] = 0
		if holdonsynchronizedflash and flashes-flashes_before == len(data)*len(data[0]):
			return data, step+1

	if doprint:
		print(f"After step {step}")
		print_board(data)
	return data, flashes

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = [[int(i) for i in l] for l in open(sys.argv[1]).read().splitlines()]
	print(part1(data,100))
	print(part2(data))
