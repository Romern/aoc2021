def parse_packet(data, part2=False):
	version = int(data[:3],2)
	typeid = int(data[3:6],2)
	# literal value packet
	if typeid == 4:
		final_number = ""
		counter = 6
		last = False
		while not last:
			if data[counter] == "0":
				last = True
			final_number += data[counter+1:counter+1+4]
			counter += 5
		return int(final_number,2), version, counter
	# operator packet
	else:
		length_type_id = data[6]
		counter = 7
		total_length = None
		sub_packet_num = None
		if length_type_id == "0":
			total_length = int(data[7:7+15],2)
			counter += 15
		if length_type_id == "1":
			sub_packet_num = int(data[7:7+11],2)
			counter += 11
		packets = 0
		val = None
		offset = counter
		while (total_length and (counter-offset) < total_length) or (sub_packet_num and packets < sub_packet_num):
			subpacket_val, subpacket_version, res = parse_packet(data[counter:])
			counter += res
			packets += 1
			# part2 stuff
			if typeid == 0: # sum
				if val == None:
					val = 0
				val += subpacket_val
			elif typeid == 1: # mult
				if val == None:
					val = 1
				val *= subpacket_val
			elif typeid == 2: # min
				if val == None:
					val = subpacket_val
				val = min(val,subpacket_val)
			elif typeid == 3: # max
				if val == None:
					val = subpacket_val
				val = max(val,subpacket_val)
			elif typeid == 5: # greater than
				if val == None:
					val = subpacket_val
				else:
					val = 1 if val > subpacket_val else 0
			elif typeid == 6: # less than
				if val == None:
					val = subpacket_val
				else:
					val = 1 if val < subpacket_val else 0
			elif typeid == 7: # equals
				if val == None:
					val = subpacket_val
				else:
					val = 1 if val == subpacket_val else 0
			version += subpacket_version
		return val, version, counter

def hex_to_bin(h):
	return bin(int(h,16))[2:].zfill(4)

def part1(data):
	return parse_packet("".join(hex_to_bin(h) for h in data))[1]

def part2(data):
	return parse_packet("".join(hex_to_bin(h) for h in data))[0]

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	data = open(sys.argv[1],"r").read().splitlines()
	for l in data: # for ease of use to try multiple examples at once
		print(part1(l), part2(l))
