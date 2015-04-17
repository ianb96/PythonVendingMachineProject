from graphics import *
import time

def LoadingScreen():
    lodScrens = []
    b = 0
    win = GraphWin("Vending Machine Simulator 2.0 - (v3)", 400, 400)
    lodScrens.append(Image(Point(200,200),"Waitscreen1.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen2.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen3.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen4.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen5.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen6.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen7.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen8.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen9.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen10.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen11.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen12.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen13.png"))
    lodScrens.append(Image(Point(200,200),"Waitscreen14.png"))
    while  b != 5:
        for i in range(len(lodScrens)):
            lodScrens[i].draw(win)
            if i >= 1:
                lodScrens[i-1].undraw()
            time.sleep(0.1)
        time.sleep(1)
        b += 1
        lodScrens[i].undraw()

LoadingScreen()
