import math
from svghelper import *

def generateSierpenski(iterations, polygons = [SVGPolygon([[50, 450], [450, 450], [250, 50]])], removeOld = True):
    def getHalfwayPoint(a, b):
        x = (b[0]-a[0])/2 + a[0]
        y = (b[1]-a[1])/2 + a[1]
        return (x, y)

    for i in range(len(polygons)-1, -1, -1):
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
        if removeOld:
            polygons.pop(i)
    if iterations > 0:
        polygons = generateSierpenski(iterations-1, polygons, removeOld)
    return polygons

def generateAltKoch(iterations, polygons = [SVGPolygon([[100, 500], [400, 500]])], vectScale = 2.0, removeOld = True):
    for i in range(len(polygons)-1, -1, -1):
        oldPoints = polygons[i].points
        #print(i, len(polygons), oldPoints)
        points = []
        x = (oldPoints[1][0]-oldPoints[0][0])/2 + oldPoints[0][0]
        y = (oldPoints[1][1]-oldPoints[0][1])/2 + oldPoints[0][1]
        vectx = (oldPoints[1][0]-oldPoints[0][0])/vectScale
        vecty = (oldPoints[1][1]-oldPoints[0][1])/vectScale
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
        if removeOld:
            polygons.pop(i)
    if iterations > 0:
        polygons = generateAltKoch(iterations-1, polygons, vectScale, removeOld)
    return polygons

def generateKoch(iterations, polygons = [SVGPolygon([[100, 500], [400, 500]])], vectScale = 2.0, removeOld = True):
    for i in range(len(polygons)-1, -1, -1):
        oldPoints = polygons[i].points
        #print(i, len(polygons), oldPoints)
        points = []
        x = (oldPoints[1][0]-oldPoints[0][0])/2 + oldPoints[0][0]
        y = (oldPoints[1][1]-oldPoints[0][1])/2 + oldPoints[0][1]
        vectx = (oldPoints[1][0]-oldPoints[0][0])/vectScale
        vecty = (oldPoints[1][1]-oldPoints[0][1])/vectScale
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
        newPolygon.stroke = polygons[i].stroke
        polygons.append(newPolygon)
        points = []
        points.append(onethirdPoint)
        points.append(halfPoint)
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.55/9)
        newPolygon.stroke = polygons[i].stroke
        polygons.append(newPolygon)
        points = []
        points.append(halfPoint)
        points.append(twothirdPoint)
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.55/9)
        newPolygon.stroke = polygons[i].stroke
        polygons.append(newPolygon)
        points = []
        points.append(twothirdPoint)
        points.append(oldPoints[1])
        newPolygon = SVGPolygon(points, polygons[i].strokeWidth*7.55/9)
        newPolygon.stroke = polygons[i].stroke
        polygons.append(newPolygon)
        points = []
        if removeOld:
            polygons.pop(i)
    if iterations > 0:
        polygons = generateKoch(iterations-1, polygons, vectScale, removeOld)
    return polygons


def generateDragon(iterations, polygons = [SVGPolygon([[125, 300], [425, 300]])], vectScale = 2.0, removeOld = True):
    for i in range(len(polygons)-1, -1, -1):
        oldPoints = polygons[i].points
        points = []
        x = (oldPoints[1][0]-oldPoints[0][0])/2 + oldPoints[0][0]
        y = (oldPoints[1][1]-oldPoints[0][1])/2 + oldPoints[0][1]
        vectx = (oldPoints[1][0]-oldPoints[0][0])/vectScale
        vecty = (oldPoints[1][1]-oldPoints[0][1])/vectScale
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
        if removeOld:
            polygons.pop(i)
    if iterations > 0:
        polygons = generateDragon(iterations-1, polygons, vectScale, removeOld)
    return polygons
