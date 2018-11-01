import math

class SVGImage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []

    def addObject(self, obj):
        self.objects.append(obj)

    def generateImageString(self):
        imageString = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{0}" height="{1}">\n'.format(self.width, self.height)
        for obj in self.objects:
            imageString += '  {0}\n'.format(obj.generateObjectString())
        imageString += '</svg>\n'
        return imageString

class SVGPolygon:
    def __init__(self, points = []):
        self.points = points
        self.stroke = "black"
        self.strokeWidth = 4
        self.fill = "none"

    def addPoint(self, x, y):
        self.points.append([x, y])

    def generateObjectString(self):
        pointsString = ""
        for point in self.points:
            pointsString += "{0},{1} ".format(point[0], point[1])
        pointsString = pointsString.rstrip()
        styleString = 'stroke="{0}" stroke-width="{1}" fill="{2}"'.format(self.stroke, self.strokeWidth, self.fill)
        objectString = '<polygon points="{0}" {1} />'.format(pointsString, styleString)
        return objectString

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
        oldPoints = polygons[i].points
        points = []
        points.append(getHalfwayPoint(oldPoints[1], oldPoints[0]))
        points.append((oldPoints[1][0], oldPoints[1][1]))
        points.append(getHalfwayPoint(oldPoints[1], oldPoints[2]))
        newPolygon = SVGPolygon(points)
        newPolygon.strokeWidth = polygons[i].strokeWidth*7/9
        polygons.append(newPolygon)
        points = []
        points.append(getHalfwayPoint(oldPoints[2], oldPoints[0]))
        points.append(getHalfwayPoint(oldPoints[2], oldPoints[1]))
        points.append((oldPoints[2][0], oldPoints[2][1]))
        newPolygon = SVGPolygon(points)
        newPolygon.strokeWidth = polygons[i].strokeWidth*7/9
        polygons.append(newPolygon)
        polygons.pop(i)
    if iterations > 0:
        polygons = generateSierpenski(iterations-1, polygons)
    return polygons

image = SVGImage(500, 500)
for polygon in generateSierpenski(7, [SVGPolygon([[50, 450], [450, 450], [250, 250]]), SVGPolygon([[450, 450], [450, 50], [250, 250]]),
     SVGPolygon([[450, 50], [50, 50], [250, 250]]), SVGPolygon([[50, 50], [50, 450], [250, 250]])]):
    image.addObject(polygon)
#for polygon in generateSierpenski(6):
#    image.addObject(polygon)

with open("output.svg", "w") as svgFile:
    svgFile.write(image.generateImageString())

