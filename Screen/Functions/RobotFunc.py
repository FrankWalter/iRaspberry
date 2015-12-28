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
        self.facesDict['smile'].active = True

    def feedMe(self):
        print "feed"

    def petMe(self):
        print "pet"

    def punishMe(self):
        print "punish"

    def setElemInactive(self, elem):
        elem.active = False

    def setElemActive(self, elem):
        elem.active = True

    def turnOffFunc(self):
        self.funcInUse = False
        map(lambda x: self.setElemInactive(x) ,self.facesDict.values() + self.buttonDict.values() )

    def turnOnFunc(self):
        self.funcInUse = True
        map(lambda x: self.setElemActive(x) ,self.facesDict.values() + self.buttonDict.values() )
    # def speak(self, sentence):
    #     util.voice.speak(sentence)








