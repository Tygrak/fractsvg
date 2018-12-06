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
    def __init__(self, points = [], strokeWidth = 4):
        self.points = points
        self.stroke = "black"
        self.strokeWidth = strokeWidth
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

def GetBackgroundImage(width, height, backgroundColor = "white"):
    image = SVGImage(width, height)
    bgSquare = SVGPolygon([[0, 0], [width, 0], [width, height], [0, height]], 0)
    bgSquare.fill = backgroundColor
    image.addObject(bgSquare)
    return image