from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # General width is 20 reducing to half
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_xcor = random.randint(-200, 200)
        random_ycor = random.randint(-200, 200)
        self.goto(random_xcor, random_ycor)
