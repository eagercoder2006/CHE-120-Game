#Israelle Azilinon:IA
#Ishita Rajan: I.R
#Nicole Trinidad: NT
#Amy Wang: 

#NT: to be used for the dice roll
import random
#NT: defining how many spaces there are available for the game
board_size=100

#NT:defines a dictionary where, the keys represent the starting positions of snakes/ladders
#NT:and the values represent the ending positions after sliding down the snake or climbing a ladder.
snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    85: 59,
    90: 48,
    99: 63
}

ladders = {
  1: 38,
  8: 30,
  21: 42,
  28: 76,
  50: 67,
  71: 92,
  80: 93,
  83: 95
}
#NT: simple print statements that will be used to make the game more interactive, these will be randomly printed at
#NT: the beginning of each turn, or when a player encounters a snake or ladder
player_turn_text= [ "It's your turn.", "MOVE!", "Please proceed.", "You ready to win this?", "Let's Go!"]
snake_bite_text= ["Ouch!", "whomp whomp", "oh no", "did that hurt?", "Slide you later!"]
ladder_jump= ["Woop woop", "YAY", "Climb up!", "You're closer to the end"]

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


#I.R: This function will take user input for the names of the players. 
def get_player_names():
    
#I.R: This line says that the variable player1_name initially does not have a value, as it will get filled when the user inputs a name. 
    player1_name = None
    
#I.R: This loop will keep asking for a player name until a non-empty string is entered by the user.  
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()
        
 #NT: to make player 3 optional   
    player3_name = input("Please enter a valid name for third player: ").strip()
 #NT:the str.strip() is used to remove any excess whitespace infront or behind the user's input
    if not player3_name:
#NT: this checks whether the player3_name is an empty string or a None value
#NT: if the name is empty, meaning no input was provided, the condition will return True
         player3_name = None
         
#NT: to make player 4 optional, exact logic was used for player4_name that was used in player3_name
    player4_name = input("Please enter a valid name for fourth player: ").strip()
    if not player4_name:
        player4_name= None

#I.R This line will return the four inputed player names that have been inputed by the user.
    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name)
    if player3_name: 
#NT: checks is player3_name is not None, and if true, it will print the player's name as part of the match condition
        print(" and" + player3_name)
    if player4_name: #NT: same logic as above
        print (" and" + player4_name)
    print("\n")
    return player1_name, player2_name, player3_name, player4_name

#I.R: The dice roll
def player_turn():
    dice_roll= random.randint(1,6)
#NT: python's random module to generate a random integer, and the arguments specify that the random
#NT: number should be between 1 and 6 (inclusive)
    print ("You got a " + str(dice_roll))
    return dice_roll
#NT: allows us to use this value in other parts of the program, like updating a player's position in the game

#NT: this checks whether a player has reached the end of the game, and since the max player position can be the size of the board
#NT: this is why we set the position equal to the board size
def check_for_a_winner(player_name, position):
    if position== board_size:
        print ("Hooray! " + str (player_name) + "  has won the game!")
        return True
#NT: this indicates that a winner has been found, and will be used by other parts of the program
#NT: to stop the game or anything additional to be added
    else:
        return False
#NT: if a player has not won, this will tell the program to continue the game

def moving_positions(current_value, dice_roll):
    old_value = current_value
#NT: stores the player's current position (current_value) in the variable old_value to be later used to
#NT: calculate how many spaces the player has moved and show an error if the player has exceeded the board size
    current_value += dice_roll
#NT: this is what updates the player's position by adding the dice_roll to the current_value
#NT: and the new current_value represents the player's new position after their turn

    if current_value > board_size:
#NT: this checks if the player's new position exceeds the total number of spaces on the baord
        print ("You must move exactly " + str (board_size - old_value) + " of spaces in order to win.")
        return old_value
#NT: if this is true, the player if returned to their original position, since in our rules, it must be an exact roll to win


    if current_value in snakes:
#NT: checks if the player' new position corresponds to a snake's head (checks is current_value is in snakes dictionary)
        final_position= snakes.get(current_value) 
#NT: the function retrieves the final position from the dictionary using snakes.get(current_value), providing the position the snake takes the player
        print(random.choice(snake_bite_text))
#NT: this randomizes the texts that will be shown to alert player about the snake they landed on

    elif current_value in ladders:
        final_position=ladders.get(current_value)
        print(random.choice(ladder_jump))
#NT: this also uses the same logic as the if statement for snakes above, but uses the ladder dictionary and other functions related to ladders rather than snakes

    else:
        final_position=current_value
#NT: if the player's new position is neither a snake nor a ladder, the final position is simply the current position, and no special event occurs
        print(str(board_size-final_position) + " more spaces to go!")
    return final_position
#NT: returns the player's final position


def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
#NT: prompts user whether they want to play again, and checks the input for yes, or even just y, where if its one of these options it will return True


#MAIN BODY OF CODE  
def start_game():      
    welcome_msg()
    player1_name, player2_name,player3_name,player4_name = get_player_names()

    current_positions = [0, 0, 0, 0]
#NT: the stores the current positions of all players on the board, and are initially set to 0
    players=[player1_name, player2_name, player3_name, player4_name]
#NT: stores the player names
    flag = False #Keeps track of whether the game has ended, and is initially set to False, meaning there is no winner
    dice_value = 0
#NT: a variable to store the dice value rolled by the players, will be updates after each player's turn

#NT: main game loop
    while not flag:
#NT: this loop will iterates over each player allowing each player to take a turn in order
        for i in range(4):
            if players[i]is None:
#NT: checks is a player's name is None, and if true, this player will be skipped 
                continue
            if players[i]:
                input('\n' + players[i] + ":" + random.choice(player_turn_text) + " Hit enter to start your turn")
#NT: prompts current players with a random text to alert them of their turn  
#NT: the input function waits for the player to hit enter to start their turn         
                dice_value = player_turn() #Rolls the dice
                current_positions[i] = moving_positions(current_positions[i], dice_value) #Updates current position according to dice rolled
                if check_for_a_winner(players[i], current_positions[i]): #checks if someone won
                    flag = True
#NT: if a winner is found, flag returns true and will break out of the loop and end the game
                    break
    
        if flag:
#NT: checks whther the user wants to play again using playAgain(), if player says no, it will exit the game
            if playAgain():
                start_game()
        
   
#NT: function contains the entire game loop, and calls upon itself recursively if another round will be played, and ensures that the
#NT: next round restarts with cleared data from the last game 
start_game()
    
    


import turtle

scr= turtle.Screen()
scr.bgcolor("green")
scr.title("Snakes and ladders board")
tur=turtle.Turtle()

size=50

def square(x):
    for i in range(4):
        tur.forward(x)
        tur.right(90)
initial_position=tur.pos()

for i in range(10):
    tur.penup()
    tur.goto(initial_position+(-10,(size*i))-10)
    tur.pendown()
    tur.seth(0)
    for j in range(10):
        tur.begin_fill()
        tur.fillcolor("orange")
        square(size)
        tur.forward(size)
        tur.end_fill()
        
tur.penup()
tur.goto(initial_position + (-10,size))
tur.pendown()
tur.width(20)
for l in range(10):
    square(size*10)

tur.penup()
tur.pos()

tur.done()
