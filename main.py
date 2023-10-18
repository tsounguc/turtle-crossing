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
car_manager.create_cars()

game_is_on = True
while game_is_on:
    time.sleep(0.10)
    screen.update()

screen.exitonclick()
