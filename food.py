from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.appear()
    def appear(self):
        random_x = random.randint(-360, 360)
        random_y = random.randint(-360, 350)
        self.goto(random_x, random_y)