import time
from turtle import Screen
from player import FINISH_LINE_Y, Player
from car_manager import CarManager
from scoreboard import Scoreboard

# list_of_cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.up, "Up")

scoreboard.write_level()

# tick = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #Make new car every 6 time the loop runs
    car_manager.create_car()
    car_manager.move()
    # tick += 1
    # if tick == 6:
    #     car = CarManager()
    #     list_of_cars.append(car)
    #     tick = 0
    #Move every car in the same time...
    # for i in list_of_cars:
    #     if i.xcor() > -330:
    #         i.move()
            
    #Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    #         if player.distance(i) < 15:
    #             scoreboard.game_over()
    #             game_is_on = False
    #     else:
    #         #...and remove if outside of screen
    #         i.clear()
    #         i.ht()
    #         list_of_cars.remove(i)
    #         del i

    #Detect when players reaches finish line
    if player.ycor() > FINISH_LINE_Y:
        player.res_position()
        scoreboard.level_up()
        car_manager.increase_speed()

screen.exitonclick()