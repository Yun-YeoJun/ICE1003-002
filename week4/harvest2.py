from cs1robots import *

load_world('worlds/harvest2.wld')

hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_and_pick_1(n):
    for i in range(n):
        hubo.pick_beeper()
        hubo.move()
        hubo.turn_left()
        hubo.move()
        turn_right()
    hubo.pick_beeper()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def move_and_pick_2(n):
    for i in range(n):
        hubo.pick_beeper()
        hubo.move()
        turn_right()
        hubo.move()
        hubo.turn_left()
    hubo.pick_beeper()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()

def move_and_pick_3(n):
    for i in range(n):
        hubo.pick_beeper()
        hubo.move()
        hubo.turn_left()
        hubo.move()
        turn_right()
    hubo.pick_beeper()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def move_and_pick_4(n):
    for i in range(n):
        hubo.pick_beeper()
        hubo.move()
        turn_right()
        hubo.move()
        hubo.turn_left()
    

def move_and_pick(n):
    move_and_pick_1(n)
    move_and_pick_2(n)
    move_and_pick_3(n)
    move_and_pick_4(n)
    hubo.pick_beeper()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

for i in range(5):
    hubo.move()
hubo.turn_left()
hubo.move()
turn_right()
for i in [4, 2, 0]:
    if i == 0:
        move_and_pick_1(i)
        move_and_pick_2(i)
        move_and_pick_3(i)
        move_and_pick_4(i)
        hubo.pick_beeper()
        break
    move_and_pick(i)