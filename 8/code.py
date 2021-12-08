import itertools

numberdict = {
	0: {"a","b","c","e","f","g"},
	1: {"c","f"},
	2: {"a","c","d","e","g"},
	3: {"a","c","d","f","g"},
	4: {"b","c","d","f"},
	5: {"a","b","d","f","g"},
	6: {"a","b","d","e","f","g"},
	7: {"a","c","f"},
	8: {"a","b","c","d","e","f","g"},
	9: {"a","b","c","d","f","g"}
}
segments = "abcdefg"

def part1(data):
	unique_number_segments = {len(numberdict[i]) for i in [1,4,7,8]}
	return sum(len(d) in unique_number_segments for (_,j) in data for d in j)

def part2(data):
	output_values = []
	for (i,o) in data:
		for config in itertools.permutations(segments):
			# get a mapping
			mapping_dict = {new:segments[f] for f,new in enumerate(config)}
			# check if all digits in the current line yield sensible displays
			found = True
			for dig in i:
				out = set(map((lambda x: mapping_dict[x]),dig))
				# check if digit is in numberdict
				if not any(out==a for a in numberdict.values()):
					found = False
					break
			if found:
				break
		if not found:
			raise Exception("hmmm")
		# we found our right mapping for this line, so now decode all outputs
		output_value = []
		for dig in o:
			mapping = set(map((lambda x: mapping_dict[x]),dig))
			for k,v in numberdict.items():
				if v == mapping:
					output_value.append(str(k))
					break
#					print(dig, " is actually ", k)
		output_values.append(int("".join(output_value)))
	return sum(output_values)
if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = [(lambda x: (set(x[0].split(" ")),list(x[1].split(" "))))(l.split(" | ")) for l in open(sys.argv[1]).read().rstrip("\n").split("\n")]
	print(part1(data))
	print(part2(data))
