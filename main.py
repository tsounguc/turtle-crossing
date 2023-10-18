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
    index += 1
    time.sleep(0.10)
    screen.update()



screen.exitonclick()
