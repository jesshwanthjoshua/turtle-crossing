from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars_list = []

        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        num = random.randint(1, 6)

        if num == 1:
            ralph = Turtle("square")
            ralph.color(random.choice(COLORS))
            ralph.penup()
            ralph.shapesize(stretch_len=2)
            ralph.setheading(180)
            y = random.randrange(-250, 260, 10)
            ralph.setpos(280, y)
            self.cars_list.append(ralph)
            print(f"new car = {ralph.position()}")

    def move_cars(self):
        for cars in self.cars_list:
            cars.forward(self.car_speed)

    def speed_up_car(self):
        self.car_speed += MOVE_INCREMENT