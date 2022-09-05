from turtle import Turtle
import random

POINTS = [-270, -260, -250, -240, -230, -220, -210, -200, -190, -180, -170, -160, -150, -140, -130, -120, -110,
          -100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130,
          140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.choice(POINTS)
        random_y = random.choice(POINTS)
        self.goto(random_x, random_y)


