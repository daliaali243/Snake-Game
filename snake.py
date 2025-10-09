from turtle import  Turtle,Screen
import random
class Snake:
    def __init__(self):
        self.position=[(-20,0),(0,0),(20,0)]
        self.turtles=[]

        self.create_snake()
        self.snake_head = self.turtles[-1]
    def create_snake(self):
        for i in range(len(self.position)):
            new_turtle=Turtle('square')
            new_turtle.color('black')
            new_turtle.penup()
            new_turtle.goto(self.position[i])
            self.turtles.append(new_turtle)
    def move_turtle(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.snake_head.forward(20)
    def up(self):
        self.snake_head.setheading(90)
    def down(self):
        self.snake_head.setheading(270)
    def left(self):
        self.snake_head.setheading(180)
    def right(self):
        self.snake_head.setheading(0)
    def extend(self):
        new_segment=Turtle('square')
        new_segment.color('black')
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0,new_segment)