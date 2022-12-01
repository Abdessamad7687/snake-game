from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

from snake import Snake
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard() 

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
  
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or  snake.head.ycor() >280 or  snake.head.ycor() < -280:
        scoreboard.game_over()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()