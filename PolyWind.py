import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(a, b, c):
    return np.sign(np.linalg.det(np.array([[a.x, b.x, c.x],
                                          [a.y, b.y, c.y],
                                          [1, 1, 1]])))

def windingNum(point, polygon):
    n = len(polygon)
    crossings = 0
    
    for i in range(0, n):
        #is a crossing with edge pointing upward
        if (polygon[i]).y <= point.y and (polygon[i+1]).y > point.y:
            #point is to the left of the edge
            if ccw(polygon[i], polygon[i+1], point) == 1:
                crossings += 1
        #is a crossing with edge pointing downward
        if (polygon[i]).y > point.y and (polygon[i+1]).y <= point.y:
            #point is to the right of the edge
            if ccw(polygon[i], polygon[i+1], point) == -1:
                crossings -= 1
    return crossings

###################

from graphics import *

def main():
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()
main()
