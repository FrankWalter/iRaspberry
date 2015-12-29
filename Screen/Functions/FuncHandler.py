import pygame
from RobotFunc import *
from ClockFunc import *
from WeatherFunc import *
from NewsFunc import *
from MusicFunc import *
from UIElements.Button import *
from UIElements.Background import *
from UIElements.Dicts import *
class FuncHandler():
    Funcs = FuncsButtonDict
    def __init__(self, context):
        self.context = context
        self.functionPool = {}
        # the function layer may should not aware of the screen layer, but we
        # need the screenSize for evenListening
        self.buttonDict = CreateButtonDict(context.getScreenSize(), self.Funcs)
        context.addDictForDisplay(self.buttonDict)

        self.clockFunc = ClockFunc(self.context)
        self.robotFunc = RobotFunc(self.context)
        self.weatherFunc = WeatherFunc(self.context)
        self.newsFunc = NewsFunc(self.context)
        self.musicFunc = MusicFunc(self.context)
        self.functionPool['ClockFunc'] = self.clockFunc
        self.functionPool['RobotFunc'] = self.robotFunc
        self.functionPool['WeatherFunc'] = self.weatherFunc
        self.functionPool['NewsFunc'] = self.newsFunc
        self.functionPool['MusicFunc'] = self.musicFunc
        self.clockFunc.start()

        self.swithTo('RobotFunc')
    def swithTo(self, funcStr):
        map(lambda x: x.turnOffFunc(), self.functionPool.values())
        self.functionPool[funcStr].turnOnFunc()
   #     self.robotFunc.start()
