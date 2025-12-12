import turtle as ekans
import snakebody
import food
import scoreboard

import time

screen = ekans.Screen() #calls the in built turtle function
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Big Black Cobra")
screen.tracer(0) #turtle drawing function. Forgot why this needs to be here

arbok = snakebody.Snake() #calls the snake function to build the initial snake. I will call this instance of the object "arbok"
flapple = food.Food() #places food on the board
buzzer = scoreboard.Board() #displays the scoreboard

screen.listen() #sets a "listener" for the screen for screen to listen for keyboard inputs

#sets arbok to call the directional functions from snakebody.py when there is a keyboard input for the keys in the quotation marks
#use wasd for second player if I ever choose to build out a two player function
screen.onkey(arbok.up, "Up")
screen.onkey(arbok.left, "Left")
screen.onkey(arbok.down, "Down")
screen.onkey(arbok.right, "Right")

game_over = False

while not game_over:
    screen.update() #sets screen to refresh so it displays objects moving around on screen
    time.sleep(.1) #since the original settings are too fast, the screen should refresh at 1/10th speed
    arbok.movement()

    #Eat Food
    if arbok.head.distance(flapple) < 15:
        flapple.refresh()
        arbok.grow()
        buzzer.update_score()

    #Detect collision with wall
    if arbok.head.xcor() > 290 or arbok.head.xcor() < -290 or arbok.head.ycor() > 290 or arbok.head.ycor() < -290:
        # game_over = True
        buzzer.reset()
        arbok.reset()

    #Detect collision with tail
    for segment in arbok.piece_coord[1:]:
        if arbok.head.distance(segment) < 10:
            # game_over = True
            buzzer.reset()
            arbok.reset()


screen.exitonclick()