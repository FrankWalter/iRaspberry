import pygame
import threading
# import RobotFunc
import sys
from UIElements.ButtonElem.Button import *
from UIElements.ButtonElem.CreateButtonDict import *
class FuncHandler():
    Funcs = {'Alarm': 3, 'Music': 4, 'News': 5, 'Weather': 6, 'Face': 7}
    def __init__(self, screen):
        buttonTuple = ("alarm", "music", "news", "weather", "return")
        self.buttonDict = CreateButtonDict(screen, buttonTuple)
        # self.robotFunc = RobotFunc.RobotFunc(screen)

# class buttonListener(threading.Tread):
#     def __init__(self, buttonDict):
#         threading.Thread.__init__(self)
#         self.buttonDict = buttonDict
#     def run(self):

