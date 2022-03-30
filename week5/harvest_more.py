from cs1robots import *

load_world("worlds/harvest3.wld")

hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)

def turn_right(): 
    for i in range(3):
        hubo.turn_left()

def turn_around_left():  
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def turn_around_right():
    turn_right()
    hubo.move()
    turn_right()

def beeper_on_pick(): # if hubo is on beeper, hubo pick beeper
    if hubo.on_beeper():
        hubo.pick_beeper()

def move_5(): # if hubo is on beeper, hubo pick beeper for 5 times
    for i in range(5):
        hubo.move()
        beeper_on_pick()

def move_and_check_beeper(): # hubo picks up beeper beeper if hubo is on beeper when zigzag
    hubo.move()
    for i in range(1, 7):
        beeper_on_pick()
        move_5()
        if i == 6:
            break
        elif i % 2 == 1:
            turn_around_left()
        else:
            turn_around_right()
    

move_and_check_beeper()