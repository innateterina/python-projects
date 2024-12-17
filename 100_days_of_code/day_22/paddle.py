from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
