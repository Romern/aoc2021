from parse import parse

def draw_diagram(diagram):
	print("\n".join(["".join(str(i) if i!=0 else "." for i in d) for d in diagram]))

def part1(data):
	max_x = max(max(i[0],i[2]) for i in data)
	max_y = max(max(i[1],i[3]) for i in data)
	diagram = [[0]*(max_x+1) for _ in range(max_y+1)]
	for l in data:
		#only consider hor and vert lines
		if l[0] != l[2] and l[1] != l[3]:
			continue
		#vertical
		if l[0] == l[2]:
			for y in range(min(l[1],l[3]),max(l[1],l[3])+1):
				diagram[y][l[0]] += 1
		#horizontal
		if l[1] == l[3]:
			for x in range(min(l[0],l[2]),max(l[0],l[2])+1):
				diagram[l[1]][x] += 1
#	draw_diagram(diagram)
	return sum(i>=2 for l in diagram for i in l)

def part2(data):
	max_x = max(max(i[0],i[2]) for i in data)
	max_y = max(max(i[1],i[3]) for i in data)
	diagram = [[0]*(max_x+1) for _ in range(max_y+1)]
	for l in data:
		if l[0] == l[2]: #vertical
			for y in range(min(l[1],l[3]),max(l[1],l[3])+1):
				diagram[y][l[0]] += 1
		elif l[1] == l[3]: #horizontal
			for x in range(min(l[0],l[2]),max(l[0],l[2])+1):
				diagram[l[1]][x] += 1
		else: #diagonal
			start_x = min(l[0],l[2])
			end_x = max(l[0],l[2])
			start_y = l[1] if start_x == l[0] else l[3]
			end_y = l[3] if start_x == l[0] else l[1]
			asc = start_y < end_y
			cur_y = start_y
			for cur_x in range(start_x,end_x+1):
				diagram[cur_y][cur_x] += 1
				if asc:
					cur_y += 1
				else:
					cur_y -= 1
#	draw_diagram(diagram)
	return sum(i>=2 for l in diagram for i in l)


if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = [parse("{:d},{:d} -> {:d},{:d}\n", x) for x in open(sys.argv[1])]
	print(part1(data))
	print(part2(data))
