from cs1media import *

threshold = 100
white = (255,255,255)
black = (0,0,0)

img = load_picture('images/inhaCampus2.jpg')
w, h = img.size()
for y in range(h):
    for x in range(w):
        r,g,b = img.get(x,y)
        v = (r+g+b)//3 # average of r,g,b
        if v > threshold:
            img.set(x,y,white)
        else:
            img.set(x,y,black)

img.show()