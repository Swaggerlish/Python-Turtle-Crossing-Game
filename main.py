import time
from turtle import Screen, Turtle
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player(STARTING_POSITION)
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.hideturtle()
car_manager.hideturtle()



screen.listen()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.end_game()
    if player.ycor() > 280:
        player.reset()
        car_manager.increase_speed()
        scoreboard.level_up()





screen.exitonclick()