import turtle as ekans

STARTING_PIECE_COUNT = 3
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():
    def __init__(self): #defines the snake
        self.piece_coord = []
        self.snake_creation()
        self.head = self.piece_coord[0]
        self.head.shape("circle") #make the head a different shape from the rest of the body

    def snake_creation(self): #creates the start of game body and positions the pieces("piece")
        for block in range(STARTING_PIECE_COUNT):
            piece = ekans.Turtle("square")
            piece.color("white")
            piece.penup()
            piece.setpos(x= (block*-20), y=0)
            self.piece_coord.append(piece)
    
    def grow(self): #adds to body by placing another piece where the tail was at the time of "food collision"
        piece = ekans.Turtle("square")
        piece.color("white")
        piece.penup()
        piece.goto(self.piece_coord[-1].position())
        self.piece_coord.append(piece)

    #defines the rules for movement
    def movement(self):
        for block in range(len(self.piece_coord)-1, 0, -1):
            new_x = self.piece_coord[block-1].xcor()
            new_y = self.piece_coord[block-1].ycor()
            self.piece_coord[block].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    #defines the rules for resetting the snake
    def reset(self):
        for piece in self.piece_coord:
            piece.goto(1000,1000)
        self.piece_coord.clear()
        self.snake_creation()
        self.head = self.piece_coord[0]
        self.head.shape("circle")
        

