import pygame
import random
import thread
import time
import Util.voice
import Util.weather
import sys
Faces = ('smile', 'smile2', 'angry', 'contempt', 'crafty', 'cute'\
             , 'love', 'shy', 'threaten')

Weathers = Util.weather.weatherSet

Treats = {'Notreat': 0, 'Feed': 1, 'Pet': 2, 'Punish': 3}

ISOTIMEFORMAT="%Y-%m-%d %X"

class RobotFunc():
    def __init__(self, screen):
        self.screen = screen
        self.numbers = []
        self.buttons = []
        self.weatherImgs = {}
        self.facesImgs = []
        self.screenHight = screen.get_height()
        self.screenWidth = screen.get_width()
        self.buttonSize = self.screenWidth / 6

        self.loadImg()

        self.initFace()

        self.Func = Funcs['Face']
        self.Treat = Treats['Notreat']

        print Weathers
        try :

            thread.start_new_thread(self.performTreatAndFunc, ())
            thread.start_new_thread(self.bottonListener(), ())

        except Exception as err:
            print err

    def loadImg(self):
        for i in range(0,10):
            path = '../resources/img/numbers/%i.png'%i
            tmp = pygame.image.load(path).convert()
            self.numbers.append(pygame.transform.scale(tmp, (self.screenWidth / 5, self.screenHight / 5)))

        for i in range(0, len(Buttons)):
            path = '../resources/img/buttons/' + Buttons[i] + '.png'
            tmp = pygame.image.load(path).convert()
            array = []
            array.append(pygame.transform.scale(tmp, (self.buttonSize, self.buttonSize)))
            self.buttons.append(array)

        for i in range(0, len(Faces)):
            tmp = pygame.image.load('../resources/img/' + Faces[i] + '.png').convert()
            tmp = pygame.transform.scale(tmp, (self.screenWidth, self.screenHight))
            self.facesImgs.append(tmp)

        self.weatherImgs = dict(
                                    map(
                                            lambda x:
                                                     (x, pygame.transform.scale(pygame.image.load('../resources/img/' + x + '.png').convert(), (self.screenWidth, self.screenHight))),
                                                     Weathers.keys()))
        print self.weatherImgs

    def initFace(self):
        self.faceImg = self.facesImgs[0]

    def performTreatAndFunc(self):
        while True:
            if self.Treat == Treats['Feed']:
                self.feedMe()
                self.Treat = Treats['Notreat']

            elif self.Treat == Treats['Pet']:
                self.petMe()
                self.Treat = Treats['Notreat']

            elif self.Treat == Treats['Punish']:
                self.punishMe()
                self.Treat = Treats['Notreat']

            if self.Func == Funcs['Alarm']:
                self.displayClock()

            elif self.Func == Funcs['Music']:
                self.displayPlayer()

            elif self.Func == Funcs['News']:
                self.displayNews()

            elif self.Func == Funcs['Weather']:
                self.displayWeather()

            elif self.Func == Funcs['Face']:
                self.screen.blit(self.faceImg, [0, 0])
                self.displayButtons()

            pygame.display.flip()

    def feedMe(self):
        print "feed"

    def petMe(self):
        print "pet"

    def punishMe(self):
        print "punish"

    def displayButtons(self):
        stepHori = self.screenWidth / 20
        stepVert = self.screenHight / 20

        for i in range(0, 3):
            self.buttons[i].append([stepHori * (3 + i * 5), stepVert * 15])
        for i in range(3, 7):
            self.buttons[i].append([stepHori * (2 + (i - 3) * 4), stepVert * 1])
        self.buttons[7].append([stepHori * 16, stepVert * 8])
        for i in range(0, len(self.buttons)):
            self.screen.blit(self.buttons[i][0], self.buttons[i][1])

    def displayClock(self):
        self.screen.fill([255, 255, 255])
        stepHori = self.screenWidth / 20
        stepVert = self.screenHight / 20
        location1 = [0, stepVert * 5]
        location2 = [stepHori * 5, stepVert * 5]
        location31 = [stepHori / 4 * 40, stepVert * 6]
        location32 = [stepHori / 4 * 40,  stepVert * 8]
        location4 = [stepHori * 10, stepVert * 5]
        location5 = [stepHori * 15, stepVert * 5]
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min
        second = now.tm_sec
        self.screen.blit(self.numbers[hour / 10], location1)
        self.screen.blit(self.numbers[hour % 10], location2)
        self.screen.blit(self.numbers[minute / 10], location4)
        self.screen.blit(self.numbers[minute % 10], location5)

        if second % 2 == 0:
            pygame.draw.circle(self.screen, [205, 0, 0], location31, self.screenWidth / 45)
            pygame.draw.circle(self.screen, [205, 0, 0], location32, self.screenWidth / 45)

    def displayPlayer(self):
        self.screen.fill([255, 255, 255])
        stepHori = self.screenWidth / 20
        stepVert = self.screenHight / 20
        location1 = [0, stepVert * 5]
        location2 = [stepHori * 5, stepVert * 5]
        location31 = [stepHori / 4 * 40, stepVert * 6]
        location32 = [stepHori / 4 * 40,  stepVert * 8]
        location4 = [stepHori * 10, stepVert * 5]
        location5 = [stepHori * 15, stepVert * 5]
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min
        second = now.tm_sec
        self.screen.blit(self.numbers[hour / 10], location1)
        self.screen.blit(self.numbers[hour % 10], location2)
        self.screen.blit(self.numbers[minute / 10], location4)
        self.screen.blit(self.numbers[minute % 10], location5)

        if second % 2 == 0:
            pygame.draw.circle(self.screen, [205, 0, 0], location31, self.screenWidth / 45)
            pygame.draw.circle(self.screen, [205, 0, 0], location32, self.screenWidth / 45)

    def displayNews(self):
        self.screen.fill([255, 255, 255])
        stepHori = self.screenWidth / 20
        stepVert = self.screenHight / 20
        location1 = [0, stepVert * 5]
        location2 = [stepHori * 5, stepVert * 5]
        location31 = [stepHori / 4 * 40, stepVert * 6]
        location32 = [stepHori / 4 * 40,  stepVert * 8]
        location4 = [stepHori * 10, stepVert * 5]
        location5 = [stepHori * 15, stepVert * 5]
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min
        second = now.tm_sec
        self.screen.blit(self.numbers[hour / 10], location1)
        self.screen.blit(self.numbers[hour % 10], location2)
        self.screen.blit(self.numbers[minute / 10], location4)
        self.screen.blit(self.numbers[minute % 10], location5)

        if second % 2 == 0:
            pygame.draw.circle(self.screen, [205, 0, 0], location31, self.screenWidth / 45)
            pygame.draw.circle(self.screen, [205, 0, 0], location32, self.screenWidth / 45)

    def displayWeather(self):
        self.screen.fill([255, 255, 255])
        wt = util.weather.getWeather()
        print wt
        self.screen.blit(self.weatherImgs[wt], [0, 0])

    def speak(self, sentence):
        util.voice.speak(sentence)








