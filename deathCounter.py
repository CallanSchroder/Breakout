from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Deaths(Turtle):
    def __init__(self):
        super(Deaths, self).__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(200, 270)
        self.score = 0

    def show_deaths(self):
        self.write(f"DEATHS:{self.score}",align= 'left', font= FONT )

    def death(self):
        self.score += 1