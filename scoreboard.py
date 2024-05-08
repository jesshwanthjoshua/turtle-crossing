from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 1
        self.shape("circle")
        self.hideturtle()
        self.penup()
        self.setpos(-260, 260)
        self.color('black')
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f"Level = {self.level}", False, 'left', FONT)

    def game_over(self):
        self.setpos(0, -30)
        self.write(f"Game Over", False, 'left', FONT)
