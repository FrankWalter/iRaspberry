import time
from UIElements.ClockNumber import *
from UIElements.Dicts import *
import threading
import pygame
class ClockFunc(threading.Thread):
    ISOTIMEFORMAT="%Y-%m-%d %X"
    ClockNumbers = ClockNumberDict
    def __init__(self, context):
        threading.Thread.__init__(self)
        # stepHori = self.screenWidth / 20
        # stepVert = self.screenHight / 20
        # location31 = [stepHori / 4 * 40, stepVert * 6]
        # location32 = [stepHori / 4 * 40,  stepVert * 8]

        self.now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min
        second = now.tm_sec

        self.numberDict = CreateClockNumberDict(context.getScreenSize(), self.ClockNumbers, (hour / 10, hour % 10, minute / 10, minute % 10))
        context.addDictForDisplay(self.numberDict)
    def run(self):
        while True:
            now = time.localtime()
            hour = now.tm_hour
            minute = now.tm_min
            second = now.tm_sec
            if(now, hour, minute, second) != (self.now, self.hour, self.minite, self.second)


    # def displayClock(self):
    #
    #
    #     if second % 2 == 0:
    #         pygame.draw.circle(self.screen, [205, 0, 0], location31, self.screenWidth / 45)
    #         pygame.draw.circle(self.screen, [205, 0, 0], location32, self.screenWidth / 45)