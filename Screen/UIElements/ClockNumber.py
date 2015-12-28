import pygame
from UIElement import UIElement
from Dicts import *
class Number(UIElement):
    def __init__(self, name, index, Location, width, height, active, value):
        UIElement.__init__(self, name, index, Location, width, height, active)
        self.value = value
        self.img = None
    def changeValue(self, newValue):
        self.value = newValue
        self.loadImg()
    def loadImg(self):
        self.img = pygame.transform.scale(pygame.image.load('Resources/img/numbers/%d.png' %self.value).convert(), (self.width, self.height))


#Factory Method
def CreateClockNumberDict(screenSize, Numbers, inits):
    width = screenSize[0] / 7
    height = screenSize[1] / 7
    tmp = map(lambda x: x[0], sorted(Numbers.iteritems(), key = lambda x: x[1], reverse = False))
    return dict(map(lambda x:
                    (x[0], Number(x[0], Numbers[x[0]], getNumberLocation(screenSize, Numbers[x[0]]), getNumberSize(screenSize, Numbers[x[0]])[0], getNumberSize(screenSize, Numbers[x[0]])[1], True, x[1]))
                    , zip(tmp, inits)))

def getNumberLocation(screenSize, numberIndex):
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    stepHori = screenWidth / 20
    stepVert = screenHeight / 20
    if 8 <= numberIndex <= 11:
        return [stepHori * 4 * ( numberIndex - 8), stepVert * 5]
    else:
        return [stepHori * (12 + (numberIndex - 11)* 3), stepVert * 47 / 8]
def getNumberSize(screenSize, numberIndex):
    if 8 <= numberIndex <= 11:
        return [screenSize[0] / 7, screenSize[1] / 7]
    else:
        return [screenSize[0] / 10, screenSize[1] / 10]
class colon(UIElement):
    def __init__(self, name, index , Location, width, height, active):
        UIElement.__init__(self, name, index, Location, width, height, active)
        self.img = None
    def loadImg(self):
        self.img = pygame.transform.scale(pygame.image.load('Resources/img/numbers/colon.png').convert(), (self.width, self.height))
    def reverse(self):
        self.active = ~self.active
def CreateColon(screenSize, active):
    width = screenSize[0] / 16
    height = screenSize[1] / 7
    return colon('colon', ColonIndex, getColonLocation(screenSize), width, height, active)
def getColonLocation(screenSize):
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    stepHori = screenWidth / 20
    stepVert = screenHeight / 20
    return [stepHori * 7, stepVert * 5]