from parse import parse
from tqdm import trange

def part1(data):
	xmin, xmax, ymin, ymax = data
	cur_max = (0,0,-100)
	applicable_configs = 0
	for init_xvel in trange(1000,-1000,-1):
		for init_yvel in range(1000,-1000,-1):
			xvel = init_xvel
			yvel = init_yvel
			x = 0
			y = 0
			ymaxreached = -100
			overshot = False
			while not (x >= xmin and x <= xmax and y >= ymin and y <= ymax):
				# overshoot condition:
				if y < ymin:
					overshot = True
					break
				ymaxreached = max(y,ymaxreached)
				x += xvel
				y += yvel
				xvel = xvel + 1 if xvel < 0 else (xvel - 1 if xvel > 0 else xvel)
				yvel -= 1
			if not overshot:
				applicable_configs += 1
				print(applicable_configs)
				if cur_max[2] < ymaxreached:
					cur_max = (init_xvel,init_yvel,ymaxreached)
					print(cur_max)
	return cur_max, applicable_configs

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = parse("target area: x={:d}..{:d}, y={:d}..{:d}",open(sys.argv[1],"r").read().rstrip()).fixed
	print(part1(data))
