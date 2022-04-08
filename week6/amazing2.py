from cs1robots import *

load_world('worlds/amazing2.wld')

hubo = Robot(beepers=1)
hubo.set_trace("blue")
def turn_right():
    for i in range(3):
        hubo.turn_left()

hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
    if hubo.front_is_clear():
        if hubo.right_is_clear():
            turn_right()
            hubo.move()
        else:
            hubo.move()
    else:
        hubo.turn_left()
        hubo.move()

hubo.pick_beeper()