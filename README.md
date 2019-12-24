# a0

### Question 1
The program does not work very well; it will probably enter an innite loop and you'll
have to press CONTROL-C to kill it. Nevertheless, the code is a good starting point, so familiarize
yourself with it. Figure out the precise search abstraction that the program is using and include it in
your report. In other words, what is the set of valid states, the successor function, the cost function,
the goal state defnition, and the initial state?

Code name: find_luddy.py
Input is map.txt

##### Sol: 

State Space: It contains all the possible combination of a given arrangement. For eg. Let's take a NxM matrix that is given in the assignment, every cell can have two values "." and "&", so the number of state space is 2^(N*M).

Valid State: It is the subset of the state space, contains all the valid state that a problem can take to trasition from n to n+1 state satisfying all the condition. Here, the valid state from the given state can be moving in N,E,W,S direction and entering the cells that has ".".

Successor Function: Here, the function returns all the possible valid states from the given state.

Cost Function: Here the cost is 1 to move in N,E,W,S direction from the given cell.

Goal State Defnition: Traversing to the destination(reaching "@") via shortest possible path.

Initial State: Starting point ("#" in the graph)

Implementation: 
1. Fringe here is declared as a priority queue with cost of path traversed as the priority.
2. Everytime fringe is appended with the current position and the string of the path that has been traversed by code upto that position
3. Here, priority queue handles the condition where there are multiple moves for a single position by assigning the priority and poping elements according to priority.
4. Also, the code has list called visited which keeps track of all the nodes that a program has already visited, which doesnt let the program get stuck in infinite loop.


### Question 2
You've made k new friends so far at IU, but none of them like each another. Your goal is to arrange your
friends on the IU campus such that no two of your friends can see one another. Write a program called
hide.py that takes the lename of a map in the same format as Part 1 as well as a single parameter specifying
the number k of friends you have. Assume two friends can see each other if they are on either the same row
or column of the map, and there are no buildings between them. Your friends can only be positioned on
sidewalks. (It's okay if friends see you. Any building including Luddy Hall obscures the view, but you do
not.) Your program should output to the screen (in the last lines of its output) a new version of the map,
but with your friends' locations marked with letters F. If there is no solution, your program should just
display None.

Code name: hide.py
Input: map.txt and K(number of face to be inserted)
##### Sol: 

State Space: ALl possible combination of map with and without F at ".". i.e. again 2^(N*M)

Valid State: Here, the valid state from the given state is inserting a "F" if there are no "F" in the correspoding row or column and also two F can be in same row if there is "&" in between them.

Successor Function: Here, the function returns all the possible positions that F can be inserted in the input matrix.

Goal State Defnition: Successfully placing k "F" while satisfying the conditions mentioned in the valid state definition. 

Initial State: Map with no "F" inserted.

Implementation: 
1. Fringe here contains map and is popped off. We use BFS in this code.
2. Successor function iterates through every "." in the given matrix and calls the add_friend function to insert "F".

Lets consider position P where "F" has to be inserted

3. Add_friend function has four while loop to handle four directions from P. Here, every while loop checks every node in one particular direction from P. If the loop encounters "&" first, it checks other direction and validates P and then inserts "F". If the loop encounters "F" first in any one direction then it breaks out of the function and returns None. If the function does not encounter "F" in any direction then it inserts "F" at P.

4. This is continued till number of F inserted in the map is not equal to K.

