#Israelle Azilinon:
#Ishita Rajan: I.R
#Nicole Trinidad: NT
#Amy Wang: 

#NT: to be used for the dice roll
import random
import turtle
#NT: defining how many spaces there are available for the game
board_size=100

#NT: defining where the snakes and ladder are on, and where they will take the players afterwards
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
#NT: simple print statements that will be used to make the game more interactive
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
        
    player3_name = None
    while not player3_name:
        player3_name = input("Please enter a valid name for second player: ").strip()
    
    player4_name = None
    while not player4_name:
        player4_name = input("Please enter a valid name for second player: ").strip()

#I.R This line will return the four inputed player names that have been inputed by the user.
    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "' and '" + player3_name + "' and '" + player4_name + "'\n")
    return player1_name, player2_name, player3_name, player4_name



players_position = []

#I.R: The dice roll
def player_turn():
    dice_roll= random.randint(1,6)
    print ("You got a " + str(dice_roll))
    return dice_roll

#NT: this checks whether a player has reached the end of the game, and since the max player position can be the size of the board
#NT: this is why we set the position equal to the board size
def check_for_a_winner(player_name, position):
    if position== board_size:
        print ("Hooray!" + str (player_name) + "  has won the game!")
        
#I.R: This tells the player whether to move up or down depending on if they landed on a snake or on a ladder.
if position in snakes:
        print(f"{player} encountered {'a ladder' if position < board[position] else 'a snake'}!")

def start_game():
    welcome_msg()
    player1_name, player2_name,player3_name,player4_name = get_player_names()

    player1_current_position = 0
    player2_current_position = 0
    player3_current_position = 0
    player4_current_position = 0
