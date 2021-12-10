delims = {
	"(": ")",
	"{": "}",
	"[": "]",
	"<": ">"
}
opening_chars = set(delims.keys())
closing_chars = set(delims.values())
illegal_character_table = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}
incomplete_character_table = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4
}


def part1(data):
	score = 0
	for l in data:
		opening = []
		for c in l:
			# if closing character
			if c in closing_chars:
				if delims[opening[-1]] != c:
					# corrupted
					score += illegal_character_table[c]
					break
				else:
					opening = opening[:-1]
			else: # only valid characters are assumed, so this is a opening character
				opening += [c]
	return score

def part2(data):
	scores = []
	for l in data:
		opening = []
		corrupt = False
		for c in l:
			# if closing character
			if c in closing_chars:
				if delims[opening[-1]] != c:
					# corrupted
					corrupt = True
					break
				else:
					opening = opening[:-1]
			else:
				opening += [c]
		if not corrupt and len(opening) != 0:
			# incomplete
			score = 0
			for i in opening[::-1]:
				score = (score * 5) + incomplete_character_table[delims[i]]
			scores.append(score)
	return sorted(scores)[int(len(scores)/2)]

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = open(sys.argv[1]).read().splitlines()
	print(part1(data))
	print(part2(data))
