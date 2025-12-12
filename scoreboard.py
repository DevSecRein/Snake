import turtle as ekans

ALIGNMENT = "center"
FONT = "Calibri"


class Board(ekans.Turtle):
    def __init__(self): #defines the scoreboard as an object
        super().__init__()
        self.score = 0
        with open("./highscore.txt", mode="r") as file: #reads the high score from the txt file
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0,280)
        self.display_scoreboard()
    
    def display_scoreboard(self): #displays the scoreboard
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move = False, align = ALIGNMENT, font=(FONT, 12, "normal"))
    
    def update_score(self): #updates the scoreboard
        self.score += 1
        self.display_scoreboard()
        
    def reset(self): #resets scoreboard after collision
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_scoreboard()

    # def game_over(self):
    #     self.setpos(0,0)
    #     self.write(f"GAME OVER", move = False, align = ALIGNMENT, font=(FONT, 12, "normal"))