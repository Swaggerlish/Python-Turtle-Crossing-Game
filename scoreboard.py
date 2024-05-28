from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.update()

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



    def update(self):
        self.clear()
        self.penup()
        self.goto(0, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def level_up(self):
        self.level += 1
        self.update()





