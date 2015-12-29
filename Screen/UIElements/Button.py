import pygame
from UIElement import UIElement
class Button(UIElement):
    def __init__(self, name, index, Location, width, height, active):
        UIElement.__init__(self, name, index, Location, width, height, active)
        self.img = None
    def cursorInsideButton(self, point):
        return self.rect.collidepoint(point[0], point[1])
    def loadImg(self):
        self.img = pygame.transform.scale(pygame.image.load('Resources/img/buttons/' + self.name.lower() + '.png').convert(), (self.width, self.height))

#Factory Method
def CreateButtonDict(screenSize, Funcs):
    width = screenSize[0] / 6
    height = screenSize[1] / 6
    return dict(map(lambda x:
                    (x, Button(x, Funcs[x], getButtonLocation(screenSize, Funcs[x]), getButtonSize(screenSize, Funcs[x])[0], getButtonSize(screenSize, Funcs[x])[1], True))
                    , Funcs.keys()))

def getButtonLocation(screenSize, buttonIndex):
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    stepHori = screenWidth / 20
    stepVert = screenHeight / 20
    if 3 <= buttonIndex <= 7: #functionbutton
        return [stepHori * (1 + (buttonIndex - 3) * 4), stepVert * 1]
    elif 0 <= buttonIndex <= 2:#treatbutton
        return [stepHori * (3 + buttonIndex * 5), stepVert * 17]
    elif 14 <= buttonIndex <= 15:
        return [stepHori * (3 + (buttonIndex - 14) * 3), stepVert * 17]

def getButtonSize(screenSize, buttonIndex):
    if 3 <= buttonIndex <= 7: #functionbutton
        return [screenSize[0] / 6, screenSize[1] / 6]
    elif 0 <= buttonIndex <= 2:#treatbutton
        return [screenSize[0] / 6, screenSize[1] / 6]
    elif 14 <= buttonIndex <= 15:
        return [screenSize[0] / 8, screenSize[1] / 8]