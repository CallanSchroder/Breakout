from turtle import Turtle
import random
colors=["yellow", "gold", "orange", "red", "maroon",
        "violet", "magenta", "purple", "navy", "blue",
        "skyblue", "cyan", "turquoise", "lightgreen",
        "green", "darkgreen", "chocolate", "brown",
        "gray", "white"]

class Walls(Turtle):
    def __init__(self):
        super(Walls, self).__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.speed("fastest")
        self.all_walls=[]


    def Setup(self):
        RANDOM_X = -280
        BACK_Y = 250
        for n in range (5):
            if RANDOM_X > 340:
                RANDOM_X=-360
            else:
                RANDOM_X=-360
            if BACK_Y < 120:
                BACK_Y = 250
            else:
                BACK_Y -= 30
            color = random.choice(colors)
            for wall in range (13):
                new_wall=Turtle("square")
                new_wall.penup()
                new_wall.speed("fastest")
                new_wall.color(color)
                new_wall.shapesize(stretch_wid=1, stretch_len=2 )
                new_wall.goto(x=RANDOM_X,y=BACK_Y)
                RANDOM_X += 50
                self.all_walls.append(new_wall)

    def Go(self):
        for wall in self.all_walls:
            if wall.xcor() == 0 and wall.ycor() == 0:
                wall.goto(x=1500, y=1500)