from cs1robots import *

load_world("worlds/harvest4.wld")

hubo = Robot()

hubo.set_trace('blue')
#hubo.set_pause(0.1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def turn_arround_1():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def turn_arround_2():
    turn_right()
    hubo.move()
    turn_right()

def pick_and_move():
    while hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()

def zig_zag(cnt):
    col = 0
    while hubo.front_is_clear():
        pick_and_move()
        col += 1
    while hubo.on_beeper():
        hubo.pick_beeper()
    turn_arround_1()
    for i in range(col):
        pick_and_move()
    while hubo.on_beeper():
        hubo.pick_beeper()
    if cnt < 2:
        turn_arround_2()

hubo.move()

for i in range(3):
    zig_zag(i)