from cs1robots import *

load_world('worlds/rain1.wld')

hubo = Robot(beepers=6,orientation="E",avenue=2,street=6)
hubo.set_trace('blue')
hubo.set_pause(0.2)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def check_and_drop():
    if hubo.right_is_clear():
        hubo.drop_beeper()

# move into the house and put beeper at door
hubo.move()
turn_right()
hubo.drop_beeper()
hubo.move()

# repeat until hubo arrive door
while not hubo.on_beeper():
    check_and_drop()
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
        hubo.move()

# pick beeper and turn to door
hubo.pick_beeper()
turn_right()