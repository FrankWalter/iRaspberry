import pygame
from UIElement import *
class Background(UIElement):
    def __init__(self, name, index, Location, width, height, active):
        UIElement.__init__(self, name, index, Location, width, height, active)
        self.img = None
    def loadImg(self):
        try:
            self.img =  pygame.transform.scale(pygame.image.load('Resources/img/' + self.name.lower() + '.png').convert(), (self.width, self.height))
        except Exception as err:
            print err

#Factory Method
def CreateBGDict(screenSize, Bgs):
    width = screenSize[0]
    height = screenSize[1]
    return dict(map(lambda x:
                    (x, Background(x, Bgs[x], [0, 0], width, height, False))
                    , Bgs.keys()))

def CreateBGOne(screenSize, name, index, active):
    width = screenSize[0]
    height = screenSize[1]
    stepHori = width / 20
    stepVert = height / 20
    if index != 17:
        return Background(name, index, [0, 0], width, height, active)
    else:
        return Background(name, index, [stepHori * 3, stepVert * 6], width / 3, height / 3, active)