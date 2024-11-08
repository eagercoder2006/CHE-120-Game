#hi uwu
#NT: to be used for the dice roll
import random
import graphics
#NT: defining how many spaces there are available for the game
board_size=100

#NT: defining where the snakes and ladder are on, and where they will take the players afterwards
#I.R: snakes = {
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

players_position = []

player_turn  = random.randint(1,6)

player_position+= player_turn

