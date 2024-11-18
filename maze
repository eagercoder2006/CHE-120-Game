#Notes: code includes generation of maze (incl list of path indexes in tuples of the form (y,x)), generation of snake and ladder positions in a dictionary


import random

#AW: This function, used for the creation of the maze, checks which direction (N, W, S, E) is valid for a path to be carved out
def validMoveExists(currentTile):
    valid = False
    #AW: The current position must be within the bounds of the maze (at least 3 tiles away from any edges), and there must not be a path in that direction to avoid self-intersecting paths
    if currentTile[0] > 2 and maze[currentTile[0] - 2][currentTile[1]] != " ": #NORTH
        validMoves.append(0)
        valid = True
    if currentTile[1] > 2 and maze[currentTile[0]][currentTile[1] - 2] != " ": #WEST
        validMoves.append(1)
        valid = True
    if currentTile[0] < mazeSize - 2 and maze[currentTile[0] + 2][currentTile[1]] != " ": #SOUTH
        validMoves.append(2)
        valid = True
    if currentTile[1] < mazeSize - 2 and maze[currentTile[0]][currentTile[1] + 2] != " ": #EAST
        validMoves.append(3)
        valid = True
    return valid

#AW: Creates the maze and fills all tiles with walls initially
maze = []
mazeSize = 25
#fill all spots with walls first
for i in range(mazeSize):
    row = []
    for j in range(mazeSize):
        row.append(chr(9608))
    maze.append(row)

#AW: Carves out a random "solution" path from bottom right to top left, going only north and west
#AW: Also adds coordinates of tile paths to a list for future use
paths = []
x = mazeSize - 2
y = mazeSize - 2
maze[y][x] = " "
maze[y + 1][x] = " "
paths.append((y+1, x))
paths.append((y, x))
current = 0
while x > 1 and y > 1:
    direction = random.randint(0,10)
    #AW: This random generation strongly favours changing direction (if generated int is from 1-10, change direction, if 0, keep the same direction), in order to improve the odds of creating a diagonal that actually reaches the other corner
    if direction >= 2:
        direction = abs(current - 1)
    if direction == 0 and y > 2: #NORTH
        maze[y - 1][x] = " "
        maze[y - 2][x] = " "
        paths.append((y-1,x))
        paths.append((y-2,x))
        y = y - 2
        current = 0
    elif direction == 1 and x > 2: #WEST
        maze[y][x - 1] = " "
        maze[y][x - 2] = " "
        paths.append((y,x-1))
        paths.append((y,x-2))
        x = x - 2
        current = 1

#AW: Fills in the remaining tiles so that the path from start to finish is connected
if x <= 1:
   for i in range(y):
       maze[i][1] = " "
       paths.append((y-i-1,1))
else:
    for i in range(1,x):
        maze[1][i] = " "
        paths.append((1,x-i))
    paths.append((0,1))
    maze[0][1] = " "     


#AW: Generates the branches of the maze by iterating through the solution path by two (so that adjacent paths are at least separated by one wall). Checks for valid potential directions, then randomly selects one to move in (again by two tiles).
#AW: Stops moving down that branch when there are no more available paths, then backtracks to the original tile on the main solution path
currentTile = (mazeSize - 2, mazeSize - 2)
pathLength = len(paths)
for i in range(1, pathLength, 2):
    validMoves = []
    while True:
        validMoves.clear()
        if validMoveExists(currentTile):
            direction = validMoves[random.randint(0,len(validMoves)) - 1]
            if direction == 0: #NORTH
                #AW: Replaces the wall with paths, then adds those path coordinates to the paths list
                maze[currentTile[0] - 1][currentTile[1]] = " "
                maze[currentTile[0] - 2][currentTile[1]] = " "
                paths.append((currentTile[0] - 1, currentTile[1]))
                paths.append((currentTile[0] - 2, currentTile[1]))
                currentTile = (currentTile[0] - 2, currentTile[1])
            elif direction == 1: #WEST
                maze[currentTile[0]][currentTile[1] - 1] = " "
                maze[currentTile[0]][currentTile[1] - 2] = " "
                paths.append((currentTile[0], currentTile[1] - 1))
                paths.append((currentTile[0], currentTile[1] - 2))
                currentTile = (currentTile[0], currentTile[1] - 2)
            elif direction == 2: #SOUTH
                maze[currentTile[0] + 1][currentTile[1]] = " "
                maze[currentTile[0] + 2][currentTile[1]] = " "
                paths.append((currentTile[0] + 1, currentTile[1]))
                paths.append((currentTile[0] + 2, currentTile[1]))
                currentTile = (currentTile[0] + 2, currentTile[1])
            else: #EAST
                maze[currentTile[0]][currentTile[1] + 1] = " "
                maze[currentTile[0]][currentTile[1] + 2] = " "
                paths.append((currentTile[0], currentTile[1] + 1))
                paths.append((currentTile[0], currentTile[1] + 2))
                currentTile = (currentTile[0], currentTile[1] + 2)
        else:
            currentTile = paths[i] #AW: Backtrack to original tile to continue for loop
            break

#print(paths)
#show the maze - FOR TESTING ONLY, REMOVE FROM FINAL CODE
for i in range(mazeSize):
    for j in range(mazeSize):
        print(maze[i][j], end="")
    print()
        
snakes = {}
ladders = {}

#AW: Generating ladders: a 45:1 ratio of paths to ladders produces a balanced board
for i in range(len(paths) // 45):
    #AW: Randomly select a path tile as a starting position for a ladder, then pick an end position. If the end is lower down than the start, retry
    start = random.randint(0, len(paths) - 1)
    end = random.randint(0, len(paths) - 1)
    while paths[start][0] <= paths[end][0] or paths[start] in ladders:
        start = random.randint(0, len(paths) - 1)
        end = random.randint(0, len(paths) - 1)
    #AW: Add the ladder key (start pos) and value (end pos) to the ladders dictionary
    ladders[paths[start]] = paths[end]
    #REMOVE FROM FINAL CODE. THIS IS JUST FOR TESTING
    maze[paths[start][0]][paths[start][1]] = chr(i+65)
    maze[paths[end][0]][paths[end][1]] = chr(i+65)
#print(ladders)
#print()


#AW: Generating snakes
for i in range(len(paths) // 45):
    start = random.randint(0, len(paths) - 1)
    end = random.randint(0, len(paths) - 1)
    #AW: Similarly, if the end position of the snake is higher up than the start position or if the start position is already taken by a ladder, regenerate a starting and end position
    while paths[start][0] >= paths[end][0] or paths[start] in snakes or paths[start] in ladders:
        start = random.randint(0, len(paths) - 1)
        end = random.randint(0, len(paths) - 1)
    #AW: Add the snake key and value to the snakes dictionary
    snakes[paths[start]] = paths[end]
    #REMOVE FROM FINAL CODE, ONLY FOR TESTING
    maze[paths[start][0]][paths[start][1]] = chr(i+97)
    maze[paths[end][0]][paths[end][1]] = chr(i+97)

#print(snakes)
#show the board, ONLY FOR TESTING.
for i in range(mazeSize):
    for j in range(mazeSize):
        print(maze[i][j], end="")
    print()
