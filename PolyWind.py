import numpy as np

BUTTON_X = 80
BUTTON_Y = 40
WIDTH = 1024
HEIGHT = 768

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#class Polygon:
#    def __init__(self):
#        self.pointList = list()
        
#    def 

def ccw(a, b, c):
    return np.sign(np.linalg.det(np.array([[a.x, b.x, c.x],
                                          [a.y, b.y, c.y],
                                          [1, 1, 1]])))

def windingNum(point, polygon):
    n = len(polygon)
    crossings = 0
    
    print('point = (%d, %d) and polygon = %s' %  (point.x, point.y, str(polygon)))
    
    for i in range(0, n):
        #is a crossing with edge pointing upward
        if (polygon[i]).y <= point.y and (polygon[(i+1) % n]).y > point.y:
            #point is to the left of the edge
            if ccw(polygon[i], polygon[(i+1) % n], point) == 1:
                crossings += 1
        #is a crossing with edge pointing downward
        if (polygon[i]).y > point.y and (polygon[(i+1) % n]).y <= point.y:
            #point is to the right of the edge
            if ccw(polygon[i], polygon[(i+1) % n], point) == -1:
                crossings -= 1
    return np.abs(crossings)

###################

from graphics import *

    #Button class to help provide input to program as a button
class Button:
    def __init__(self, text, x, y):
        self._topLeftPoint = Point(x, y)
        self._pressed = False
        self._text = text
    
    def Press(self):
        self._pressed = True
        
    def Pressed(self):
        return self._pressed
    
    def AckPress(self):
        self._pressed = False
        
    def Draw(self, graphWin):
        rect = Rectangle(self._topLeftPoint, Point(self._topLeftPoint.x + BUTTON_X, self._topLeftPoint.y + BUTTON_Y))
        rect.setFill("gold")
        rect.setOutline("green")
        rect.setWidth(2)
        rect.draw(graphWin)
        
        text = Text(Point(self._topLeftPoint.x + BUTTON_X/2, self._topLeftPoint.y + BUTTON_Y/2), self._text)
        text.setOutline("black")
        text.setFill("black")
        text.draw(graphWin)
        
    def TestPoint(self, point):
        if (point.x > self._topLeftPoint.x) & (point.x < self._topLeftPoint.x + BUTTON_X) & (point.y > self._topLeftPoint.y) & (point.y < self._topLeftPoint.y + BUTTON_Y):
            self._pressed = True
        else:
            self._pressed = False

#main() Function: Creates GraphWin window object and runs main loop for
#user input and graphics. Loop can be stopped by pressing keyboard c or
#by just closing window with its close button.
def main():
    stopLoop = False
    win = GraphWin("My Circle", WIDTH, HEIGHT)
    c = Circle(Point(50,50), 10)
    pointList = []
    #Construct "Clear" button. Draw it in loop.
    clearButton = Button("Clear", 900, 10) 
    win.setBackground("black")
    #windingPoint is the point around which the polygon winds
    windingPoint = Point(WIDTH/2, HEIGHT/2)
    #initialize winding number
    windingNumValue = 0
    
    while stopLoop == False:    #The main graphics/input processing loop
        #Clear the drawing area
        win.delete("all")
        #Draw the lines representing the polygon
        for pointIndex in range(len(pointList)):
            if pointIndex == len(pointList) - 1:
                #When reaching last point in polygon list, connect with first point
                line = Line(pointList[pointIndex], pointList[0])
            else:
                #For all other points, connect line from current point to next point
                line = Line(pointList[pointIndex], pointList[pointIndex + 1])
            #Set up remaining line attiorbutes and draw it
            line.setWidth(3)
            line.setFill("lightgreen")
            line.setOutline("lightgreen")
            line.draw(win)
            
        #Draw a circle to represent the winding point
        pointCircle = Circle(windingPoint,3)
        pointCircle.setFill("white")
        pointCircle.setOutline("white")
        pointCircle.draw(win)
        
        windingNumValue = windingNum(windingPoint, pointList)
        
        #Draw text representing winding number, offset from circle center
        pointText = Text(Point(windingPoint.x + 15, windingPoint.y - 10), str(windingNumValue))
        pointText.setOutline("white")
        pointText.draw(win)
        clearButton.Draw(win)
        
        
        #The check functions below do not stop to wait for input, but we only
        #need to draw after user input, so the following loop just waits for
        #input from mouse or keyboard.
        somethingPressed = False #Flag for whether user pressed something
        while somethingPressed == False:
            #Check and return where the mouse was clicked
            mousePressed = win.checkMouse()
            #Check and return what key was pressed
            keyPressed = win.checkKey()
            if mousePressed != None:
                somethingPressed = True
                #Have the clear button check whether it was pressed given the click point
                clearButton.TestPoint(mousePressed)
                if clearButton.Pressed():
                    pointList.clear()
                    #Tell button to reset pressed state
                    clearButton.AckPress()
                else:
                    #Add a point to the polygon point list!
                    pointList.append(mousePressed)
                    print(pointList)
            
            if keyPressed != "":
                somethingPressed = True
                #Press c to close (or just click close on window)
                if keyPressed == "c":
                    stopLoop = True
                    
                #win.close()
                
    #We're done
    win.close()
    
#Run main from here
main()
