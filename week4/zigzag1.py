from cs1robots import *
create_world()

def turn_right():
    for i in range(3):
        hubo.turn_left()
    
def zig_zag():
    for i in range(9):
        hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    for i in range(9):
        hubo.move()

hubo = Robot()
#hubo.set_trace('blue')
hubo.set_pause(0.1)

hubo.turn_left()
hubo.set_trace('blue')
for i in range(4):
    zig_zag()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
zig_zag()