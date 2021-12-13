import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    if car_manager.cars[-1].xcor() < 300:
        car_manager.create_cars(x=300)
    if player.cleared_level():
        player.reset_position()
        car_manager.increment_speed()
        scoreboard.level_up()
    if car_manager.car_hit_turtle(player):
        time.sleep(0.1)
        screen.update()
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
