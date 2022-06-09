from cs1robots import *

load_world("worlds/add2.wld")

hubo = Robot(street=2)
hubo.set_trace("blue")
hubo.set_pause(0.1)

var1 = []
var2 = []
tf = False
while hubo.front_is_clear():
    cnt = 0
    while hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1
        tf = True
    if tf:
        var1.append(str(cnt))
    hubo.move()
if hubo.on_beeper():
    cnt = 0
    while hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1
        tf = True
    if tf:
        var1.append(str(cnt))
else:
    var1.append('0')
var1 = int(''.join(var1))

hubo.turn_left()
hubo.turn_left()

while hubo.front_is_clear():
    hubo.move()

hubo.turn_left()
hubo.move()
hubo.turn_left()

tf = False
while hubo.front_is_clear():
    cnt = 0
    while hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1
        tf = True
    if tf:
        var2.append(str(cnt))
    hubo.move()
if hubo.on_beeper():
    cnt = 0
    while hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1
        tf = True
    if tf:
        var2.append(str(cnt))
else:
    var2.append('0')
var2 = int(''.join(var2))

var3 = var1 + var2

var3 = list(map(int,reversed(str(var3))))

hubo.turn_left()
hubo.turn_left()

for i in range(len(var3)):
    for i in range(var3[i]):
        hubo.drop_beeper()
    hubo.move()