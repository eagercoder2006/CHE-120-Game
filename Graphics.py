import pygame, sys
from pygame.locals import * 
import turtle

Display_Screen=pygame.display.set_mode((1000, 1000)) #IA: Define the dimensions for the graphics window.
pygame.init()


from random import randrange
from turtle import *

from freegames import square, vector

coloursturtle = ["red", "yellow", "blue", "orange"]
colourspygame = [(0,0,250), (250,0,0), (0,250,0), (0,50,50), (100,100,0), (70,60,50), (30,40,10)]

#food = vector(0, 0) #IA: Sets food to the vector psotion of (0,0)


#def change(x, y):
    #"""Change snake direction."""
    #aim.x = x #IA: Redifines the value of x to whatever is inputted as x in the arguments
    #aim.y = y #IA: Redifines the values of y to whatever is inputted as x in the arguments
#IA: This part of the code will not be useful for our game as our snakes do not move but rather are stationnary

for items in snakes:
    pygame.draw.aaline(Display_Screen,colourspygame[5], items, snakes[items]) #IA: This will draw the snakes as a coloured line from its initial position to it's finale inteded position (where it will take the player when they land on it's head)

for items in ladders:
    pygame.draw.aaline(Display_Screen,colourspygame[4], items, ladders[items])#IA: Similarly, this will draw a differently coloured line for the ladders starting at the position that is specified as its key and it's final position will be the value corresponding to the key.


for items in range(len(currrent_positions)): #IA: Iterates through all the items that have the index in the range of the length of the list named current_positions.
    pygame.draw.circle(Display_Screen,colourspygame[items], (0,0),10)
    

def move():
    """Move snake forward one segment."""
    #head = snakes1[-1].copy() #IA: Copy the last vector in the list of vectors given to the variable head that represents the front part of the snake.
    ##IA: This code for when the snakes and ladders were not randomly generated (this section was below the inside_snake() and inside_ladder() functions## 
    for i in range(len(current_positions)):
        #if (dice_roll()+current_positions[i]-1)%10 == 0:
         #  circle.move(0,10)
        #elif (dice_roll()+current_positions[i])%10 !=0:
            #if (dice_roll()+current_positions[i]) < 10:
                #horizontal_move=((dice_roll()+current_positions[i])%10)*10
            #else:
                #horizontal_move=((dice_roll()+current_positions[i])%10)*-10 #IA: A problem here is that i do not knwo if this .move() function is coordinate based or if it moves on the basis of vectors.
           #vertical_move=(dice_roll+current_position-horizontal_move)*10
           #circle_move(horizontal_move, vertical_move)
        #if inside_snake(circle):
         #   a = snakes1.find((circle.xcircle.y)) #IA: Define a new variable a as the addition of the values of the x and y coordinates of the circle. snake was the name of the list containing the number of the tiles that would have the snakes on them.
          #  circle.move(aim1[a]) #IA: Moves the head of the snake to the aim vector position. aim1 was the name of the list containing the values that the circle would be brought to when landing on a snake. The original code for the snake game had this part as, but the snake was the one moving. I wanted to change the variable that the vector position will be changed to be the circle. 
        #elif inside_ladder(circle):
         #   a = ladders.find((circle.x + circle.y))
          #  circle.move(aim2[a])
    ##IA: This part of the code is for when our snakes and ladders were randomly generated##
        if (dice_roll+current_positions[i])%10!=0: #IA: This will verify if the dice roll result has made the player move to a different row (since the rows in a traditional snakes and ladders game are of legnth 10). Yet, I realize that this is not needed for our game, since we have a maze and the player can movein any direction depending on their chioce.
            circle[i].move(dice_roll,0) #IA: move the corresponding circle by the rolled value.
            Dispaly_Screen.update() #IA: Update the screen.
        else:
            x_value=(dice_roll+current_positions[i])%10 #IA: Calculate the amont of squares that the circle should move horizontally based on its current position and rolled value.
            x_value=(dice_roll+current_positions[i]-x_value)/10 #IA: Calculate the amont of squares that the circle should move vertically based on its current position and rolled value.
            circle[i].move(x_value,y_value) #IA: Move the circle
            Dispaly_Screen.update()

def inside_snake(head):#IA: This function originally verifies if the head is outside of the board. We will use this to check if the circle that represents each character is on the snakes.
    #"""Return True if head inside boundaries."""
    #return -200 < head.x < 190 and -200 < head.y < 190 #IA: Returns true if the coordinates of the head is in between (-200,-200) and (190,190)
    for i in range(len(current_positions)): #IA: This loop itirates through the current positions of players.
        if current_positions[i] in snakes: #IA: if the position of the player is the same as one of the keys of the dictionnary named "snakes", if the player is on the head of a snake, then it is moved to that keys corresponding value.
            circle[i].move(snakes[current_positions[i]]) #IA: Would move snake to the intended position based on the saved value in snakes)

def inside_ladder(head): #IA: Verify the psoition of of each player and determine if the player is at the start of a ladder.
    for i in range(len(current_positions)): #IA: The loop should itirate through the whole list.
        if current_positions[i] in ladders: #IA: If the position of the player is at the bottom of the ladder, the player will be moved to the psotion saved as the value in the dictionnary named "ladders".
            circle.move(ladders[current_positions[i]]) 
            Dispaly_Screen.update()
        else:
            circle.move(dice_roll)
            Dispaly_Screen.update()


    #if not inside(head) or head in snake: #IA: Verifies if the vector that head has at that point is in the set of vectors in snake or if it our of the boudaries. This is part of the original snakes game code.
        #square(head.x, head.y, 9, 'red') #IA: If one of these conditions is filled, then there will be a square coloured at the psotion of the head with a 9x9 dimension and it will be coloured red.
        #update() #IA: This updates the drawing of before.
        #return

    #snake.append(head) IA: This adds the new vector set to the value of head to the collection of vectors named snake.

    #if head == food: #IA; This is part of the original snakes game code. It verifies if the head of the snakes is at the coordinate of the food. If yes, it prints the legth of the snake (which is a list with the vectors of eahc square composing the snake).
        #print('Snake:', len(snake))
        #food.x = randrange(-15, 15) * 10 #IA: This line randomly assigns a new coordinate to the food.
        #food.y = randrange(-15, 15) * 10
    #else:
        #snake.pop(0) #IA: If the snakes head is not at the same place as the food, then we do not add this square to the list containing the vectors of the position of the squares making up the snake.

    #clear()

    #for body in snake:
        #square(body.x, body.y, 9, 'black') #IA: colours the snake black and makes its body composed of squares by using suqare(). This loop itirates through all the elements in the list named snake and makes a square for each position.

    #square(food.x, food.y, 9, 'green') #Ia: Similarly to the body of the snake, this shapes the food as a circle and colours it green.
    #update()
    #ontimer(move, 100)


#setup(420, 420, 370, 0) #IA: This sets up the size of the window that will display the graphics and its position.
#hideturtle() #IA: Hides turtle (which does the drawing), which can speed up the drawing.
#tracer(False) #IA: This tells turtle to not enable turtle animations for drawing.
#listen() #IA: This sets focus to the display screen, this is so that it pays attention to the keys hit.
#onkey(lambda: change(10, 0), 'Right') #IA: applies the change function to the snake when the right key is hit
#onkey(lambda: change(-10, 0), 'Left') #IA: applies the change function to the snake when the left key is hit
#onkey(lambda: change(0, 10), 'Up') #IA: applies the change fucntion to the snake when the up key is hit
#onkey(lambda: change(0, -10), 'Down') #IA: applies the change function to the snake when the down key is hit
#move() #IA: Runs the move function
#done()
if playAgain()==False: #IA: This verifies if the player of the snakes and ladders game has decided to play again. If not, the screen
    Display_Screen.QUIT
pygame.quit() #IA: Shuts down the displayed screen