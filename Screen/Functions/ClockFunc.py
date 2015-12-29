import time
import urllib2
from UIElements.ClockNumber import *
from UIElements.TextItem import *
from UIElements.Dicts import *
from UIElements.Button import *
import Utils.voice
import threading
import pygame
class ClockFunc(threading.Thread):
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

        self.closeAlarmButton = CreateButtonOne(self.context.getScreenSize(), 'closealarm', CloseAlarm, True)

        self.getScheduleText()
        self.getAlarmTime()

        self.context.addDictForDisplay(self.numberDict)
        self.context.addDictForDisplay(self.scheduleText)
        self.context.addElemForDisplay(self.colon)
        self.context.addElemForDisplay(self.closeAlarmButton)
        self.funcInUse = True
        self.shutDownSignal = False
    def run(self):
        time.sleep(1)
        while True:
            if self.funcInUse == True:
                now = time.localtime()
                hour = now.tm_hour
                minute = now.tm_min
                second = now.tm_sec

                ahour = self.alarmTime.tm_hour
                aminute = self.alarmTime.tm_min
                if (hour, minute) == (ahour, aminute) and self.shutDownSignal == False and not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load("Resources/voice/alarm.mp3")
                    pygame.mixer.music.play(1)

                if minute > aminute:
                    self.shutDownSignal = False

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
        self.setElemInactive(self.closeAlarmButton)

    def turnOnFunc(self):
        self.funcInUse = True
        map(lambda x: self.setElemActive(x) ,self.numberDict.values() + self.scheduleText.values() )
        self.setElemActive(self.colon)
        self.setElemActive(self.closeAlarmButton)

    def getScheduleText(self):
        req = urllib2.Request('http://4c.rokiy.com/%d-%d-%d.txt'%(self.year, self.mon, self.day))
        resp = urllib2.urlopen(req)
        content = resp.read()
        fileLines = content.split('\n')
        self.scheduleText = CreateTextDict(self.context.getScreenSize(), fileLines, ScheduleIndex, True)

    def getAlarmTime(self):
        req = urllib2.Request('http://4c.rokiy.com/alarm.txt')
        resp = urllib2.urlopen(req)
        content = resp.readlines()
        self.alarmTime = time.localtime(int(content[1]))
        self.alarmText = content[2]
        Utils.voice.speak(self.alarmText)
    def closeAlarm(self):
        self.shutDownSignal = True