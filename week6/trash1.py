from cs1robots import *

load_world('worlds/trash2.wld')

hubo = Robot()
hubo.set_trace('blue')
def turn_right():
    for i in range(3):
        hubo.turn_left()

def pick_and_move():
    while hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()

def turn_arround():
    for i in range(2):
        hubo.turn_left()

def trash_to_garbage_can():
    hubo.move()
    while hubo.carries_beepers():
        hubo.drop_beeper()
    turn_arround()
    hubo.move()
    hubo.turn_left()

def return_1():
    while hubo.front_is_clear():
        hubo.move()
    turn_right()


while hubo.front_is_clear():
    pick_and_move()
while hubo.on_beeper():
    hubo.pick_beeper()


turn_arround()
return_1()
trash_to_garbage_can()   
