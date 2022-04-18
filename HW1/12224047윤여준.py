# Task 1. Smart Hurdles
from cs1robots import *

load_world('worlds/hurdles3.wld')

hubo = Robot()
hubo.set_trace('blue')

def turn_right(): # hubo turn right
    for i in range(3):
        hubo.turn_left()

def jump(): # hubo jumps hurdle
    hubo.turn_left()
    hubo.move()
    i = 0
    while i < 2:
        turn_right()
        hubo.move()
        i+=1
    hubo.turn_left()

# repeat until hubo is on beeper
while not hubo.on_beeper():
    if hubo.front_is_clear(): # if hubo's front is not hurdle, hubo moves forward
        hubo.move()
    else: # if hubo's front is hurdle, hubo jumps hurdle
        jump()







# # Task 2. Rain
# from cs1robots import *

# load_world('worlds/rain1.wld')

# hubo = Robot(beepers=6,orientation="E",avenue=2,street=6) # Set the initial location of hubo
# hubo.set_trace('blue')
# hubo.set_pause(0.2)

# def turn_right(): # A function that causes hubo to turn right
#     for i in range(3):
#         hubo.turn_left()

# def check_and_drop(): # A function that drops a beeper if hubo is next to a window
#     if hubo.right_is_clear():
#         hubo.drop_beeper()

# # move into the house and put beeper at door
# hubo.move()
# turn_right()
# hubo.drop_beeper()
# hubo.move()

# # repeat until hubo arrive door
# while not hubo.on_beeper():
#     check_and_drop()
#     if hubo.front_is_clear(): # if hubo's front is clear, hubo move forward 
#         hubo.move()
#     else: # if hubo's front is not clear, hubo turn left and move forward
#         hubo.turn_left()
#         hubo.move()

# # pick beeper and turn to door
# hubo.pick_beeper()
# turn_right()
