import math
from parse import parse
import itertools
from collections import Counter

def part1(data):
	states = Counter()
	for state, xstart, xstop, ystart, ystop, zstart, zstop in data:
		state = 1 if state == "on" else 0
		for x in range(max(xstart,-50), min(51,xstop+1)):
			for y in range(max(ystart,-50), min(51,ystop+1)):
				for z in range(max(-50,zstart), min(50,zstop+1)):
					states[x,y,z] = state
	return sum(states.values())

def is_inside(xstart, xstop, ystart, ystop, zstart, zstop, oxstart, oxstop, oystart, oystop, ozstart, ozstop):
	return oxstart >= xstart and oxstop <= xstop and oystart >= ystart and oystop <= ystop and ozstart >= zstart and ozstop <= zstop

def is_overlapping(xstart, xstop, ystart, ystop, zstart, zstop, oxstart, oxstop, oystart, oystop, ozstart, ozstop):
	return xstart <= oxstop - 1 and xstop - 1 >= oxstart and ystart <= oystop - 1  and ystop - 1 >= oystart and zstart <= ozstop - 1 and zstop - 1 >= ozstart

# after failing to get my convuluted solution working, basically this: https://github.com/anthonywritescode/aoc2021/blob/main/day22/part2.py

def subtract(xstart, xstop, ystart, ystop, zstart, zstop, oxstart, oxstop, oystart, oystop, ozstart, ozstop):
	if not is_overlapping(xstart, xstop, ystart, ystop, zstart, zstop, oxstart, oxstop, oystart, oystop, ozstart, ozstop):
		# if we arent overlapping, then the result is just the first input
		return [(xstart, xstop, ystart, ystop, zstart, zstop)]
	elif is_inside(oxstart, oxstop, oystart, oystop, ozstart, ozstop, xstart, xstop, ystart, ystop, zstart, zstop):
		# if we are inside the second one, then just return nothing
		return []

	xs = sorted((xstart,xstop,oxstart,oxstop))
	ys = sorted((ystart,ystop,oystart,oystop))
	zs = sorted((zstart,zstop,ozstart,ozstop))
	ret = []
	for x0, x1 in zip(xs, xs[1:]):
		for y0, y1 in zip(ys, ys[1:]):
			for z0, z1 in zip(zs, zs[1:]):
				if is_inside(xstart, xstop, ystart, ystop, zstart, zstop, x0,x1,y0,y1,z0,z1) and not is_overlapping(x0,x1,y0,y1,z0,z1,oxstart, oxstop, oystart, oystop, ozstart, ozstop):
					ret.append((x0,x1,y0,y1,z0,z1))
	return ret

def get_size(xstart, xstop, ystart, ystop, zstart, zstop):
	return (xstop-xstart)*(ystop-ystart)*(zstop-zstart)

def part2(data):
	# use ranges instead of individual points
	ranges = Counter()
	cubes = []
	for i, (state, xstart, xstop, ystart, ystop, zstart, zstop) in enumerate(data):
		xstop += 1
		ystop += 1
		zstop += 1
#		print(f"{i}/{len(data)}: {sum(get_size(*cube) for cube in cubes)} {len(cubes)}")
#		if i == 1:
#			print(cubes)
		cubes = [split for oxstart, oxstop, oystart, oystop, ozstart, ozstop in cubes for split in subtract(oxstart, oxstop, oystart, oystop, ozstart, ozstop ,xstart, xstop, ystart, ystop, zstart, zstop)]
		if state == "on":
			cubes.append((xstart, xstop, ystart, ystop, zstart, zstop))
	return sum(get_size(*cube) for cube in cubes)
	""" #Yeah this was convoluted
	for i, (state, xstart, xstop, ystart, ystop, zstart, zstop) in enumerate(data):
		print(f"{i}/{len(data)}")
		state = 0 if state == "off" else 1
		# initialization
		if state == 1 and len(ranges)==0:
			ranges[(xstart, xstop, ystart, ystop, zstart, zstop)] = 1
			continue
		if state == 0 and len(ranges)==0:
			continue
		# check if there is overlap:
		delete_and_split = [] # (delete_key, add_key)
		new_range = True
		for oxstart, oxstop, oystart, oystop, ozstart, ozstop in ranges:
			# if overlap exists, split the range
			if is_inside(xstart, xstop, ystart, ystop, zstart, zstop, oxstart, oxstop, oystart, oystop, ozstart, ozstop):
				print(f"{i} IS INSIDE")
				# current instruction is inside another existing one
				if state == 0: # if state == 0, just subtract it, else, we dont need to do anything
					delete_and_split.append(((oxstart, oxstop, oystart, oystop, ozstart, ozstop),subtract(oxstart, oxstop, oystart, oystop, ozstart, ozstop, xstart, xstop, ystart, ystop, zstart, zstop)))
				new_range = False
				break
			elif is_inside(oxstart, oxstop, oystart, oystop, ozstart, ozstop, xstart, xstop, ystart, ystop, zstart, zstop):
				print(f"{i} IS AROUND")
				# current instruction is around another existing one
				if state == 0: # if state == 0, just delete the existing cube
					delete_and_split.append(((oxstart, oxstop, oystart, oystop, ozstart, ozstop),[]))
				else: # if state == 1, then extend the area: it could happen that we now overlap with another area though...
					delete_and_split.append(((oxstart, oxstop, oystart, oystop, ozstart, ozstop)),[(xstart, xstop, ystart, ystop, zstart, zstop)])
				new_range = False
			elif is_overlapping(xstart, xstop, ystart, ystop, zstart, zstop, oxstart, oxstop, oystart, oystop, ozstart, ozstop):
				print(f"{i} IS OVERLAPPING")
				# current instruction is partially inside another existing one
				if state == 0: # we subtract the new one
					delete_and_split.append(((oxstart, oxstop, oystart, oystop, ozstart, ozstop),subtract(oxstart, oxstop, oystart, oystop, ozstart, ozstop, xstart, xstop, ystart, ystop, zstart, zstop)))
				else: # we subtract both, and add the new areas
					delete_and_split.append(((oxstart, oxstop, oystart, oystop, ozstart, ozstop),[(xstart, xstop, ystart, ystop, zstart, zstop)] + subtract(oxstart, oxstop, oystart, oystop, ozstart, ozstop, xstart, xstop, ystart, ystop, zstart, zstop)))
				new_range = False
				break
		if new_range and state == 1:
			# new range, no splitting
			delete_and_split.append((None, [((xstart, xstop, ystart, ystop, zstart, zstop), state)]))
		else:
			# delete old ranges and add new split ranges
			for delete_key, add_key in delete_and_split:
				del ranges[delete_key]
				for k in add_key:
					ranges[k] = 1
	return sum((xstop-xstart)*(ystop-ystart)*(zstop-zstart) for xstart, xstop, ystart, ystop, zstart, zstop in ranges.keys())"""

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	infile = sys.argv[1]
#	infile = "example.txt"
	data = [parse("{:w} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}",l).fixed for l in open(infile,"r").read().splitlines()]
#	print(data)
	print(part1(data))
	print(part2(data))
