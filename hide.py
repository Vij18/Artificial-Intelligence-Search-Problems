#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : [Vijayalaxmi Bhimrao Maigur Username: vbmaigur]
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys


# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])
	

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    
    newBoard  = None
    #check on top
    i=row
    valid_top=True
    while i>=0:
        i-=1
        if board[i][col]=="&":
            valid_top=True
            break
        if board[i][col]=="F":
            valid_top=False
            break

    #check on top
    j=col
    valid_left=True
    while j>=0:
        j-=1
        if board[row][j]=="&":
            valid_left=True
            break
        if board[row][j]=="F":
            valid_left=False
            break
    i=row+1
    valid_down=True
    while i<len(board):
        if board[i][col]=="&":
            valid_down=True
            break
        if board[i][col]=="F":
            valid_down=False
            break
        i+=1
    j=col+1
    valid_right=True
    while j<len(board[0]):
        if board[row][j]=="&":
            valid_right=True
            break
        if board[row][j]=="F":
            valid_right=False
            break
        j+=1
    
    if valid_left and valid_top and valid_right and valid_down:
        newBoard=board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]
#     print(board)
    return newBoard

# Get list of successors of given board state
def successors(board):
    
    listOfSucc = []
    for r in range(0, len(board)):
        for c in range(0,len(board[0])):
            if board[r][c] == '.' :
                newBoard = add_friend(board, r, c)
                if newBoard is not None:
                
                    listOfSucc.append(newBoard)
    
    return listOfSucc

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 


# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    visited=[]
    while len(fringe) > 0:
        curr_place=fringe.pop()
        visited.append(curr_place)
        for s in successors(curr_place):
            if s not in visited:
                if is_goal(s):
                    return(s)
                fringe.append(s)
            
    '''solu=successors(initial_board)'''


# Main Function
#import time as time
#start=time.time()
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])

    # This is K, the number of friends
    K = int(sys.argv[2])
    #K=9
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")
#end=time.time()
#print(end-start)
