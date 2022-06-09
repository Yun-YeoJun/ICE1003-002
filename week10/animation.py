from cs1graphics import *
from time import *

paper = Canvas()

paper.setBackgroundColor('skyBlue')
paper.setWidth(300)
paper.setHeight(200)
paper.setTitle("My World")

roof = Polygon(Point(105, 105),Point(175,105),Point(170,85),Point(110,85))
roof.setFillColor('darkgray')
roof.setDepth(30)
paper.add(roof)

facade = Square(60,Point(140,130))
facade.setFillColor('white')
paper.add(facade)

chimney = Rectangle(15,28,Point(155,85))
chimney.setFillColor('red')
chimney.setBorderColor('red')
paper.add(chimney)

smoke = Path(Point(155,70),Point(150,65),Point(160,55),Point(155,50))
smoke.setBorderWidth(2)
paper.add(smoke)

car = Layer()

tire1 = Circle(10,Point(-20,-10))
tire1.setFillColor('black')
car.add(tire1)

tire2 = Circle(10,Point(20,-10))
tire2.setFillColor('black')
car.add(tire2)

body = Rectangle(70,30,Point(0,-25))
body.setFillColor('blue')
body.setDepth(60)
car.add(body)

car.moveTo(110,180)
#car.setDepth(20)
paper.add(car)

timeDelay = 0.1
sleep(timeDelay)

car.move(-10,0)
sleep(timeDelay)

car.move(-30,0)
sleep(timeDelay)

car.move(-60,0)
sleep(timeDelay)

car.move(-100,0)
sleep(timeDelay)