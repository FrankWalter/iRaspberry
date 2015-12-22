import pygame
import random
import thread
import time
import util.voice
import sys
faceIndex = ('smile', 'smile2', 'angry', 'contempt', 'crafty', 'cute'\
             , 'love', 'shy', 'threaten')
Faces = {'smile':'smile', 'smile2': 'smile2', 'angry':'angry', \
         'contempt': 'contempt', 'crafty': 'crafty', 'cute': 'cute',\
         'love': 'love', 'shy': 'shy', 'threaten': 'threaten'}
Weathers = {'sunny': 'sunny', 'cloudy': 'cloudy', 'overcast': 'overcast'\
    , 'light_rain': 'light_rain', 'moderate_rain': 'moderate_rain',\
            'heavy_rain': 'heavy_rain', 'moderate_snow': 'moderate_snow',\
            'heavy_snow': 'heavy_snow', 'light_snow': 'light_snow', 'fog': 'fog'}
Buttons = ("feed", "pet", "punish", "alarm", "music", "news",   "weather")
ISOTIMEFORMAT="%Y-%m-%d %X"

class robot():

    def __init__(self, screen):
        self.screen = screen
        self.number = []
        self.buttons = []

        self.screenHight = screen.get_height()
        self.screenWidth = screen.get_width()
        self.initFace()
        self.initWeather()
        self.buttonSize = self.screenWidth / 6
        self.loadImg()

        self.Func = 0
        #decide what action to perform
        # 0 stands for feed
        # 1 stands for pet
        # 2 stands for punish
        # 3 stands for alarm
        # 4 stands for music
        # 5 stands for news
        # 6 stands for weather

        try :
            thread.start_new_thread(self.performFunc, ())
            thread.start_new_thread(self.bottonListener(), ())
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
    def initFace(self):
        self.face = Faces['smile']
        self.faceImg = pygame.image.load('../resources/img/' + self.face + '.png').convert()
        self.faceImg = pygame.transform.scale(self.faceImg, (self.screenWidth, self.screenHight))

    def initWeather(self):
        self.weather = Weathers['fog']
        self.weatherImg = pygame.image.load('../resources/img/' + self.weather + '.png').convert()
        self.weatherImg = pygame.transform.scale(self.weatherImg, (self.screenWidth, self.screenHight))

    def changeFace(self, face):
        self.face = face
        self.faceImg = pygame.image.load('../resources/img/' + self.face + '.png').convert()
        self.faceImg = pygame.transform.scale(self.faceImg, (self.screenWidth, self.screenHight))

    def changeWeather(self, weather):
        self.weather = weather
        self.weatherImg = pygame.image.load('../resources/img/' + self.weather + '.png').convert()
        self.weatherImg = pygame.transform.scale(self.weatherImg, (self.screenWidth, self.screenHight))

    def performFunc(self):
        location = [0, 0]
        while True:
            if self.Func == 0:
                self.screen.blit(self.faceImg, location)
                self.displayButtons()
                self.feedMe()

            elif self.Func == 1:
                self.screen.blit(self.weatherImg, location)
                self.displayButtons()
                self.petMe()

            elif self.Func == 2:
                self.screen.blit(self.weatherImg, location)
                self.displayButtons()
                self.punishMe()

            elif self.Func == 3:
                self.displayClock()

            elif self.Func == 4:
                self.displayPlayer()

            elif self.Func == 5:
                self.displayNews()

            elif self.Func == 6:
                self.displayWeather()

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
                for i in range(0, len(self.buttons)):
                    if self.Func == event.type == pygame.MOUSEBUTTONDOWN and self.buttons[i][1][0]<= event.pos[0] <= self.buttons[i][1][0] + self.buttonSize and self.buttons[i][1][1]<= event.pos[1] <= self.buttons[i][1][1] + self.buttonSize:
                        print "click!%d" %i
                        self.Func = i
                    elif event.type == pygame.QUIT:
                        print "quit!"
                        pygame.quit()
                        sys.exit()





