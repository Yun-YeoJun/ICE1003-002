from cs1robots import *

load_world('worlds/harvest3.wld')

hubo = Robot(beepers=100)
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

def not_beeper_on_drop(): # if hubo is not on beeper, hubo drops beeper
    if not hubo.on_beeper():
        hubo.drop_beeper()

def move_5(): # if hubo is not on beeper, hubo drops beeper for 5 times
    for i in range(5):
        hubo.move()
        not_beeper_on_drop()

def move_and_check_beeper(): # hubo drops up beeper beeper if hubo is not on the beeper when zigzag
    hubo.move()
    for i in range(1, 7):
        not_beeper_on_drop()
        move_5()
        if i == 6:
            break
        elif i % 2 == 1:
            turn_around_left()
        else:
            turn_around_right()
    

move_and_check_beeper()