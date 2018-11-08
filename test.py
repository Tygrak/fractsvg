import math
from svghelper import *
from fractalgenerators import *
from fractals import *

def CreateIterationImages(iterations, filename, function):
    for i in range(iterations):
        image = function(i)
        with open("output/{0}-{1}.svg".format(filename, i), "w") as svgFile:
            svgFile.write(image.generateImageString())

#CreateIterationImages(14, "output9", NotDragon)
#CreateIterationImages(12, "output8", DoubleDragonCurve)
#CreateIterationImages(14, "output7", DragonCurve)
CreateIterationImages(6, "output6", KochCross)
#CreateIterationImages(6, "output5", DoubleKochCurve)
#CreateIterationImages(7, "output4", KochSnowflake)
#CreateIterationImages(7, "output3", KochSnowflake)
#CreateIterationImages(7, "output2", KochSnowflake)
#CreateIterationImages(8, "output1", QuadSierpenski)
#CreateIterationImages(8, "output0", SierpenskiTriangle)