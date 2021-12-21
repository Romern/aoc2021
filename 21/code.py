import math
from parse import parse
import itertools
from collections import Counter

def roll_det_dice(cur_value,counter):
	if cur_value == 98:
		return 98 + 99 + 100, 1,counter+3
	if cur_value == 99:
		return 99 + 100 + 1, 2,counter+3
	elif cur_value == 100:
		return 100 + 1 + 2, 3,counter+3
	else:
		return 3*cur_value+3,cur_value+3,counter+3

def part1(data):
	cur_pos = [data[0],data[1]]
	player_scores = [0,0]
	dice_value = 1
	turn = 0
	dice_counter = 0
	while player_scores[0]<1000 and player_scores[1]<1000:
		dice_result, dice_value, dice_counter = roll_det_dice(dice_value,dice_counter)
		cur_pos[turn] = ((cur_pos[turn] + dice_result - 1) % 10) + 1 # wrap around at 10->1
		player_scores[turn] += cur_pos[turn]
#		print(f"Player {turn+1} rolls {dice_result} and moves to space {cur_pos[turn]} for a total score of {player_scores[turn]}.")
		turn = (turn + 1) % 2
	return (player_scores[0] if player_scores[0]<1000 else player_scores[1]) * dice_counter

encounters = Counter(i + j + k for i in (1, 2, 3) for j in (1, 2, 3) for k in (1, 2, 3))
cache = dict()

def play_game_and_count(cur_pos_1, cur_pos_2, score_1, score_2):
	if cache.get((cur_pos_1, cur_pos_2, score_1, score_2)):
		return cache.get((cur_pos_1, cur_pos_2, score_1, score_2))
	# cur_pos_1, cur_pos_2, score_1, score_2, turn, dice_val, encounters
	# 10*10*21*21*2*many
	init_pos = [cur_pos_1, cur_pos_2]
	cur_pos = [cur_pos_1, cur_pos_2]
	init_player_scores = [score_1, score_2]
	player_scores = [score_1, score_2]
	player_1_wins = 0
	player_2_wins = 0
	for dice_result, occurences in encounters.items():
		cur_pos[0] = ((init_pos[0] + dice_result - 1) % 10) + 1 # wrap around at 10->1
		player_scores[0] = init_player_scores[0] + cur_pos[0]
		if player_scores[0] < 21:
			player_2_wins_sub, player_1_wins_sub = play_game_and_count(cur_pos[1], cur_pos[0], player_scores[1], player_scores[0])
			player_1_wins += player_1_wins_sub * occurences
			player_2_wins += player_2_wins_sub * occurences
		else:
			player_1_wins += occurences
	cache[(cur_pos_1, cur_pos_2, score_1, score_2)] = (player_1_wins, player_2_wins)
	return player_1_wins, player_2_wins

def part2(data):
	player_1_wins, player_2_wins = play_game_and_count(data[0], data[1], 0, 0)
	return max(player_1_wins, player_2_wins)

if __name__ == "__main__":
	import sys
	if len(sys.argv)<2:
		print("Gib data")
		exit()
	infile = sys.argv[1]
#	infile = "example.txt"
	data = [int(l[-1]) for l in open(infile,"r").read().splitlines()]
	print(part1(data))
	print(part2(data))
