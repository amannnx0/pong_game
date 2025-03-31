from turtle import Screen,Turtle
from hitter import Hitter
from  ball import Ball
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)

right_hitter = Hitter((350,0))
left_hitter = Hitter((-350,0))
ball = Ball()



screen.listen()
screen.onkey(right_hitter.go_up,"Up")
screen.onkey(right_hitter.go_down,"Down")
screen.onkey(left_hitter.go_up,"w")
screen.onkey(left_hitter.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()
    ball.move()








screen.exitonclick()