import pygame
from UIElement import *
class Background(UIElement):
    def __init__(self, name, index, Location, width, height, active):
        UIElement.__init__(self, name, index, Location, width, height, active)
        self.img = None
    def loadImg(self):
        self.img =  pygame.transform.scale(pygame.image.load('Resources/img/' + self.name.lower() + '.png').convert(), (self.width, self.height))
#Factory Method
def CreateBGDict(screenSize, Bgs):
    width = screenSize[0]
    height = screenSize[1]
    return dict(map(lambda x:
                    (x, Background(x, Bgs[x], [0, 0], width, height, False))
                    , Bgs.keys()))

#Factory Method