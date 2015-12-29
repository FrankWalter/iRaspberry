from UIElements.TextItem import *
from UIElements.Dicts import *
from UIElements.Button import *
from UIElements.Background import *
import threading
import pygame
class MusicFunc():
    def __init__(self, context):
        self.context = context
        fileObj = open('Resources/database/music/songs.txt')
        songNames = fileObj.readlines()
        self.songListDict = CreateTextDict(self.context.getScreenSize(), songNames, SongListDict, True)
        self.ctrButtonDict = CreateButtonDict(context.getScreenSize(), MusicControlButtonDict)
        self.background = CreateBGOne(context.getScreenSize(), 'musicback', MusicBackground, True)
        self.context.addDictForDisplay(self.songListDict)
        self.context.addDictForDisplay(self.ctrButtonDict)
        self.context.addElemForDisplay(self.background)
        self.songListTuples = map(lambda x: x, sorted(self.songListDict.iteritems(), key = lambda x: x[1].index, reverse = False))
        self.currentSongIndex = 0
        self.funcInUse = True
        self.loadMusic('yellow')
        self.ctrButtonDict['play'].active = True
        self.ctrButtonDict['pause'].active = False
        self.songListTuples[0][1].changeColorToRed()
    def loadMusic(self, musicStr):
        pygame.mixer.music.load('Resources/voice/' + musicStr + 'short.mp3')

    def setElemInactive(self, elem):
        elem.active = False

    def setElemActive(self, elem):
        elem.active = True

    def turnOffFunc(self):
        self.funcInUse = False
        map(lambda x: self.setElemInactive(x) ,self.songListDict.values() + self.ctrButtonDict.values())
        self.background.active = False
        pygame.mixer.music.stop()

    def turnOnFunc(self):
        self.funcInUse = True
        map(lambda x: self.setElemActive(x) ,self.songListDict.values() + self.ctrButtonDict.values())
        self.ctrButtonDict['play'].active = False
        self.ctrButtonDict['pause'].active = True
        self.background.active = True
        self.loadMusic('yellow')
        pygame.time.wait(100)
        pygame.mixer.music.play()

    def upDateList(self, key):
        map(lambda x: x.changeColorToDark() ,self.songListDict.values() )
        self.songListDict[key].changeColorToRed()
        for i in range(0, self.songListTuples.__len__()):
            if self.songListTuples[i][0] == key:
                self.currentSongIndex = i
                break
        pygame.mixer.music.fadeout(10)
        pygame.time.wait(100)
        self.loadMusic(self.songListDict[key].textStr[2: -1])
        pygame.time.wait(100)
        pygame.mixer.music.play()

    def performAction(self, k):
        if k == 'play':
            if self.ctrButtonDict['pause'].active:
                print "pause"
                pygame.mixer.music.pause()
                self.ctrButtonDict['pause'].active = False
                self.ctrButtonDict['play'].active = True

            elif self.ctrButtonDict['play'].active:
                pygame.mixer.music.unpause()
                print "unpause"
                self.ctrButtonDict['pause'].active = True
                self.ctrButtonDict['play'].active = False
        if k == 'next':
            newKey = self.songListTuples[(self.currentSongIndex + 1) % self.songListTuples.__len__()][0]
            self.upDateList(newKey)
