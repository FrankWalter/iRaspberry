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
        # stepHori = self.screenWidth / 20        self.loadImg()

        # stepVert = self.screenHight / 20
        # location31 = [stepHori / 4 * 40, stepVert * 6]
        # location32 = [stepHori / 4 * 40,  stepVert * 8]

        self.now = time.localtime()
        self.hour =  self.now.tm_hour
        self.minute =  self.now.tm_min
        self.second =  self.now.tm_sec

        self.numberDict = CreateClockNumberDict(context.getScreenSize(), self.ClockNumbers, ( self.hour / 10, self.hour % 10, self.minute / 10, self.minute % 10))
        self.colon = CreateColon(context.getScreenSize(), self.second % 2 == 0)
        context.addDictForDisplay(self.numberDict)
        context.addElemForDisplay(self.colon)
    def run(self):
        while True:
            now = time.localtime()
            hour = now.tm_hour
            minute = now.tm_min
            second = now.tm_sec
            self.colon.active = second % 2 == 0
            if(hour, minute) != (self.hour, self.minute): #update time
                self.hour = hour
                self.minute = minute
                tmp = self.numberDict.values()
                tmp.sort(cmp = None, key = lambda x: x.name, reverse = False)
                map(lambda x: x[0].changeValue(x[1]), zip(tmp, (self.hour / 10, self.hour % 10, self.minute / 10, self.minute % 10)))


    # def displayClock(self):
    #
    #
    #     if second % 2 == 0:
    #         pygame.draw.circle(self.screen, [205, 0, 0], location31, self.screenWidth / 45)
    #         pygame.draw.circle(self.screen, [205, 0, 0], location32, self.screenWidth / 45)