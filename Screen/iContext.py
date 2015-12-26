import Display.Displayer
from Functions.FuncHandler import *
import os
import os
import pygame
class iContext():
    def createScreen(self, screenWidth, screenHight):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
        self.screen = pygame.display.set_caption('Screen!')
        self.screen = pygame.display.set_mode((screenWidth, screenHight), pygame.NOFRAME)
        self.screen.fill([255,255,255])
        return self.screen
    def getScreenSize(self):
        return (self.screen.get_width(), self.screen.get_height())
    def createDisplayer(self):
        self.displayer = Display.Displayer.Displayer(self, None)
        return self.displayer
    def createFuncHdl(self):
        self.funcHdl = FuncHandler(self)
        return self.funcHdl
    def addDictForDisplay(self, ddict):
        self.displayer.addDict(ddict)
