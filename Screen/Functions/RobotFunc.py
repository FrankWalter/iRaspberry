import Utils.voice
from UIElements.Button import *
from UIElements.Background import *
from UIElements.Dicts import *
import threading
class RobotFunc(threading.Thread):
    Treats = TreatsButtonDict
    Faces = FacesBackgroundDict
    def __init__(self, context):
        threading.Thread.__init__(self)
        self.context = context
        self.facesDict = CreateBGDict(context.getScreenSize(), self.Faces)
        self.buttonDict = CreateButtonDict(context.getScreenSize(), self.Treats)
        context.addDictForDisplay(self.facesDict)
        context.addDictForDisplay(self.buttonDict)

        self.infoDict = {}
        self.loadInfo()
        self.infoDict['Hp'] = self.infoDict['Happy'] * 0.2 + self.infoDict['Starving'] * 0.8
        self.moodCalculate()
    def loadInfo(self):
        fileObj = open('Resources/database/robot/info.txt')
        fileLines = fileObj.readlines()
        fileLines = map(lambda x: (x.split(' ')[0], int(x.split(' ')[1][: -1])), fileLines)
        self.infoDict = dict(fileLines)

    def TreatRobot(self, treat):
        if treat == 'Feed':
            self.feedMe()
        elif treat == 'Pet':
            self.petMe()
        elif treat == 'Punish':
            self.punishMe()
    def feedMe(self):
        self.infoDict['Starving'] += 2
        self.moodCalculate()

    def petMe(self):
        self.infoDict['Happy'] += 1
        self.moodCalculate()

    def punishMe(self):
        self.infoDict['Happy'] -= 3
        self.moodCalculate()

    def setElemInactive(self, elem):
        elem.active = False

    def setElemActive(self, elem):
        if elem.name == self.mood or 0 <= elem.index <= 2:
            elem.active = True

    def turnOffFunc(self):
        self.funcInUse = False
        map(lambda x: self.setElemInactive(x) ,self.facesDict.values() + self.buttonDict.values() )

    def turnOnFunc(self):
        self.funcInUse = True
        map(lambda x: self.setElemActive(x) ,self.facesDict.values() + self.buttonDict.values() )
    # def speak(self, sentence):
    #     util.voice.speak(sentence)

    def moodCalculate(self):
        self.infoDict['Hp'] = self.infoDict['Happy'] * 0.5 + self.infoDict['Starving'] * 0.5
        if self.infoDict['Hp'] < 0:
            self.infoDict['Hp'] = 0
        Hp = self.infoDict['Hp']
        if 0 <= Hp < 10:
            self.mood = 'threaten'
        elif 10 <= Hp < 20:
            self.mood = 'angry'
        elif 20 <= Hp < 30:
            self.mood = 'contempt'
        elif 30 <= Hp < 40:
            self.mood = 'shy'
        elif 40 <= Hp < 50:
            self.mood = 'cute'
        elif 50 <= Hp < 60:
            self.mood = 'crafty'
        elif 60 <= Hp < 70:
            self.mood = 'smile'
        elif 70 <= Hp < 80:
            self.mood = 'smile2'
        elif 80 <= Hp < 100:
            self.mood = 'love'

        map(lambda x: self.setElemInactive(x) ,self.facesDict.values())
        self.facesDict[self.mood].active = True
        print self.infoDict['Hp']








