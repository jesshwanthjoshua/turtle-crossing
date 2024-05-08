from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.leo = Turtle("turtle")
        self.leo.color("black")
        self.leo.penup()
        self.leo.setheading(90)
        self.start_position()

    def move_player(self):
        self.leo.forward(MOVE_DISTANCE)

    def start_position(self):
        self.leo.goto(STARTING_POSITION)

