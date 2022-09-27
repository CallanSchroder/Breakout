import time
from turtle import Turtle, Screen
import random
from gear import Ball, Bats
from walls import Walls
from scoreboard import Scoreboard
from deathCounter import Deaths


screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("MY FIRST Break Out Game")
screen.listen()
screen.tracer(0)
timesleep = 0.1


colors=["yellow", "gold", "orange", "red", "maroon",
        "violet", "magenta", "purple", "navy", "blue",
        "skyblue", "cyan", "turquoise", "lightgreen",
        "green", "darkgreen", "chocolate", "brown",
        "gray", "white"]


RANDOM_Y = random.randint(150, 280)
RANDOM_STRETCH = [3,4,5]
FONT = ("Courier", 24, "normal")


bat = Bats()
screen.onkey(bat.go_left,"a")
screen.onkey(bat.go_right,"d")
deaths = Deaths()

died = 0
wall = Walls()
ball = Ball()
wall.Setup()
score = Scoreboard()
game_on = True

while game_on: #playing the game
    score.clear()
    deaths.clear()
    score.show_score()
    deaths.show_deaths()
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280: #topbounce
        ball.hit()
    if ball.xcor() < -380 or ball.xcor() > 380:  # hit_side_walls
        ball.bounce()
    if ball.ycor() < -235 and ball.distance(bat) < 40: #hit_with_bat
        ball.hit()
    if ball.ycor() < -260:      #if ball goes too far down
        deaths.death()
        ball.goto(0,0)
        ball.move()
        died += 1
    elif died == 3:  #end game show final score
        score.final_score()
        game_on = False
    for block in wall.all_walls:  #hit the brick logic
        if ball.distance(block) <30 and ball.ycor() == block.ycor():   #if ball comes from side hit and change x to *-1
            ball.bounce()
            block.goto(x=1000, y=1000)
            score.destroyed()
        elif ball.distance(block)<40:
            # ball.bounce()
            ball.hitwall()
            block.goto(x=1000,y=1000)
            score.destroyed()

#issues - ball glitches with bat
# ball hitting bricks from side doesnt change x direction




#if y value of ball is >/< y value of brick

screen.exitonclick()