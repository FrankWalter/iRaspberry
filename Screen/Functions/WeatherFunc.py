import time
from UIElements.Dicts import *
from UIElements.Background import *
from UIElements.TextItem import *
from Utils.weather import *
import threading
import pygame
class WeatherFunc():
    ISOTIMEFORMAT="%Y-%m-%d %X"
    Weathers = WeatherIndex
    def __init__(self, context):
        self.context = context

        self.BGDict = CreateBGDict(self.context.getScreenSize(), self.Weathers)

        self.context.addDictForDisplay(self.BGDict)
        self.funcInUse = True

        fileObj = open('Resources/database/weather/cache.txt')
        self.weather = fileObj.read()

        self.createReminer()

    def createReminer(self):
        fileObj = open('Resources/database/weather/' + self.weather + 'R.txt')
        reminderStr = fileObj.read()
        self.reminder = CreateTextOne(self.context.getScreenSize(), reminderStr, WeatherReminderIndex, True)
        self.context.addElemForDisplay(self.reminder)

    def setElemInactive(self, elem):
        elem.active = False

    def setElemActive(self, elem):

        if elem.name == self.weather:
            elem.active = True
        else:
            elem.active = False

    def turnOffFunc(self):
        self.funcInUse = False
        map(lambda x: self.setElemInactive(x) ,self.BGDict.values() + self.BGDict.values() )
        self.reminder.active = False

    def turnOnFunc(self):
        self.funcInUse = True
        map(lambda x: self.setElemActive(x) ,self.BGDict.values() + self.BGDict.values() )
        self.reminder.active = True



