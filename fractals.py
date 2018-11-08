import math
from svghelper import *
from fractalgenerators import *

def SierpenskiTriangle(iterations):
    image = getBackgroundImage(900, 900, "white")
    polygons = []
    polygons.append(SVGPolygon([[100, 800], [800, 800], [450, 100]]))
    for polygon in generateSierpenski(iterations, polygons):
        image.addObject(polygon)
    return image

def QuadSierpenski(iterations):
    image = getBackgroundImage(900, 900, "white")
    polygons = []
    polygons.append(SVGPolygon([[100, 100], [800, 100], [450, 450]]))
    polygons.append(SVGPolygon([[800, 100], [800, 800], [450, 450]]))
    polygons.append(SVGPolygon([[800, 800], [100, 800], [450, 450]]))
    polygons.append(SVGPolygon([[100, 800], [100, 100], [450, 450]]))
    for polygon in generateSierpenski(iterations, polygons):
        image.addObject(polygon)
    return image

def KochSnowflake(iterations):
    image = getBackgroundImage(900, 900, "white")
    polygons = []
    polygons.append(SVGPolygon([[300, 450+150*(3**0.5)], [600, 450+150*(3**0.5)]]))
    polygons.append(SVGPolygon([[600, 450+150*(3**0.5)], [750, 450]]))
    polygons.append(SVGPolygon([[750, 450], [600, 450-150*(3**0.5)]]))
    polygons.append(SVGPolygon([[600, 450-150*(3**0.5)], [300, 450-150*(3**0.5)]]))
    polygons.append(SVGPolygon([[300, 450-150*(3**0.5)], [150, 450]]))
    polygons.append(SVGPolygon([[150, 450], [300, 450+150*(3**0.5)]]))
    for polygon in generateKoch(iterations, polygons, vectScale=-2.25):
        image.addObject(polygon)
    return image

def DoubleKochCurve(iterations):
    image = getBackgroundImage(900, 900, "white")
    for i in range(iterations+1):
        polygons = []
        polygons.append(SVGPolygon([[100, 450], [800, 450]]))
        polygons.append(SVGPolygon([[800, 450], [100, 450]]))
        for polygon in generateKoch(i, polygons, vectScale=2.2):
            image.addObject(polygon)
    return image

def KochCross(iterations):
    image = getBackgroundImage(900, 900, "white")
    polygons = []
    polygons.append(SVGPolygon([[100, 450], [450, 850]]))
    polygons.append(SVGPolygon([[450, 850], [800, 450]]))
    polygons.append(SVGPolygon([[800, 450], [450, 50]]))
    polygons.append(SVGPolygon([[450, 50], [100, 450]]))
    for polygon in generateKoch(iterations, polygons, vectScale=1.5):
        image.addObject(polygon)
    return image

def NotDragon(iterations):
    image = getBackgroundImage(900, 900, "white")
    polyg1 = SVGPolygon([[660, 450], [240, 450]])
    polyg1.strokeWidth = 6
    polyg2 = SVGPolygon([[240, 450], [660, 450]])
    polyg2.strokeWidth = 6
    for polygon in generateAltKoch(iterations, [polyg1, polyg2]):
        image.addObject(polygon)
    return image

def DragonCurve(iterations):
    image = getBackgroundImage(900, 900, "white")
    dragon = SVGPolygon([[220, 550], [770, 550]])
    dragon.stroke = "black"
    dragon.strokeWidth = 4.5
    for i in range(iterations+1):
        for polygon in generateDragon(i, [dragon]):
            image.addObject(polygon)
    return image

def DoubleDragonCurve(iterations):
    image = getBackgroundImage(900, 900, "black")
    dragon1 = SVGPolygon([[200, 450], [700, 450]])
    dragon1.stroke = "red"
    dragon1.strokeWidth = 4.5
    dragon2 = SVGPolygon([[700, 450], [200, 450]])
    dragon2.stroke = "blue"
    dragon2.strokeWidth = 4.5
    for polygon in generateDragon(iterations, [dragon1, dragon2]):
        image.addObject(polygon)
    return image
