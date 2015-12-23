import pygame
from RobotFunc import *
from ClockFunc import *
from NewsFunc import *
from MusicFunc import *
from UIElements.Button import *
from UIElements.Background import *
class FuncHandler():
    Funcs = {'Alarm': 3, 'Music': 4, 'News': 5, 'Weather': 6, 'Face': 7}
    def __init__(self, screen, displayer):
        self.screen = screen
        self.Funcs = self.Funcs
        self.displayer = displayer
        # self.Backgrounds = Backgrounds

        self.buttonDict = CreateButtonDict(screen, self.Funcs)
        self.displayer.addDict(self.buttonDict)
        #
        # self.backgroundDict = CreateBGDict(screen, self.Backgrounds)
        # self.displayer.addDict(self.backgroundDict)

        self.robotFunc = RobotFunc(screen, self.displayer)
        self.clockFunc = ClockFunc(screen, self.displayer)
        # self.NewsFunc = NewsFunc(screen, self.displayer)


