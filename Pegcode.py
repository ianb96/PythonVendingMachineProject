from graphics import *
from random import *
#Making a window
win = GraphWin("Pegs", 400,400)
#First making the random coordinates for the center point of the pegs
def main():
    num = 14 # Ian feel free to change this value for the number of pegs.
    for p in range(num):
        x = randint(1,401) #Random x point
        y = randint(1,401) #Random y point
        peg = Circle(Point(x,y), 15) #Combined the random points for center, w/ radius 15 pixels
        peg.setFill("Light Green") #Fill in the circle with light green color
        peg.draw(win) #Draw peg on graph
        
main()
