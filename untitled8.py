#hi uwu
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
#COMMENTS
player_turn_text= [ "It's your turn.", "MOVE!", "Please proceed.", "You ready to win this?", "Let's Go!"]
snake_bite_text= ["Ouch!", "whomp whomp", "oh no", "did that hurt?", "Slide you later!"]
ladder_jump= ["Woop woop", "YAY", "Climb up!", "You're closer to the end"]

#COMMENTS
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

#COMMENTS
def get_player_names():
    player1_name = None
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

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name, player3_name, player4_name
players_position = []

player_turn  = random.randint(1,6)
if player_turn = 6:
    
player_position+= player_turn

