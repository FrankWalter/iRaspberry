import pygame
from UIElement import UIElement
class Button(UIElement):
    def __init__(self, name, index, img, Location, width, height, active):
        UIElement.__init__(self, name, index, img, Location, width, height, active)
    def cursorInsideButton(self, point):
        return self.rect.collidepoint(point[0], point[1])
    def loadImg(self):
        self.img = pygame.transform.scale(pygame.image.load('Resources/img/buttons/' + self.name.lower() + '.png').convert(), (self.width, self.height))

#Factory Method
def CreateButtonDict(screen, Funcs):
    height = screen.get_height() / 6
    width = screen.get_width() / 6
    return dict(map(lambda x:
                    (x, Button(x, Funcs[x], None, getButtonLocation(screen, Funcs[x]), width, height, True))
                    , Funcs.keys()))

def getButtonLocation(screen, buttonIndex):
    screenWidth = screen.get_width()
    screenHeight = screen.get_height()
    stepHori = screenWidth / 20
    stepVert = screenHeight / 20
    if 3 <= buttonIndex <= 7:
        return [stepHori * (2 + (buttonIndex - 3) * 4), stepVert * 1]
    if 0 <= buttonIndex <= 2:
        return [stepHori * (3 + buttonIndex * 5), stepVert * 15]