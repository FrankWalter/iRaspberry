import pygame
from UIElement import UIElement
class Number(UIElement):
    def __init__(self, name, index, img, Location, width, height, active, value):
        UIElement.__init__(self, name, index, img, Location, width, height, active)
        self.value = value
    def changeValue(self, newValue):
        self.value = newValue
        self.loadImg()
    def loadImg(self):
        self.img = pygame.transform.scale(pygame.image.load('Resources/img/numbers/%d.png' %self.value).convert(), (self.width, self.height))


#Factory Method
def CreateClockNumberDict(screenSize, Numbers, inits):
    width = screenSize[0] / 5
    height = screenSize[1] / 5
    tmp = Numbers.keys()
    tmp.sort(cmp = None, key = lambda x: x, reverse = False)
    return dict(map(lambda x:
                    (x, Number(x[0], Numbers[x[0]], None, getNumberLocation(screenSize, Numbers[x[0]]), width, height, True, x[1]))
                    , zip(tmp, inits)))

def getNumberLocation(screenSize, numberIndex):
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    stepHori = screenWidth / 20
    stepVert = screenHeight / 20
    return [stepHori * 5 * ( -numberIndex - 1), stepVert * 5]