#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : [Name:Vijayalaxmi Bhimrao Maigur Username:vbmaigur]
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json
from queue import PriorityQueue

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
	return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)

def moves(map, row, col):
    moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))
    # adding an extra paramater to the valid moves which gives the geographical directions
    direction=["S","N","W","E"]
    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    val_neighbour= [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]
    move=[]
    for m in val_neighbour:
        i=moves.index(m)
        move.append((m,direction[i]))
    return move


# Perform search on the map
# Perform search on the map
def search1(IUB_map):
    # Find my start position
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    visited=[]
    fringe=PriorityQueue()
    fringe.put((0,(you_loc,"")))
    final_path=[]
    while fringe:
        (curr_dist,(curr_move,path_str))=fringe.get()
        visited.append(curr_move)
        for move in moves(IUB_map, *curr_move):
            if move[0] not in visited:
                if IUB_map[move[0][0]][move[0][1]]=="@":
                    return str(curr_dist+1)+" "+(path_str+move[1])
                else:
                    fringe.put((curr_dist+1,(move[0],path_str+move[1])))
        if fringe.qsize()==0:
            return None

# Main Function
if __name__ == "__main__":
	IUB_map=parse_map(sys.argv[1])
	print("Shhhh... quiet while I navigate!")
	solution = search1(IUB_map)
	print("Here's the solution I found:")
	if solution!=None:
		print(solution)
	else:
		print("Inf")
