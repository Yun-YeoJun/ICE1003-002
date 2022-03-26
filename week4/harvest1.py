from cs1robots import *

load_world('worlds/harvest1.wld')

hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.5)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def up():
    for i in range(6):
        hubo.pick_beeper()
        hubo.move()
def down():
    for i in range(6):
        hubo.move()
        hubo.pick_beeper()

def up_and_down():
    hubo.move()
    hubo.turn_left()
    up()
    turn_right()
    hubo.move()
    turn_right()
    down()
    hubo.turn_left()

for i in range(3):
    up_and_down()