from cs1robots import *

load_world('worlds/newspaper.wld')

hubo = Robot(beepers=1)
hubo.set_trace('blue')
hubo.set_pause(0.5)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def climb_up_one_stair():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()

def climb_up_four_stairs():
    for i in range(4):
        climb_up_one_stair()
    hubo.move()
    hubo.drop_beeper()

def turn_around():
    hubo.turn_left()
    hubo.turn_left()

def climb_down_one_stair():
    hubo.move()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

def climb_down_four_stair():
    for i in range(4):
        climb_down_one_stair()
    hubo.move()

climb_up_four_stairs()
turn_around()
climb_down_four_stair()