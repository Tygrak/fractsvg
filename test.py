import math
from svghelper import *

def getHalfwayPoint(a, b):
    x = (b[0]-a[0])/2 + a[0]
    y = (b[1]-a[1])/2 + a[1]
    return (x, y)

def generateSierpenski(iterations, polygons = [SVGPolygon([[50, 450], [450, 450], [250, 50]])]):
    for i in range(len(polygons)-1, -1, -1):
        #print(polygons[i].points)
        oldPoints = polygons[i].points
        points = []
        points.append((oldPoints[0][0], oldPoints[0][1]))
        points.append(getHalfwayPoint(oldPoints[0], oldPoints[1]))
        points.append(getHalfwayPoint(oldPoints[0], oldPoints[2]))
        newPolygon = SVGPolygon(points)
        newPolygon.strokeWidth = polygons[i].strokeWidth*7/9
        polygons.append(newPolygon)
        points = []
        points.append(getHalfwayPoint(oldPoints[1], oldPoints[0]))
        points.append((oldPoints[1][0], oldPoints[1][1]))
        points.append(getHalfwayPoint(oldPoints[1], oldPoints[2]))
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7/9)
        polygons.append(newPolygon)
        points = []
        points.append(getHalfwayPoint(oldPoints[2], oldPoints[0]))
        points.append(getHalfwayPoint(oldPoints[2], oldPoints[1]))
        points.append((oldPoints[2][0], oldPoints[2][1]))
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7/9)
        polygons.append(newPolygon)
        polygons.pop(i)
    if iterations > 0:
        polygons = generateSierpenski(iterations-1, polygons)
    return polygons

def generateAltKoch(iterations, polygons = [SVGPolygon([[100, 500], [400, 500]])]):
    for i in range(len(polygons)-1, -1, -1):
        oldPoints = polygons[i].points
        #print(i, len(polygons), oldPoints)
        points = []
        x = (oldPoints[1][0]-oldPoints[0][0])/2 + oldPoints[0][0]
        y = (oldPoints[1][1]-oldPoints[0][1])/2 + oldPoints[0][1]
        vectx = (oldPoints[1][0]-oldPoints[0][0])/2.265
        vecty = (oldPoints[1][1]-oldPoints[0][1])/2.265
        secondPoint = (x+vecty, y-vectx)
        points.append(oldPoints[0])
        points.append(secondPoint)
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.75/9)
        newPolygon.stroke = polygons[i].stroke
        polygons.append(newPolygon)
        points = []
        points.append(secondPoint)
        points.append(oldPoints[1])
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.75/9)
        newPolygon.stroke = polygons[i].stroke
        polygons.append(newPolygon)
        #polygons.pop(i)
    if iterations > 0:
        polygons = generateAltKoch(iterations-1, polygons)
    return polygons

def generateKoch(iterations, polygons = [SVGPolygon([[100, 500], [400, 500]])]):
    for i in range(len(polygons)-1, -1, -1):
        oldPoints = polygons[i].points
        #print(i, len(polygons), oldPoints)
        points = []
        x = (oldPoints[1][0]-oldPoints[0][0])/2 + oldPoints[0][0]
        y = (oldPoints[1][1]-oldPoints[0][1])/2 + oldPoints[0][1]
        vectx = (oldPoints[1][0]-oldPoints[0][0])/2.75
        vecty = (oldPoints[1][1]-oldPoints[0][1])/2.75
        halfPoint = (x+vecty, y-vectx)
        x = (oldPoints[1][0]-oldPoints[0][0])/3 + oldPoints[0][0]
        y = (oldPoints[1][1]-oldPoints[0][1])/3 + oldPoints[0][1]
        onethirdPoint = (x, y)
        x = 2*(oldPoints[1][0]-oldPoints[0][0])/3 + oldPoints[0][0]
        y = 2*(oldPoints[1][1]-oldPoints[0][1])/3 + oldPoints[0][1]
        twothirdPoint = (x, y)
        points.append(oldPoints[0])
        points.append(onethirdPoint)
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.55/9)
        polygons.append(newPolygon)
        points = []
        points.append(onethirdPoint)
        points.append(halfPoint)
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.55/9)
        polygons.append(newPolygon)
        points = []
        points.append(halfPoint)
        points.append(twothirdPoint)
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.55/9)
        polygons.append(newPolygon)
        points = []
        points.append(twothirdPoint)
        points.append(oldPoints[1])
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.55/9)
        polygons.append(newPolygon)
        points = []
        polygons.pop(i)
    if iterations > 0:
        polygons = generateKoch(iterations-1, polygons)
    return polygons


def generateDragon(iterations, polygons = [SVGPolygon([[125, 300], [425, 300]])]):
    for i in range(len(polygons)-1, -1, -1):
        oldPoints = polygons[i].points
        points = []
        x = (oldPoints[1][0]-oldPoints[0][0])/2 + oldPoints[0][0]
        y = (oldPoints[1][1]-oldPoints[0][1])/2 + oldPoints[0][1]
        vectx = (oldPoints[1][0]-oldPoints[0][0])/2
        vecty = (oldPoints[1][1]-oldPoints[0][1])/2
        secondPoint = (x+vecty, y-vectx)
        points.append(oldPoints[0])
        points.append(secondPoint)
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.85/9)
        newPolygon.stroke = polygons[i].stroke
        polygons.append(newPolygon)
        points = []
        points.append(oldPoints[1])
        points.append(secondPoint)
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.85/9)
        newPolygon.stroke = polygons[i].stroke
        polygons.append(newPolygon)
        polygons.pop(i)
    if iterations > 0:
        polygons = generateDragon(iterations-1, polygons)
    return polygons

image = SVGImage(500, 500)
bgSquare = SVGPolygon([[0, 0], [500, 0], [500, 500], [0, 500]], 0)
bgSquare.fill = "white"
image.addObject(bgSquare)

#for polygon in generateSierpenski(7, [SVGPolygon([[50, 450], [450, 450], [250, 250]]), SVGPolygon([[450, 450], [450, 50], [250, 250]]),
#     SVGPolygon([[450, 50], [50, 50], [250, 250]]), SVGPolygon([[50, 50], [50, 450], [250, 250]])]):
#    image.addObject(polygon)
#for polygon in generateSierpenski(6):
#    image.addObject(polygon)
polyg1 = SVGPolygon([[400, 250], [100, 250]])
polyg1.stroke = "rgb(255, 0, 191)"
polyg2 = SVGPolygon([[100, 250], [400, 250]])
polyg2.stroke = "rgb(0, 64, 255)"
polyg3 = SVGPolygon([[250, 400], [250, 100]])
polyg3.stroke = "rgb(0, 255, 64)"
polyg4 = SVGPolygon([[250, 100], [250, 400]])
polyg4.stroke = "rgb(255, 191, 0)"
for polygon in generateAltKoch(7, [polyg1, polyg2, polyg3, polyg4]):
    image.addObject(polygon)
#for polygon in generateKoch(5, [SVGPolygon([[500, 250], [0, 250]]), SVGPolygon([[0, 250], [500, 250]])]):
#    image.addObject(polygon)
#for polygon in generateKoch(6, [SVGPolygon([[150, 250+100*(3**0.5)], [350, 250+100*(3**0.5)]]), SVGPolygon([[350, 250+100*(3**0.5)], [450, 250]]),
#                            SVGPolygon([[450, 250], [350, 250-100*(3**0.5)]]), SVGPolygon([[350, 250-100*(3**0.5)], [150, 250-100*(3**0.5)]]),
#                            SVGPolygon([[150, 250-100*(3**0.5)], [50, 250]]), SVGPolygon([[50, 250], [150, 250+100*(3**0.5)]])]):
#    image.addObject(polygon)
#for polygon in generateDragon(13, [SVGPolygon([[130, 250], [370, 250]])]):
#    image.addObject(polygon)
#dragon1 = SVGPolygon([[130, 250], [370, 250]])
#dragon1.stroke = "red"
#dragon1.strokeWidth = 4.5
#dragon2 = SVGPolygon([[370, 250], [130, 250]])
#dragon2.stroke = "blue"
#dragon2.strokeWidth = 4.5
#for polygon in generateDragon(13, [dragon1, dragon2]):
#    image.addObject(polygon)

with open("output9.svg", "w") as svgFile:
    svgFile.write(image.generateImageString())
