def dfs_part1(data, cur_path, paths):
	if cur_path[-1] == "end":
		paths.append(cur_path)
		return
	for n in data.get(cur_path[-1],[]):
		# small caves only once
		if n.islower() and n in cur_path:
			continue
		dfs_part1(data, cur_path + [n], paths)
	return

def part1(data):
	paths = []
	dfs_part1(data, ["start"], paths)
	return len(paths)

def max_small_cave_count(path):
	return any(d.islower() and path.count(d) == 2 for d in path)

def dfs_part2(data, cur_path, paths):
	if cur_path[-1] == "end":
		paths.append(cur_path)
		return
	for n in data.get(cur_path[-1],[]):
		# one small cave twice
		if n.islower() and max_small_cave_count(cur_path) and cur_path.count(n)>=1:
			continue
		if n == "start":
			continue
		dfs_part2(data, cur_path + [n], paths)
	return

def part2(data):
	paths = []
	dfs_part2(data, ["start"], paths)
#	return "\n".join(sorted(",".join(p) for p in paths))
	return len(paths)

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = dict()
	for l in open(sys.argv[1]).read().splitlines():
		a,b = l.split("-")
		if not data.get(a):
			data[a] = set()
		if not data.get(b):
			data[b] = set()
		data[a].add(b)
		data[b].add(a)
	print(part1(data))
	print(part2(data))
