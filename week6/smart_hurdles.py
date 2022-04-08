# #hurdles1
# from cs1robots import *

# load_world('worlds/hurdles1.wld')

# hubo = Robot()
# hubo.set_trace('blue')

# def turn_right():
#     for i in range(3):
#         hubo.turn_left()

# def jump():
#     hubo.turn_left()
#     hubo.move()
#     for i in range(2):
#         turn_right()
#         hubo.move()
#     hubo.turn_left()

# while not hubo.on_beeper():
#     if hubo.front_is_clear():
#         hubo.move()
#     else:
#         jump()






# hurdles2
from cs1robots import *

load_world('worlds/hurdles2.wld')

hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def jump():
    hubo.turn_left()
    hubo.move()
    for i in range(2):
        turn_right()
        hubo.move()
    hubo.turn_left()

while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()
    else:
        jump()





# hurdles3
# from cs1robots import *

# load_world('worlds/hurdles3.wld')

# hubo = Robot()
# hubo.set_trace('blue')

# def turn_right():
#     for i in range(3):
#         hubo.turn_left()

# def jump():
#     hubo.turn_left()
#     hubo.move()
#     for i in range(2):
#         turn_right()
#         hubo.move()
#     hubo.turn_left()

# while not hubo.on_beeper():
#     if hubo.front_is_clear():
#         hubo.move()
#     else:
#         jump()
