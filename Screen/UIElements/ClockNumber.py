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
    def loadImg(self):
        self.img = pygame.transform.scale(pygame.image.load('Resources/img/numbers/%d.png' %self.value).convert(), (self.width, self.height))


#Factory Method
def CreateClockNumberDict(screenSize, Numbers, inits):
    width = screenSize[0] / 5
    height = screenSize[1] / 5
    tmp = map(lambda x: x[0], sorted(Numbers.iteritems(), key = lambda x: x[1], reverse = True))
    return dict(map(lambda x:
                    (x[0], Number(x[0], Numbers[x[0]], getNumberLocation(screenSize, Numbers[x[0]]), width, height, True, x[1]))
                    , zip(tmp, inits)))

def getNumberLocation(screenSize, numberIndex):
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    stepHori = screenWidth / 20
    stepVert = screenHeight / 20
    return [stepHori * 5 * ( -numberIndex - 1), stepVert * 5]

class colon(UIElement):
    def __init__(self, name, index , Location, width, height, active):
        UIElement.__init__(self, name, index, Location, width, height, active)
        self.img = None
    def loadImg(self):
        self.img = pygame.transform.scale(pygame.image.load('Resources/img/numbers/colon.png').convert(), (self.width, self.height))
    def reverse(self):
        self.active = ~self.active
def CreateColon(screenSize, active):
    width = screenSize[0] / 13
    height = screenSize[1] / 5
    return colon('colon', ColonIndex, getColonLocation(screenSize), width, height, active)
def getColonLocation(screenSize):
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    stepHori = screenWidth / 20
    stepVert = screenHeight / 20
    return [stepHori * 35 / 4, stepVert * 5]