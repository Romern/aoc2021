
def dfs(data, cur_path, paths, condition):
	if cur_path[-1] == "end":
		paths.append(cur_path)
		return
	for n in data.get(cur_path[-1],[]):
		if condition(n, cur_path):
			continue
		dfs(data, cur_path + [n], paths, condition)
	return

# small caves only once
def part1_condition(n, cur_path):
	return n.islower() and n in cur_path

def part1(data):
	paths = []
	dfs(data, ["start"], paths, part1_condition)
	return len(paths)

def max_small_cave_count(path):
	return any(d.islower() and path.count(d) == 2 for d in path)

# one small cave twice, start only once
def part2_condition(n, cur_path):
	return (n.islower() and max_small_cave_count(cur_path) and cur_path.count(n)>=1) or n == "start"

def part2(data):
	paths = []
	dfs(data, ["start"], paths, part2_condition)
#	return "\n".join(sorted(",".join(p) for p in paths))
	return len(paths)

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = dict()
	# input parsing, prepare graph dict
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
