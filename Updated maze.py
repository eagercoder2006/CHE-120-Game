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

def validMove(move, currentPos, visited):
    moveList = ["n","s","e","w"]
    move = move.lower()
    if move not in moveList:
        print("You must enter a valid direction.")
        return False
    elif (move == "n" and maze[currentPos[0] - 1][currentPos[1]] == chr(9608)) or (move == "s" and maze[currentPos[0] + 1][currentPos[1]] == chr(9608)) or (move == "w" and maze[currentPos[0]][currentPos[1] - 1] == chr(9608)) or (move == "e" and maze[currentPos[0]][currentPos[1] + 1] == chr(9608)):
        print("Invalid direction. You are attempting to move through a wall.")
        return False
    elif (move == "n" and (currentPos[0] - 1, currentPos[1]) in visited) or (move == "s" and (currentPos[0] + 1, currentPos[1]) in visited) or (move == "w" and (currentPos[0], currentPos[1] - 1) in visited) or (move == "e" and (currentPos[0], currentPos[1] + 1) in visited):
        print("You have already been on that tile this move. Please pick another direction.")
        return False
    else:
        return True

def atDeadEnd(currentPos, visited):
    north = maze[currentPos[0] - 1][currentPos[1]]
    south = maze[currentPos[0] + 1][currentPos[1]]
    west = maze[currentPos[0]][currentPos[1] - 1]
    east = maze[currentPos[0]][currentPos[1] + 1]
    if (north == chr(9608) or (currentPos[0] - 1, currentPos[1]) in visited) and (south == chr(9608) or (currentPos[0] + 1, currentPos[1]) in visited) and (east == chr(9608) or (currentPos[0], currentPos[1] + 1) in visited) and (west == chr(9608) or (currentPos[0], currentPos[1] - 1) in visited):
        return True
    return False
    

def showMaze(maze, currentPos, positions):
    counter = 0
    start = None
    for i in ladders:
        start = i
        maze[i[0]][i[1]] = chr(counter + 65)
        maze[ladders[i][0]][ladders[i][1]] = chr(counter + 65)
        counter += 1

    counter = 0
    start = None
    for i in snakes:
        start = i
        maze[start[0]][start[1]] = chr(counter + 97)
        maze[snakes[i][0]][snakes[i][1]] = chr(counter + 97)
        counter += 1

    #AW: This adds the players as numbers to the board
    for i in range(len(positions) - 1, -1, -1):
        print(i)
        maze[positions[i][0]][positions[i][1]] = str(i + 1)

    #AW: This prints the entire maze out
    for i in range(mazeSize):
        for j in range(mazeSize):
            print(maze[i][j], end="")
        print()

maze = []
mazeSize = 21
#fill all spots with walls first
for i in range(mazeSize):
    row = []
    for j in range(mazeSize):
        row.append(chr(9608))
    maze.append(row)

#Carve out random path, going only north and west
paths = []
x = mazeSize - 2
y = mazeSize - 2
maze[y][x] = " "

paths.append((y+1, x))
paths.append((y, x))
current = 0
while x > 1 and y > 1:
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

#fill in the remaining spots
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

#BRACHING PATHS

currentTile = (mazeSize - 2, mazeSize - 2)
pathLength = len(paths)
for i in range(1, pathLength, 2):
    validMoves = []
    while True:
        validMoves.clear()
        if validMoveExists(currentTile):
            direction = validMoves[random.randint(0,len(validMoves)) - 1]
            if direction == 0: #NORTH
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
            currentTile = paths[i] #backtrack to original tile
            break

        
snakes = {}
ladders = {}
#Generating ladders
for i in range(len(paths) // 45):
    start = random.randint(0, len(paths) - 1)
    end = random.randint(0, len(paths) - 1)
    print(start, end)
    while paths[start][0] <= paths[end][0] or paths[start] in ladders or paths[start] == (mazeSize - 2, mazeSize - 2):
        start = random.randint(0, len(paths) - 1)
        end = random.randint(0, len(paths) - 1)
    ladders[paths[start]] = paths[end]
    #maze[paths[start][0]][paths[start][1]] = chr(i+65)
    #maze[paths[end][0]][paths[end][1]] = chr(i+65)
print(ladders)
print()


#Generating snakes
for i in range(len(paths) // 45):
    start = random.randint(0, len(paths) - 1)
    end = random.randint(0, len(paths) - 1)
    while paths[start][0] >= paths[end][0] or paths[start] in snakes or paths[start] in ladders:
        start = random.randint(0, len(paths) - 1)
        end = random.randint(0, len(paths) - 1)
    snakes[paths[start]] = paths[end]


'''
MAIN GAME
'''
welcome_msg()
players = get_player_names()
print(players)
#AW: Sets the current positions of all players to the beginning of the board
positions = []
visited = []
gameEnd = False
firstMove = True


for i in range(len(players)):
    positions.append((mazeSize - 2, mazeSize - 2))

while not gameEnd:
    firstMove = False
    for num in range(len(players)):
        currentPos = positions[num]
        maze[currentPos[0]][currentPos[1]] = str(num + 1)
        showMaze(maze, currentPos, positions)
        
        if firstMove:
            visited.append((mazeSize - 2, mazeSize - 2)) #AW: Prevents players from going back to the (already visited) starting tile on their first move
        
        print(players[num] + ", it's your turn. " + str(random.choice(player_turn_text)))
        diceRoll = player_turn()
    
        for i in range(diceRoll):
            move = input("Please enter a direction to move. You can enter either N, S, E or W (case of input does not matter): ")
            while not validMove(move, currentPos, visited):
                move = input("Please enter a direction to move. You can enter either N, S, E or W (case of input does not matter): ")
            if atDeadEnd(currentPos, visited):
                print("You have reached a dead end. Your remaining moves for this turn have been forfeited.")
                visited.clear()
                break
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
            
            if currentPos in ladders:
                print(random.choice(ladder_jump))
                currentPos = ladders[currentPos]
            elif currentPos in snakes:
                print(random.choice(snake_bite_text))
                currentPos = snakes[currentPos]
            maze[currentPos[0]][currentPos[1]] = num + 1
            print(currentPos, positions)
            showMaze(maze, currentPos, positions)

            gameEnd = check_for_a_winner(players[num], currentPos)
            
        visited.clear()
        positions[num] = currentPos
