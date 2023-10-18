from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        elif self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)


