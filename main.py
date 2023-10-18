from turtle import Screen
from car_manager import CarManager
from player import Player
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

# Create a turtle player
turtle_player = Player()
# Listen for the "Up" keypress to move the turtle north.
screen.listen()
screen.onkey(turtle_player.move, "Up")

# Create Car Manager
car_manager = CarManager()

game_is_on = True
index = 0
while game_is_on:
    if index == 5:
        index = 0
        car_manager.create_car()

    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False
    index += 1
    time.sleep(0.10)
    screen.update()

    # Detect when player has reached the other side
    if turtle_player.is_at_finish_line():
        turtle_player.go_to_start()
        car_manager.increase_speed()
screen.exitonclick()
