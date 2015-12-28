import time
from UIElements.ClockNumber import *
from UIElements.TextItem import *
from UIElements.Dicts import *
import threading
import pygame
class ClockFunc(threading.Thread):
    ISOTIMEFORMAT="%Y-%m-%d %X"
    ClockNumbers = ClockNumberDict
    def __init__(self, context):
        threading.Thread.__init__(self)
        self.context = context
        self.now = time.localtime()
        self.year = self.now.tm_year
        self.mon = self.now.tm_mon
        self.day = self.now.tm_mday
        self.hour =  self.now.tm_hour
        self.minute =  self.now.tm_min
        self.second =  self.now.tm_sec

        self.numberDict = CreateClockNumberDict(self.context.getScreenSize(),
                                                self.ClockNumbers,
                                                ( self.hour / 10, self.hour % 10, self.minute / 10, self.minute % 10, self.second / 10, self.second % 10))
        self.colon = CreateColon(self.context.getScreenSize(), False)

        fileObj = open('Resources/database/schedule/%d-%d-%d.txt'%(self.year, self.mon, self.day))
        fileLines = fileObj.readlines()
        self.scheduleText = CreateTextDict(self.context.getScreenSize(), fileLines, ScheduleIndex, True)

        self.context.addDictForDisplay(self.numberDict)
        self.context.addElemForDisplay(self.colon)
        self.context.addDictForDisplay(self.scheduleText)
        self.funcInUse = True
    def run(self):
        time.sleep(1)
        while True:
            if self.funcInUse == True:
                now = time.localtime()
                hour = now.tm_hour
                minute = now.tm_min
                second = now.tm_sec
                if(hour, minute, second) != (self.hour, self.minute, self.second): #update time
                    self.hour = hour
                    self.minute = minute
                    self.second = second
                    tmp = self.numberDict.values()
                    tmp.sort(cmp = None, key = lambda x: x.name, reverse = False)
                    map(lambda x: x[0].changeValue(x[1]),
                        zip(tmp, (self.hour / 10, self.hour % 10, self.minute / 10, self.minute % 10, self.second / 10, self.second % 10)))

    def setElemInactive(self, elem):
        elem.active = False

    def setElemActive(self, elem):
        elem.active = True

    def turnOffFunc(self):
        self.funcInUse = False
        map(lambda x: self.setElemInactive(x) ,self.numberDict.values() + self.scheduleText.values() )
        self.setElemInactive(self.colon)

    def turnOnFunc(self):
        self.funcInUse = True
        map(lambda x: self.setElemActive(x) ,self.numberDict.values() + self.scheduleText.values() )
        self.setElemActive(self.colon)


