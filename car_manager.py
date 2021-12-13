import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_cars()

    def create_cars(self, x=-300):
        for _ in range(10):
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.setx(x=random.randint(x, 600))
            new_car.sety(y=random.randint(-240, 240))
            self.cars.append(new_car)
        self.cars.sort(key=Turtle.xcor, reverse=False)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def increment_speed(self):
        self.move_distance += MOVE_INCREMENT

    def car_hit_turtle(self, player):
        for car in self.cars:
            if player.distance(x=0, y=car.ycor()) < 20 and -30 < car.xcor() < 30:
                return True
        return False
