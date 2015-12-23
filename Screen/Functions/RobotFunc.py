import Utils.voice
from UIElements.Button import *
from UIElements.Background import *
from Func import *
class RobotFunc(Func):
    Treats = {'Feed': 0, 'Pet': 1, 'Punish': 2}
    Faces = {'smile': 8, 'smile2': 9, 'angry':10, \
         'contempt': 11, 'crafty': 12, 'cute': 13,\
         'love': 14, 'shy': 15, 'threaten': 16}
    def __init__(self, screen, displayer):
        self.screen = screen
        self.facesDict = CreateBGDict(screen, self.Faces)
        self.buttonDict = CreateButtonDict(screen, self.Treats)
        displayer.addDict(self.facesDict)
        displayer.addDict(self.buttonDict)
        self.screenHight = screen.get_height()
        self.screenWidth = screen.get_width()
        # self.initFace()

    def initFace(self):
        self.facesDict['smile'].active = True

    def feedMe(self):
        print "feed"

    def petMe(self):
        print "pet"

    def punishMe(self):
        print "punish"

    def speak(self, sentence):
        util.voice.speak(sentence)








