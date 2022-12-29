import random
from secrets import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.speed_value = STARTING_MOVE_DISTANCE
        
    
    def create_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.seth(180)
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(x=310, y=random.randint(-250, 250))
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.fd(self.speed_value)
            if car.xcor() < -330:
                car.clear()
                car.ht()
                self.all_cars.remove(car)
                del car
    
    def increase_speed(self):
        self.speed_value += MOVE_INCREMENT