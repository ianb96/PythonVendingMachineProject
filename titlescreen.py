from graphics import *
import time
import sys
sys.path.append('C:/Users/Ric/Desktop/New folder/Python vending machine project/Loading Screen')

import os

win = GraphWin("Vending Machine Simulator 2.0 - (v3)", 400, 400)

def LoadingScreen():
    lodScrens = []
    b = 0
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
    while  b != 4:
        for i in range(len(lodScrens)):
            lodScrens[i].draw(win)
            if i >= 1:
                lodScrens[i-1].undraw()
            time.sleep(0.1)
        time.sleep(0.1)
        b += 1
        lodScrens[i].undraw()


def titleScreen():
    maintitle = []
    stop = False
    maintitle.append(Image(Point(200,200),"titlescreen400x400.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x401.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x402.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x403.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x404.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x405.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x406.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x407.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x408.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x409.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x410.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x411.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x412.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x413.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x414.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x415.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x416.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x417.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x418.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x419.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x420.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x421.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x422.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x423.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x424.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x425.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x426.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x427.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x428.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x429.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x430.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x431.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x432.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x433.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x434.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x435.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x436.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x437.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x438.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x439.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x440.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x441.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x442.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x443.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x444.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x445.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x446.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x447.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x448.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x449.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x450.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x451.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x452.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x453.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x454.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x455.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x456.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x457.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x458.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x459.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x460.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x461.png"))
    maintitle.append(Image(Point(200,200),"titlescreen400x462.png"))

    while not stop:
        for i in range(len(maintitle)):
            if win.checkMouse():
                stop = True
                break
            maintitle[i].draw(win)
            if i >= 1:
                maintitle[i-1].undraw()
            time.sleep(0.05)
        if stop:
            break
        maintitle[i].undraw()
    winwidth = 400
    winheight = 400
    b = Polygon(Point(0,0),Point(410,0),Point(410,410),Point(0,410))
    b.setFill('white')
    b.draw(win)
titleScreen()
for i in win.items:
    win.delItem(i)
os.chdir('C:/Users/Ric/Desktop/New folder/Python vending machine project/Loading Screen')
LoadingScreen()
