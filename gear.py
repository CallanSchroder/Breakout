from turtle import Turtle
import random

random_angle = (-0.95, -1)

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.speed(7)
        self.color("white")
        self.ball_speed = 0.005
        self.penup()
        self.x_move = 4
        self.y_move = 4

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
       self.x_move *= -1

    def hitwall(self):
        self.y_move*=-1
        # self.ball_speed *= 0.9

    def hit(self):
        self.y_move *= random.choice(random_angle)

class Bats(Turtle):
    def __init__(self):
        super(Bats, self).__init__()
        self.goto(x=0, y=-260)
        self.penup()
        self.color("White")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed("fastest")

    def go_left(self):
        new_x = self.xcor() - 60
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 60
        self.goto(new_x,self.ycor() )