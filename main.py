from turtle import Screen
from hitter import Hitter
from  ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)

right_hitter = Hitter((350,0))
left_hitter = Hitter((-350,0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(right_hitter.go_up,"Up")
screen.onkey(right_hitter.go_down,"Down")
screen.onkey(left_hitter.go_up,"w")
screen.onkey(left_hitter.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_hitter) < 50 and ball.xcor() > 320 or ball.distance(left_hitter)<50 and ball.xcor()<-320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -350:
        ball.reset_pos()
        scoreboard.r_point()








screen.exitonclick()