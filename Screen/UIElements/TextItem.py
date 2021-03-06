# -*- coding:utf-8 -*-
from UIElement import *
from Dicts import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class TextItem(UIElement):
    def __init__(self, name, index, Location, active, textStr, textFontSize):
        UIElement.__init__(self, name, index, Location, 0, 0, active)
        self.textFont = pygame.font.SysFont('simsun',textFontSize)
        self.textStr = textStr
        self.text = self.textFont.render(textStr.decode(), True, (10, 10, 10))
        self.rect = pygame.Rect(Location[0], Location[1], textFontSize * 4, textFontSize)

    def changeColorToRed(self):
        self.text = self.textFont.render(self.textStr.decode(), True, (255, 10, 10))
    def changeColorToDark(self):
        self.text = self.textFont.render(self.textStr.decode(), True, (10, 10, 10))

    def cursorInsideText(self, point):
        return self.rect.collidepoint(point[0], point[1])

    def changeText(self, textStr):
        self.text = self.text = self.textFont.render(textStr.decode(), True, (255, 0, 0))

def CreateTextDict(screenSize, textLines, indexes, active):
    tmp = map(lambda x: x[0], sorted(indexes.iteritems(), key = lambda x: x[1], reverse = True))
    return dict(map(lambda x: (x[0],
                               TextItem(x[0], indexes[x[0]], getTextLocation(screenSize, indexes[x[0]]), active, x[1], getTextSize(screenSize, indexes[x[0]]))),
                               zip(tmp, textLines)))

def getTextLocation(screenSize, index):
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    stepHori = screenWidth / 20
    stepVert = screenHeight / 20

    if -9 <= index <= -6: #index for schedule
        return [stepHori * 3, stepVert * ( - index - 1) * 2]

    elif index == -10: #index for weather reminder
        return [stepHori * 3, stepVert * 18]

    elif -25 <= index <= -11:
        return [stepHori * 1, stepVert * ( - index - 6) ]

    elif 50 <= index <= 54:
        return [stepHori * 14, stepVert * (( index - 45) * 2 - 3)]

def getTextSize(screenSize, index):
    if -9 <= index <= -6: #index for schedule
        return screenSize[0] / 20

    elif index == -10: #index for weather reminder
        return screenSize[0] / 20

    elif -25 <= index <= -11: #index for news
        return screenSize[0] / 40

    elif 50 <= index <= 54: #index for song list
        return screenSize[0] / 20

def CreateTextOne(screenSize, textStr, index, active):
    return TextItem('WeatherReminder', index, getTextLocation(screenSize, index), active, textStr, screenSize[0] / 20)