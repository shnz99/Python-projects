import time
import turtle as t
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
      
    #Detect if the ball goes beyond paddles
    if ball.xcor() > 330:
        ball.reset_position()
        scoreboard.l_point()

        # user_1_score += 1
    elif ball.xcor() < -330:
        ball.reset_position()
        scoreboard.r_point()

        # user_2_score += 1
        
        
screen.exitonclick()
