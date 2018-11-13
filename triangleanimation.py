import math
import graphics

from graphics import *

win = GraphWin('',400,400)

w = 0

while True:
    xcomp1 = math.cos(0.1*w)
    ycomp1 = math.sin(w)
    xcomp2 = math.cos(2*w)
    ycomp2 = math.sin(3*w)
    xcomp3 = math.cos(w)
    ycomp3 = math.sin(w**1.4)
    v1 = Point(200+150*xcomp1**3,200+100*ycomp1**5)
    v2 = Point(210+60*ycomp2,200+60*xcomp2)
    v3 = Point(200+170*xcomp3,210+170*ycomp3)
    
    v4 = Point(200+170*xcomp2,210+170*ycomp1)
##    v5 = Point(200+170*xcomp1,210+170*ycomp3)
##    v6 = Point(200+180*xcomp1,210+170*ycomp2)
    triangle = Polygon(v1,v4,v3,v2)
    circle = Circle(v2, 20)
    circle.draw(win)
    circle.undraw()
    triangle.draw(win)
    triangle.undraw()

##    l1 = Line(v1,v2)
##    l1.setOutline("red")
##    l2 = Line(v2,v3)
##    l2.setOutline("blue")
##    l3 = Line(v1,v3)
##    l3.setOutline("green")
##    l1.draw(win)
##    l2.draw(win)
##    l3.draw(win)
##    if not ((w*10)%5):
##        l1.undraw()
##        l2.undraw()
##        l3.undraw()
    w += 0.1

    if w > 314.259:
        w = 0

