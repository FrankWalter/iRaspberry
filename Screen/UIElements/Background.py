import pygame
from UIElement import *
class Background(UIElement):
    def __init__(self, name, index, img, Location, width, height, active):
        UIElement.__init__(self, name, index, img, Location, width, height, active)
    def loadImg(self):
        self.img =  pygame.transform.scale(pygame.image.load('Resources/img/' + self.name.lower() + '.png').convert(), (self.width, self.height))
    @staticmethod
    def allocLocation():
        return [0, 0]
#Factory Method
def CreateBGDict(screen, Bgs):
    height = screen.get_height()
    width = screen.get_width()
    return dict(map(lambda x:
                    (x, Background(x, Bgs[x], None, Background.allocLocation(), width, height, False))
                    , Bgs.keys()))

#Factory Method