from cs1robots import *

create_world(streets=10,avenues=1)

hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def up_and_down():
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    for i in range(2):
        turn_right()
        if hubo.front_is_clear():
            hubo.move()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()

up_and_down()
while hubo.front_is_clear():
    hubo.move()
    if hubo.front_is_clear():
        up_and_down()