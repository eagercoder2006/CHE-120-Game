import random

#NT: simple print statements that will be used to make the game more interactive, these will be randomly printed at
#NT: the beginning of each turn, or when a player encounters a snake or ladder
player_turn_text = ["MOVE!", "Please proceed.", "You ready to win this?", "Let's Go!"]
snake_bite_text = ["Ouch!", "whomp whomp", "oh no", "did that hurt?", "Slide you later!"]
ladder_jump = ["Woop woop", "YAY", "Climb up!", "You're closer to the end"]

#NT: just a message that goes over the rules and how to play the game
def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.

    Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.
    """
    print(msg)

def player_turn():
    dice_roll = random.randint(1,6)
#NT: python's random module to generate a random integer, and the arguments specify that the random
#NT: number should be between 1 and 6 (inclusive)
    print ("You got a " + str(dice_roll))
    return dice_roll

def get_player_names():
    players = []
    no_of_players = input("How many players would you like to play with? You must play with 2, 3 or 4 players. ")
    while no_of_players != "2" and no_of_players != "3" and no_of_players != "4":
        no_of_players = input("Invalid input. How many players would you like to play with? You must play with 2, 3 or 4 players. ")
    no_of_players = int(no_of_players)
    print()
    
#I.R: This line says that the variable player1_name initially does not have a value, as it will get filled when the user inputs a name. 
    player1_name = None
#I.R: This loop will keep asking for a player name until a non-empty string is entered by the user.  
    while not player1_name:
        player1_name = input("Please enter a valid name for the first player: ").strip()
    players.append(player1_name)
    
    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for the second player: ").strip()
    players.append(player2_name)

    player3_name = None
    if no_of_players > 2:
        while not player3_name:
            player3_name = input("Please enter a valid name for the third player: ").strip()
        players.append(player3_name)

    player4_name = None
    if no_of_players > 3:
        while not player3_name:
            player3_name = input("Please enter a valid name for the fourth player: ").strip()
        players.append(player4_name)
    return players

    
#NT: this checks whether a player has reached the end of the game (the top left corner)
def check_for_a_winner(player, position):
    if position == (0, 1):
        print ("Hooray! " + str(player) + "  has won the game!")
        return True
#NT: this indicates that a winner has been found, and will be used by other parts of the program
#NT: to stop the game or anything additional to be added
    else:
        return False
#NT: if a player has not won, this will tell the program to continue the game


#AW: This function checks if there are valid moves 
def validMoveExists(currentTile):
    valid = False
    if currentTile[0] > 2 and maze[currentTile[0] - 2][currentTile[1]] != " ": #N
        validMoves.append(0)
        valid = True
    if currentTile[1] > 2 and maze[currentTile[0]][currentTile[1] - 2] != " ": #W
        validMoves.append(1)
        valid = True
    if currentTile[0] < mazeSize - 2 and maze[currentTile[0] + 2][currentTile[1]] != " ": #SOUTH
        validMoves.append(2)
        valid = True
    if currentTile[1] < mazeSize - 2 and maze[currentTile[0]][currentTile[1] + 2] != " ": #E
        validMoves.append(3)
        valid = True
    return valid

#AW: This function checks if the direction the player is attempting to move in is valid
def validMove(move, currentPos, visited):
    moveList = ["n","s","e","w"]
    move = move.lower()
    #AW: If the direction entered is not one of "n", "s", "e", or "w", it is invalid
    if move not in moveList:
        print("You must enter a valid direction.")
        return False
    #AW: Based on the attempted direction, the program checks if the tile in that direction is a wall (chr(9608))
    elif (move == "n" and maze[currentPos[0] - 1][currentPos[1]] == chr(9608)) or (move == "s" and maze[currentPos[0] + 1][currentPos[1]] == chr(9608)) or (move == "w" and maze[currentPos[0]][currentPos[1] - 1] == chr(9608)) or (move == "e" and maze[currentPos[0]][currentPos[1] + 1] == chr(9608)):
        print("Invalid direction. You are attempting to move through a wall.")
        return False
    #AW: Again, based on the attempted direction, the program checks if the tile in that direction has already been visited, since no backtracking is allowed.
    elif (move == "n" and (currentPos[0] - 1, currentPos[1]) in visited) or (move == "s" and (currentPos[0] + 1, currentPos[1]) in visited) or (move == "w" and (currentPos[0], currentPos[1] - 1) in visited) or (move == "e" and (currentPos[0], currentPos[1] + 1) in visited):
        print("You have already been on that tile this move. Please pick another direction.")
        return False
    #AW: If none of those conditions have been met, the move must be valid
    else:
        return True

#AW: This function checks if the four surrounding tiles are either walls or have been visited. If so, the player has reached a dead end
def atDeadEnd(currentPos, visited):
    north = maze[currentPos[0] - 1][currentPos[1]]
    south = maze[currentPos[0] + 1][currentPos[1]]
    west = maze[currentPos[0]][currentPos[1] - 1]
    east = maze[currentPos[0]][currentPos[1] + 1]
    if (north == chr(9608) or (currentPos[0] - 1, currentPos[1]) in visited) and (south == chr(9608) or (currentPos[0] + 1, currentPos[1]) in visited) and (east == chr(9608) or (currentPos[0], currentPos[1] + 1) in visited) and (west == chr(9608) or (currentPos[0], currentPos[1] - 1) in visited):
        return True
    return False
    
#AW: This function prints the maze after every move, including the board, snakes and ladders, and player positions
def showMaze(maze, currentPos, positions):
    counter = 0
    start = None
    #AW: The start and end of each ladder is marked by an uppercase letter on the board
    for i in ladders:
        start = i
        maze[i[0]][i[1]] = chr(counter + 65)
        maze[ladders[i][0]][ladders[i][1]] = chr(counter + 65)
        counter += 1

    #AW: The start and end of each snake is marked by an uppercase letter on the board
    counter = 0
    start = None
    for i in snakes:
        start = i
        maze[start[0]][start[1]] = chr(counter + 97)
        maze[snakes[i][0]][snakes[i][1]] = chr(counter + 97)
        counter += 1

    #AW: This adds the players as numbers (1 for player 1, 2 for player 2, etc) to the board based on their positions
    for i in range(len(positions) - 1, -1, -1):
        maze[positions[i][0]][positions[i][1]] = str(i + 1)

    #AW: This prints the entire maze out, tile by tile
    for i in range(mazeSize):
        for j in range(mazeSize):
            print(maze[i][j], end="")
        print()

#AW: The following code randomly generates a maze consisting of walls (chr(9608)) and paths (" ") to be used as the board
maze = []
mazeSize = 21
#AW: All spots are filled with walls first
for i in range(mazeSize):
    row = []
    for j in range(mazeSize):
        row.append(chr(9608))
    maze.append(row)

#AW: Random path from bottom right corner to top left corner is carved out, going only north and west for sake of simplicity
paths = []
x = mazeSize - 2
y = mazeSize - 2
maze[y][x] = " "

#AW: The coordinates of the path tiles as tuples ((y,x) since indexing 2D lists indexes the "rows" first) are added
paths.append((y+1, x))
paths.append((y, x))
current = 0
#AW: Here, the direction (either north or west) is randomly chosen, but the algorithm strongly favours changing the direction of travel in order to avoid long, straight paths and encourage a diagonal path
while x > 1 and y > 1:
    #AW: The chance of the direction changing is 9/10
    direction = random.randint(0,10)
    if direction >= 2:
        direction = abs(current - 1)
    if direction == 0 and y > 2:
        maze[y - 1][x] = " "
        maze[y - 2][x] = " "
        paths.append((y-1,x))
        paths.append((y-2,x))
        y = y - 2
        current = 0
    elif direction == 1 and x > 2:
        maze[y][x - 1] = " "
        maze[y][x - 2] = " "
        paths.append((y,x-1))
        paths.append((y,x-2))
        x = x - 2
        current = 1

#AW: This fills in the remaining spots between the two corners with path tiles
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

#BRANCHING PATHS
#AW: Now that a "solution" path has been carved out, to create the actual maze, there must be branching paths that lead to dead ends
#AW: We opted to generate a maze whose paths do not intersect each other (i.e. the player cannot go in circles)
currentTile = (mazeSize - 2, mazeSize - 2)
pathLength = len(paths)
#AW: Every two tiles on the main diagonal path, the program branches out in random directions
for i in range(1, pathLength, 2):
    validMoves = []
    while True:
        validMoves.clear()
        #AW: If there are still valid directions to move in, a direction (out of the valid ones) is randomly chosen
        if validMoveExists(currentTile):
            direction = validMoves[random.randint(0,len(validMoves)) - 1]
            #AW: 0 corresponds to north, which means decreasing the y-coordinate (the row) by 1 and keeping the x-coordinate the same
            if direction == 0: 
                #AW: The program moves two tiles at a time in one direction since a path must have at least one layer of wall separating it from another path
                maze[currentTile[0] - 1][currentTile[1]] = " "
                maze[currentTile[0] - 2][currentTile[1]] = " "
                #AW: The coordinates of the two path tiles in the north direction that were just carved out are appended to the list of path coordinates
                paths.append((currentTile[0] - 1, currentTile[1]))
                paths.append((currentTile[0] - 2, currentTile[1]))
                #AW: The current tile is updated so that checks using validMoveExists() can be done on the new current position
                currentTile = (currentTile[0] - 2, currentTile[1])
            #AW: 1 corresponds to west, which is keeping the y-coordinate the same and decreasing the x (the column) by 1
            elif direction == 1: 
                maze[currentTile[0]][currentTile[1] - 1] = " "
                maze[currentTile[0]][currentTile[1] - 2] = " "
                paths.append((currentTile[0], currentTile[1] - 1))
                paths.append((currentTile[0], currentTile[1] - 2))
                currentTile = (currentTile[0], currentTile[1] - 2)
            #AW: 2 corresponds to south, which is increasing the y-coordinate by 1 and keeping the x-coordinate the same
            elif direction == 2: 
                maze[currentTile[0] + 1][currentTile[1]] = " "
                maze[currentTile[0] + 2][currentTile[1]] = " "
                paths.append((currentTile[0] + 1, currentTile[1]))
                paths.append((currentTile[0] + 2, currentTile[1]))
                currentTile = (currentTile[0] + 2, currentTile[1])
            #AW: 3 corresponds to east, which is keeping the y-coordinate the same and increasing the x by 1
            else: 
                maze[currentTile[0]][currentTile[1] + 1] = " "
                maze[currentTile[0]][currentTile[1] + 2] = " "
                paths.append((currentTile[0], currentTile[1] + 1))
                paths.append((currentTile[0], currentTile[1] + 2))
                currentTile = (currentTile[0], currentTile[1] + 2)
        #AW: If no valid moves exist, we backtrack to the original tile (on the main solution path) and keep moving through the main path.
        else:
            currentTile = paths[i] 
            break

#AW: This section generates the positions snakes and ladders (which, unlike the original game, cannot be preset since the board is randomized)    
snakes = {}
ladders = {}
#AW: This part generates the ladders. A ratio of 45 path tiles per snake or ladder produces a balanced-looking board
for i in range(len(paths) // 45):
    #AW: Start and end positions of the ladders are randomly generated
    start = random.randint(0, len(paths) - 1)
    end = random.randint(0, len(paths) - 1)
    #AW: Since the point of a ladder is to move the player up and closer to the finish, if the end of the ladder is further down than the start, it is regenerated.
    #AW: Additionally, if the chosen spots already have a ladder there or if the start of the ladder happens to be the start of the board, it is regenerated
    while paths[start][0] <= paths[end][0] or paths[start] in ladders or paths[start] == (mazeSize - 2, mazeSize - 2):
        start = random.randint(0, len(paths) - 1)
        end = random.randint(0, len(paths) - 1)
    #AW: The coordinates of the start and end of the ladders are added to a dictionary as keys and values, respectively
    ladders[paths[start]] = paths[end]
    #maze[paths[start][0]][paths[start][1]] = chr(i+65)
    #maze[paths[end][0]][paths[end][1]] = chr(i+65)

#AW: This part generates the snakes, very similarly to how the ladders are generated
for i in range(len(paths) // 45):
    start = random.randint(0, len(paths) - 1)
    end = random.randint(0, len(paths) - 1)
    #AW: If the end of the snake is higher up than the start, it is regenerated
    while paths[start][0] >= paths[end][0] or paths[start] in snakes or paths[start] in ladders:
        start = random.randint(0, len(paths) - 1)
        end = random.randint(0, len(paths) - 1)
    snakes[paths[start]] = paths[end]


'''
MAIN GAME
'''
welcome_msg()
players = get_player_names()

#AW: Sets the current positions of all players to the beginning of the board
positions = []
visited = []
gameEnd = False
firstMove = True
for i in range(len(players)):
    positions.append((mazeSize - 2, mazeSize - 2))


while not gameEnd:
    firstMove = False
    #AW: This for loop runs number of players times, cycling through each player's turn
    for num in range(len(players)):
        #AW: The current position is set to the position of the player whose turn it is
        currentPos = positions[num]
        maze[currentPos[0]][currentPos[1]] = str(num + 1)
        #AW: The board is shown
        showMaze(maze, currentPos, positions)

        #AW: Prevents players from going back to the (already visited) starting tile on their first move
        if firstMove:
            visited.append((mazeSize - 2, mazeSize - 2)) 
        
        print(players[num] + ", it's your turn. " + str(random.choice(player_turn_text)))
        #AW: The dice is rolled, determining how many moves the player can make
        diceRoll = player_turn()
    
        for i in range(diceRoll):
            move = input("Please enter a direction to move. You can enter either N, S, E or W (case of input does not matter): ")
            #AW: If the input direction is invalid, the user is prompted to enter a direction again
            while not validMove(move, currentPos, visited):
                move = input("Please enter a direction to move. You can enter either N, S, E or W (case of input does not matter): ")
            #AW: If the player is at a dead end (all surrounding tiles are either walls or already visited), the player's remaining moves are forfeited
            if atDeadEnd(currentPos, visited):
                print("You have reached a dead end. Your remaining moves for this turn have been forfeited.")
                visited.clear()
                break
            #AW: Based on the direction ("n", "s", "e", "w"), the board and current position are updated
            elif move.lower() == "n":
                maze[currentPos[0]][currentPos[1]] = " "
                currentPos = (currentPos[0] - 1, currentPos[1])
            elif move.lower() == "s":
                maze[currentPos[0]][currentPos[1]] = " "
                currentPos = (currentPos[0] + 1, currentPos[1])
            elif move.lower() == "w":
                maze[currentPos[0]][currentPos[1]] = " "
                currentPos = (currentPos[0], currentPos[1] - 1)
            else:
                maze[currentPos[0]][currentPos[1]] = " "
                currentPos = (currentPos[0], currentPos[1] + 1)
            visited.append(currentPos)
            positions[num] = currentPos

            #AW: If the played landed on the head of a snake or ladder, their position is adjusted accordingly
            if currentPos in ladders:
                print(random.choice(ladder_jump))
                currentPos = ladders[currentPos]
            elif currentPos in snakes:
                print(random.choice(snake_bite_text))
                currentPos = snakes[currentPos]

            #AW: The board is updated to show the player's position
            maze[currentPos[0]][currentPos[1]] = num + 1
            positions[num] = currentPos
            showMaze(maze, currentPos, positions)

            #AW: If a player has reached the end, the game is finished and the winner is announced.
            gameEnd = check_for_a_winner(players[num], currentPos)
            if gameEnd:
                break
            
        visited.clear()
        positions[num] = currentPos
