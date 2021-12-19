from parse import parse
import itertools
from collections import Counter

def manhatten_distance(a,b):
	return int(sum(abs(a[i]-b[i]) for i in range(len(a))))

def solve(data):
	coords = {(x,y,z):"B" for x,y,z in data[0]}
	coords[(0,0,0)] = "S"
	redo = list(range(1,len(data)))
	while redo:
		for i in list(redo):
			for reorient in reorient_iterator():
				new_scanner = map(reorient,data[i])
				diffs = Counter()
				for xb,yb,zb in new_scanner:
					for xa,ya,za in coords:
						diffs[xa-xb, ya-yb, za-zb] += 1
				diff = next((d for d in diffs if diffs[d] >= 12), None)
				if diff:
					for x,y,z in map(reorient,data[i]):
						coords[x+diff[0],y+diff[1],z+diff[2]] = "B"
					coords[diff] = "S"
					redo.remove(i)
					break
	scanners = [c for c,v in coords.items() if v == "S"]
	return sum(c == "B" for c in coords.values()), max(manhatten_distance(a,b) for a in scanners for b in scanners)
	# part1, part2

def reorient_iterator():
	# apparently too much, but works i guess
	for rotation in itertools.permutations([0,1,2]):
		for orientation in itertools.product([1,-1], repeat=3):
			yield lambda coord: (orientation[0] * coord[rotation[0]], orientation[1] * coord[rotation[1]], orientation[2] * coord[rotation[2]])

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	infile = sys.argv[1]
	data = [[parse("{:d},{:d},{:d}",l).fixed for l in s.split("\n")[1:]] for s in open(infile,"r").read().rstrip().split("\n\n")]
	print(solve(data))
