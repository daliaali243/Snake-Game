
from turtle import Turtle,Screen
import time

import snake
from food import Food
from snake import Snake
from score import Score
window = Screen()
window.tracer(0)
window.setup(width=800, height=800)
Snake=Snake()
food=Food()
score=Score()
game_on=True
while game_on:

     Snake.move_turtle()
     time.sleep(0.09)
     window.listen()
     window.onkey(Snake.up,'Up')
     window.onkey(Snake.down,'Down')
     window.onkey(Snake.left,'Left')
     window.onkey(Snake.right,'Right')
     if Snake.snake_head.distance(food) < 15:
         food.appear()
         Snake.extend()
         score.increase_score()
     if Snake.snake_head.xcor()>360 or Snake.snake_head.xcor()<-380 or Snake.snake_head.ycor()>380 or Snake.snake_head.ycor()<-300:
         game_on=False
         score.game_over()
     for segment in Snake.turtles[0:-1]:
        if segment.distance(Snake.snake_head) < 10:
            game_on=False
            score.game_over()
     window.update()
window.exitonclick()