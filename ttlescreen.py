from graphics import*
import time


def buttontest():
    maintitle = []
    win = GraphWin("My graphwindow",500,500)
    #Title screen
    Image(Point(250,250),"MTSFVMS23.png").draw(win)

    #Button screen
    button = Rectangle(Point(150,250),Point(250,300))
    button.setFill('cyan')
    button.draw(win)
    blabel = Text(Point(200,275),"button")
    blabel.setFace('times roman')
    blabel.setSize(15)
    blabel.setStyle('bold')
    blabel.move(-1,2)
    blabel.draw(win)
    
    blabel2 = Text(Point(200,275),"button")
    blabel2.setSize(15)
    blabel2.setFace('times roman')
    blabel2.setStyle('bold')
    blabel2.setTextColor('orange')
    blabel2.draw(win)
    
    
    brain = False
    while brain == False:
        #b = win.getMouse()
        b = win.checkMouse()
        if b:
            if b.getX() >= 150 and b.getX() < 250 and b.getY() >= 250 and b.getY() < 300:
                print("yay")
                blabel.undraw()
                blabel2.undraw()
                time.sleep(0.1)
                blabel.draw(win)
                blabel2.draw(win)

    
buttontest()


