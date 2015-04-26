from graphics import *
from random import *
#Making a window
win = GraphWin("Pegs", 300,400)
#First making the random coordinates for the center point of the pegs
def main():
    num = 7 # Ian feel free to change this value for the number of pegs.
    for p in range(num):
        #Row 1
        x = randrange(40,300,85) #Random x point
        y = 100
        peg1 = Circle(Point(x,y), 12)
        peg1.setFill("Light Green")
        peg1.draw(win)
        
        #Row 2
        x = randrange(40,300,85) #Random x point
        y = 200
        peg2 = Circle(Point(x,y), 12)
        peg2.setFill("Light Green")
        peg2.draw(win)
        
        #Row 3
        x = randrange(40,300,85) #Random x point
        y = 300
        peg3 = Circle(Point(x,y), 12)
        peg3.setFill("Light Green")
        peg3.draw(win)
        
main()
