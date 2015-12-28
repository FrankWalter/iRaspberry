from UIElements.Dicts import *
from UIElements.Background import *
from UIElements.TextItem import *
from Utils.news import *
from UIElements.Dicts import *
class NewsFunc():
    ISOTIMEFORMAT="%Y-%m-%d %X"
    News = NewsIndex
    Background = NewsBackGround
    def __init__(self, context):
        self.context = context
        self.funcInUse = True
        self.BG = CreateBGOne(self.context.getScreenSize(), 'paperbackground', self.Background, False)
        self.context.addElemForDisplay(self.BG)
        # fileObj = open('Resources/database/weather/cache.txt')
        # self.weather = fileObj.read()

        self.createNews()

    def createNews(self):
        # fileObj = open('Resources/database/weather/' + self.weather + 'R.txt')
        # reminderStr = fileObj.read()
        newsLines = getNews()
        self.newsDict = CreateTextDict(self.context.getScreenSize(), newsLines, NewsIndex, True)
        self.context.addDictForDisplay(self.newsDict)

    def setElemInactive(self, elem):
        elem.active = False

    def setElemActive(self, elem):
        elem.active = True

    def turnOffFunc(self):
        self.funcInUse = False
        map(lambda x: self.setElemInactive(x) ,self.newsDict.values())
        self.BG.active = False

    def turnOnFunc(self):
        self.funcInUse = True
        map(lambda x: self.setElemActive(x) ,self.newsDict.values() )
        self.BG.active = True



