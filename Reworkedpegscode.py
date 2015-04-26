from graphics import *
from random import *
#Making a window
win = GraphWin("Pegs", 300,400)
#First making the random coordinates for the center point of the pegs
def main():
    num = 7 # Ian feel free to change this value for the number of pegs.
    pegs = []
    for p in range(num):
        #Row 1
        x = randrange(40,300,85) #Random x point
        y = 100
        pegs.append(Circle(Point(x,y), 12))
        
        #Row 2
        x = randrange(40,300,85) #Random x point
        y = 200
        pegs.append(Circle(Point(x,y), 12))
        
        #Row 3
        x = randrange(40,300,85) #Random x point
        y = 300
        pegs.append(Circle(Point(x,y), 12))

    for i in range(len(pegs)):
        print(pegs[i])
        pegs[i].setFill('Light Green')
        pegs[i].draw(win)
        
main()
