import turtle as ekans
import random

ekans.colormode(255)
FLAPPLE_COLOR = (247,221,126)

class Food(ekans.Turtle):
    def __init__(self): #defines the snake food as an object by modifying a "turtle" object into circle
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color(FLAPPLE_COLOR)
        self.speed("fastest")
        self.refresh()
    
    def refresh(self): #sets the snake food to appear in a random position on screen
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setpos(random_x, random_y)