from parse import parse

def parse_data(input):
	polymer_template, rules = input.split("\n\n")
	rules = [parse("{:w} -> {:w}",r).fixed for r in rules.splitlines()]
	rules = {a:b for a,b in rules}
	return polymer_template, rules

def part1(data, steps):
	polymer_template, rules = data
	polymer_amounts = dict()
	for i in range(len(polymer_template)-1):
		if not polymer_amounts.get(polymer_template[i]+polymer_template[i+1]):
	 		polymer_amounts[polymer_template[i]+polymer_template[i+1]] = 0
		polymer_amounts[polymer_template[i]+polymer_template[i+1]] +=1
	for step in range(1,steps+1):
		new_amounts = dict()
		single_amounts = dict()
		for pair, count in polymer_amounts.items():
			if not rules.get(pair):
				continue
			if not new_amounts.get(pair[0]+rules[pair]):
				new_amounts[pair[0]+rules[pair]] = 0
			if not new_amounts.get(rules[pair]+pair[1]):
				new_amounts[rules[pair]+pair[1]] = 0
			if not single_amounts.get(pair[0]):
				single_amounts[pair[0]] = 0
			if not single_amounts.get(rules[pair]):
				single_amounts[rules[pair]] = 0

			new_amounts[pair[0]+rules[pair]] += count
			new_amounts[rules[pair]+pair[1]] += count
			single_amounts[pair[0]] += count
			single_amounts[rules[pair]] += count
		polymer_amounts = new_amounts
		print(f"Step {step}")
#		print(f"Step {step}: {polymer_amounts}")
	keys = {l for s in polymer_amounts for l in s}
	return sorted(single_amounts.values())[-1] - sorted(single_amounts.values())[0]

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = parse_data(open(sys.argv[1],"r").read())
	print(part1(data,10))
	print(part1(data,40))
