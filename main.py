import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cm = CarManager()
sre = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(player.move_player, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cm.create_car()
    cm.move_cars()

    for cars in cm.cars_list:
        if cars.distance(player.leo) <= 20:
            game_is_on = False
            sre.game_over()

    if player.leo.ycor() >= 280:
        player.start_position()
        cm.speed_up_car()
        sre.level += 1
        sre.level_up()

screen.exitonclick()
