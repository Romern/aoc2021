from functools import reduce

def get_neighbors(data,i,j):
	if i != 0:
		yield (i-1,j,data[i-1][j])
	if i != len(data)-1:
		yield (i+1,j,data[i+1][j])
	if j != len(data[i])-1:
		yield (i,j+1,data[i][j+1])
	if j != 0:
		yield (i,j-1,data[i][j-1])

def get_low_points(data):
	low_points = []
	for i,l in enumerate(data):
		for j,p in enumerate(l):
			# only if there arent any higher points
			if not any(ap <= p for ai,aj,ap in get_neighbors(data,i,j)):
				low_points.append((i,j,p))
	return low_points

def part1(data):
	return sum(p+1 for _,_,p in get_low_points(data))

def get_basin_neighbors(data, i, j, p, cur_lowi, cur_lowj, visited):
	out = []
	for ni,nj,n in get_neighbors(data,i,j):
		# ignore 9s
		if n == 9:
			continue
		if (ni,nj) in visited:
			continue
		# only consider the neighbors which arent the basin, except when we currently are the basin
		cur_neigh = [(ai,aj,a) for ai,aj,a in get_neighbors(data,ni,nj) if not (ai==cur_lowi and aj==cur_lowj) or (i==cur_lowi and j==cur_lowj)]
		cur_min = min(p for _,_,p in cur_neigh)
		# recurse into those neighbors where we are the only smallest neighbor
		if cur_min == p:
			visited.add((ni,nj))
			out.append((ni,nj,n))
			out += get_basin_neighbors(data,ni,nj,n, cur_lowi, cur_lowj, visited)
	return out

def part2(data):
	# find basins
	out = []
	for i,j,p in get_low_points(data):
		out.append(get_basin_neighbors(data, i, j, p, i, j, {(i,j)}) + [(i,j,p)])
	# return the multiplied length of the three largest basins
	out_len = sorted(len(o) for i,o in enumerate(out))
	return reduce(lambda x, y: x*y, out_len[-3:])

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = [[int(i) for i in l] for l in open(sys.argv[1]).read().splitlines()]
	print(part1(data))
	print(part2(data))
