from parse import parse

def fold(dots, fold_instructions):
	old_dots = dots
	new_dots = set()
	for axis, coord in fold_instructions:
		if axis == "x":
			for (x,y) in old_dots:
				if x > coord:
					new_dots.add((coord - (x-coord),y))
				else:
					new_dots.add((x,y))
		elif axis == "y":
			for (x,y) in old_dots:
				if y > coord:
					new_dots.add((x,coord - (y-coord)))
				else:
					new_dots.add((x,y))
		old_dots = new_dots
		new_dots = set()
	return old_dots

def plot_data(dots):
	xmax = max(d[0] for d in dots)
	ymax = max(d[1] for d in dots)
	for y in range(ymax+1):
		for x in range(xmax+1):
			print("#" if (x,y) in dots else ".", end="")
		print()

def part1(data):
	dots, fold_instructions = data
#	plot_data(dots)
#	print()
	dots = fold(dots, fold_instructions[:1])
#	plot_data(dots)
	return len(dots)

def part2(data):
	dots, fold_instructions = data
	dots = fold(dots, fold_instructions)
	plot_data(dots)

def parse_input(input):
	dots, fold_instructions = input.split("\n\n")
	dots = set(parse("{:d},{:d}",d).fixed for d in dots.splitlines())
	fold_instructions = [parse("fold along {:w}={:d}",d).fixed for d in fold_instructions.splitlines()]
	return dots, fold_instructions

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = parse_input(open(sys.argv[1],"r").read())
	print(part1(data))
	part2(data)
