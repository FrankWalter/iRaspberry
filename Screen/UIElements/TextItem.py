# -*- coding:utf-8 -*-
from UIElement import *
from Dicts import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class TextItem(UIElement):
    def __init__(self, name, index, Location, active, textStr, textFont):
        UIElement.__init__(self, name, index, Location, 0, 0, active)
        self.textFont = textFont
        self.text = self.textFont.render(textStr.decode(), True, (255, 0, 0))

    def changeText(self, textStr):
        self.text = self.text = self.textFont.render(textStr.decode(), True, (255, 0, 0))

def createTextItem(screenSize, textLines, index, active):
    textFont = pygame.font.SysFont('宋体',screenSize[0] / 20)
    tmp = map(lambda x: x[0], sorted(ScheduleIndex.iteritems(), key = lambda x: x[1], reverse = True))
    return dict(map(lambda x: (x[0],
                               TextItem(x[0], ScheduleIndex[x[0]], getTextLocation(screenSize, ScheduleIndex[x[0]]), active, x[1], textFont)),
                               zip(tmp, textLines)))

def getTextLocation(screenSize, index):
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    stepHori = screenWidth / 20
    stepVert = screenHeight / 20

    if -9 <= index <= -6:
        return [stepHori * 3, stepVert * ( - index ) * 2]
