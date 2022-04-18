from cs1media import *

img = load_picture('images/panda.jpg')

w, h = img.size()

for y in range(h):
    for x in range(w):
        r,g,b = img.get(x,y)

        v = (r+g+b) // 3 # average of r,g,b

        if v < 50:
            r,g,b = 0,0,255 # blue
        elif v>200:
            r,g,b = 255,255,0 # yellow
        else:
            r,g,b = 0,255,0 # green
        img.set(x,y,(r,g,b))
img.show()