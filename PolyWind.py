import numpy as np

#Some constants
BUTTON_X = 90
BUTTON_Y = 40
WIDTH = 1024
HEIGHT = 768

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(a, b, c):
    return np.sign(np.linalg.det(np.array([[a.x, b.x, c.x],
                                          [a.y, b.y, c.y],
                                          [1, 1, 1]])))

##########################################################
# WINDING NUMBER ALGORITHM
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
    return crossings
###########################################################
# Note: intersect function is only used for the tutorial display.
# It is not needed in the algorithm calculating the winding number.
def intersect(lineA, lineB): #intersection point of two lines
    xdiff = (lineA.getP1().x - lineA.getP2().x, lineB.getP1().x - lineB.getP2().x)
    ydiff = (lineA.getP1().y - lineA.getP2().y, lineB.getP1().y - lineB.getP2().y)
    #calculate determinants
    def lineDet(line):
        return line.getP1().x * line.getP2().y - line.getP1().y * line.getP2().x
    def det(pt1, pt2):
        return pt1[0] * pt2[1] - pt1[1] * pt2[0]
    #rays do not intersect
    div = det(xdiff, ydiff)
    if div == 0:
        return 0
    #calculate x and y values
    d = (lineDet(lineA), lineDet(lineB))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    #check if lines intersect 
    if x < lineA.getP1().x and x < lineA.getP2().x:
        return 0
    if x > lineA.getP1().x and x > lineA.getP2().x:
        return 0
    if y < lineB.getP1().y:
        return 0
    #calculate crossing number (direction)
    #if lineA.getP2().x < x:
    #    crossingNum = 1
    #else:
    #    crossingNum = 0
    #return intersectional point
    return Point(x, y)

################################################

from graphics import *

    #Button class to help provide input to program as a button
class Button:
    def __init__(self, text, x, y):
        self._topLeftPoint = Point(x, y)
        self._pressed = False
        self._text = text
        
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
    polygonPointList = []
    #Construct "Clear" button. Draw it in loop.
    clearButton = Button("Clear", 900, 10) 
    win.setBackground("black")
    #windingPoint is the point around which the polygon winds
    windingPoint = None
    #initialize winding number
    windingNumValue = 0
    displayButton = Button("Toggle Ray", 900, 70)
    displayRay = False
    while stopLoop == False:    #The main graphics/input processing loop
        #Clear the drawing area
        win.delete("all")
        #Draw buttons
        clearButton.Draw(win)
        displayButton.Draw(win)
        #initialize crossing number
        crossingNumValue = 0
        if windingPoint != None:
            if displayRay:
                #initialize ray to count edge crossings from winding point
                ray = Line(windingPoint, Point(WIDTH/2, HEIGHT))
                ray.setWidth(3)
                ray.setFill("red")
                ray.setOutline("red")
                ray.setArrow("last");
                ray.draw(win)
            #Draw the lines representing the polygon
            for pointIndex in range(len(polygonPointList)):
                if pointIndex == len(polygonPointList) - 1:
                    #When reaching last point in polygon list, connect with first point
                    line = Line(polygonPointList[pointIndex], polygonPointList[0])
                else:
                    #For all other points, connect line from current point to next point
                    line = Line(polygonPointList[pointIndex], polygonPointList[pointIndex + 1])
                #Set up remaining line attiorbutes and draw it
                line.setWidth(3)
                line.setFill("lightgreen")
                line.setOutline("lightgreen")
                line.setArrow("last")
                line.draw(win)

                if displayRay:
                    #find intersection of ray and edge
                    intersection = intersect(line, ray)
                    #display number of crossings from winding point to edge
                    if intersection != 0:
                        #crossingNumValue = crossingNumValue + 1
                        crossingNumValue = int(ccw(ray.getP1(), line.getP1(), line.getP2()))
                        rayText = Text(Point(intersection.x + 10, intersection.y - 10), str(crossingNumValue))
                        rayText.setOutline("white")
                        rayText.draw(win)
            
            #Draw a circle to represent the winding point
            pointCircle = Circle(windingPoint,3)
            pointCircle.setFill("white")
            pointCircle.setOutline("white")
            pointCircle.draw(win)
                
            windingNumValue = windingNum(windingPoint, polygonPointList)
            
            #Draw text representing winding number, offset from circle center
            pointText = Text(Point(windingPoint.x + 15, windingPoint.y - 10), str(windingNumValue))
            pointText.setOutline("white")
            pointText.draw(win)
        
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
                displayButton.TestPoint(mousePressed)
                if clearButton.Pressed():
                    windingPoint = None
                    polygonPointList.clear()
                    #Tell button to reset pressed state
                    clearButton.AckPress()
                elif displayButton.Pressed():
                    displayRay = not displayRay
                    displayButton.AckPress()
                elif windingPoint == None:
                    windingPoint = mousePressed
                else:
                    #Add a point to the polygon point list!
                    polygonPointList.append(mousePressed)
                    print(polygonPointList)
            
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
