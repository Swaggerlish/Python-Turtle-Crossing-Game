from turtle import Turtle
from player import Player
import random
from scoreboard import Scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed_increase = MOVE_INCREMENT



    def create_car(self):
        random_speed = random.randint(1, 6)
        if random_speed == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)



    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed_increase)
    def increase_speed(self):
        self.speed_increase += 10





