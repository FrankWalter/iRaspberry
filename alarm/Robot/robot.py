import pygame
import random
import thread
import time
import util.voice
import sys
Faces = ('smile', 'smile2', 'angry', 'contempt', 'crafty', 'cute'\
             , 'love', 'shy', 'threaten')

Weathers = ('sunny', 'cloudy', 'overcast', 'rain', 'snow', 'fog')

Buttons = ("feed", "pet", "punish", "alarm", "music", "news",   "weather")

ISOTIMEFORMAT="%Y-%m-%d %X"

class robot():

    def __init__(self, screen):
        self.screen = screen
        self.number = []
        self.buttons = []
        self.weatherImg = []
        self.facesImg = []
        self.screenHight = screen.get_height()
        self.screenWidth = screen.get_width()
        self.buttonSize = self.screenWidth / 6

        self.loadImg()

        self.initFace()
        self.initWeather()



        # 3 stands for alarm
        # 4 stands for music
        # 5 stands for news
        # 6 stands for weather
        # 7 stands for just displaying face
        self.Func = 7

        # 0 stands for nothing
        # 1 stands for feed
        # 2 stands for pet
        # 3 stands for punish
        self.Treat = 0

        try :
            thread.start_new_thread(self.bottonListener, ())
            thread.start_new_thread(self.performTreatAndFunc, ())

        except Exception as err:
            print err

    def loadImg(self):
        for i in range(0,10):
            path = '../resources/img/numbers/%i.png'%i
            tmp = pygame.image.load(path).convert()
            self.number.append(pygame.transform.scale(tmp, (self.screenWidth / 5, self.screenHight / 5)))

        for i in range(0, len(Buttons)):
            path = '../resources/img/buttons/' + Buttons[i] + '.png'
            tmp = pygame.image.load(path).convert()
            array = []
            array.append(pygame.transform.scale(tmp, (self.buttonSize, self.buttonSize)))
            self.buttons.append(array)

        for i in range(0, len(Faces)):
            tmp = pygame.image.load('../resources/img/' + Faces[i] + '.png').convert()
            tmp = pygame.transform.scale(tmp, (self.screenWidth, self.screenHight))
            self.facesImg.append(tmp)

        for i in range(0, len(Weathers)):
            tmp = pygame.image.load('../resources/img/' + Weathers[i] + '.png').convert()
            tmp = pygame.transform.scale(tmp, (self.screenWidth, self.screenHight))
            self.weatherImg.append(tmp)

    def initFace(self):
        self.faceImg = self.facesImg[0]

    def initWeather(self):
        self.weatherImg = self.weatherImg[0]

    def changeFace(self, faceImg):
        self.faceImg = faceImg

    def changeWeather(self, weatherImg):
        self.weatherImg = weatherImg

    def performTreatAndFunc(self):
        while True:
            if self.Treat == 1:
                self.feedMe()
                self.Treat = 0

            elif self.Treat == 2:
                self.petMe()
                self.Treat = 0

            elif self.Treat == 3:
                self.punishMe()
                self.Treat = 0

            if self.Func == 3:
                self.displayClock()

            elif self.Func == 4:
                self.displayPlayer()

            elif self.Func == 5:
                self.displayNews()

            elif self.Func == 6:
                self.displayWeather()

            elif self.Func == 7:
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
        for i in range(0, 7):
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
        self.screen.blit(self.number[hour / 10], location1)
        self.screen.blit(self.number[hour % 10], location2)
        self.screen.blit(self.number[minute / 10], location4)
        self.screen.blit(self.number[minute % 10], location5)

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
        self.screen.blit(self.number[hour / 10], location1)
        self.screen.blit(self.number[hour % 10], location2)
        self.screen.blit(self.number[minute / 10], location4)
        self.screen.blit(self.number[minute % 10], location5)

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
        self.screen.blit(self.number[hour / 10], location1)
        self.screen.blit(self.number[hour % 10], location2)
        self.screen.blit(self.number[minute / 10], location4)
        self.screen.blit(self.number[minute % 10], location5)

        if second % 2 == 0:
            pygame.draw.circle(self.screen, [205, 0, 0], location31, self.screenWidth / 45)
            pygame.draw.circle(self.screen, [205, 0, 0], location32, self.screenWidth / 45)

    def displayWeather(self):
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
        self.screen.blit(self.number[hour / 10], location1)
        self.screen.blit(self.number[hour % 10], location2)
        self.screen.blit(self.number[minute / 10], location4)
        self.screen.blit(self.number[minute % 10], location5)

        if second % 2 == 0:
            pygame.draw.circle(self.screen, [205, 0, 0], location31, self.screenWidth / 45)
            pygame.draw.circle(self.screen, [205, 0, 0], location32, self.screenWidth / 45)

    def speak(self, sentence):
        util.voice.speak(sentence)


    def bottonListener(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print "enter"
                    # for i in range(0, len(self.buttons)):
                    #     if self.buttons[i][1][0]<= event.pos[0] <= self.buttons[i][1][0] + self.buttonSize and self.buttons[i][1][1]<= event.pos[1] <= self.buttons[i][1][1] + self.buttonSize:
                    #         if i >= 3:
                    #             self.Func = i
                    #         else:
                    #             self.Treat = i + 1
                    #             print self.Treat
                elif event.type == pygame.QUIT:
                    print "quit!"
                    pygame.quit()
                    sys.exit()





