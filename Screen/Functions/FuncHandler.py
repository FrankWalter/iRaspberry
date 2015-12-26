import pygame
from RobotFunc import *
from ClockFunc import *
from NewsFunc import *
from MusicFunc import *
from UIElements.Button import *
from UIElements.Background import *
from UIElements.Dicts import *
class FuncHandler():
    Funcs = FuncsButtonDict
    def __init__(self, context):
        # the function layer may should not aware of the screen layer, but we
        # need the screenSize for evenListening
        self.buttonDict = CreateButtonDict(context.getScreenSize(), self.Funcs)
        context.addDictForDisplay(self.buttonDict)
        #
        # self.backgroundDict = CreateBGDict(screen, self.Backgrounds)
        # self.displayer.addDict(self.backgroundDict)

        self.robotFunc = RobotFunc(context)
        self.clockFunc = ClockFunc(context)
        # self.NewsFunc = NewsFunc(screen, self.displayer)


