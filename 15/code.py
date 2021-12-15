import networkx as nx
import math

def print_graph(G, weight_function, path=[]):
	maxnode = max(G.nodes)
	for y in range(maxnode[1]+1):
		for x in range(maxnode[0]+1):
			if (x,y) in path:
				print("#", end="")
			else:
				print(str(weight_function(None,(x,y),None)), end="")
		print()

def build_graph_and_calc_risk(data,scale,weight_function):
	G = nx.Graph()
	G.add_edges_from([((x,y),(x+1,y)) for x in range(len(data[0])*scale-1) for y in range(len(data)*scale)])
	G.add_edges_from([((x,y),(x-1,y)) for x in range(1,len(data[0])*scale) for y in range(len(data)*scale)])
	G.add_edges_from([((x,y),(x,y+1)) for x in range(len(data[0])*scale) for y in range(len(data)*scale-1)])
	G.add_edges_from([((x,y),(x,y-1)) for x in range(len(data[0])*scale) for y in range(1,len(data)*scale)])
	sp = nx.shortest_path(G,source=(0,0),target=(len(data[0])*scale-1,len(data)*scale-1),weight=weight_function)
#	print_graph(G, weight_function)
#	print()
#	print_graph(G, weight_function, sp)
#	print(sp)
	return sum(weight_function(None,(a,b),None) for a,b in sp) - data[0][0]

def part1_weight(u,v,d):
	return data[v[1]][v[0]]

def part1(data):
	return build_graph_and_calc_risk(data,1,part1_weight)

def manhatten_distance(a1,b1,a2,b2):
	return abs(a1-b1)+abs(a2-b2)

def modulo_one_nine(n): # whyyyyyyyyy
	while n>9:
		n -= 9
	return n

def part2_weight(u,v,d):
	orig_weight = data[v[1] % len(data)][v[0] % len(data[0])]
	md = manhatten_distance(0, math.floor(v[0]/len(data[0])), 0, math.floor(v[1]/len(data)))
	return modulo_one_nine(orig_weight + md)

def part2(data):
	return build_graph_and_calc_risk(data,5,part2_weight)

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = [[int(i) for i in l] for l in open(sys.argv[1],"r").read().splitlines()]
	print(part1(data))
	print(part2(data))
