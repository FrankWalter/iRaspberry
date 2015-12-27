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
        self.context = context
        # the function layer may should not aware of the screen layer, but we
        # need the screenSize for evenListening
        self.buttonDict = CreateButtonDict(context.getScreenSize(), self.Funcs)
        context.addDictForDisplay(self.buttonDict)
        self.clockFunc = ClockFunc(self.context)
        self.clockFunc.start()
        # self.backgroundDict = CreateBGDict(screen, self.Backgrounds)
        # self.displayer.addDict(self.backgroundDict)



    # def switchFunc(self, funcName):
    #
    # def createFuncManager(self):
    #     funcManager = {}
    #     sorted(self.Funcs.iteritems(), key = lambda x: x[1], reverse = False)
    #     self.robotFunc = RobotFunc(self.context)
    #     funcManager = zip(tmp, )
    #     self.clockFunc = ClockFunc(self.context)
    #     self.clockFunc.start()
    #     # self.NewsFunc = NewsFunc(screen, self.displayer)