import pygame
import main
import random
import thread
import time
import util.voice
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

        self.faceOrWeather = 0 #decide what to display
                               # 0 stands for face and 1 stands for weather
        try :
            thread.start_new_thread(self.display, ())
            thread.start_new_thread(self.bottonListener(), ())
            # thread.start_new_thread(self.mood, ())
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

    def display(self):
        location = [0, 0]
        while True:
            if self.faceOrWeather == 0:
                self.screen.blit(self.faceImg, location)
                self.displayButtons()
            elif self.faceOrWeather == 1:
                self.screen.blit(self.weatherImg, location)
            elif self.faceOrWeather == 2:
                self.displayClock()
            pygame.display.flip()

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

    def speak(self, sentence):
        util.voice.speak(sentence)

    def mood(self):
        while True:
            time.sleep(2)
            self.faceOrWeather = (self.faceOrWeather + 1) % 3


    def bottonListener(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[0][1][0]<= event.pos[0] <= self.buttons[0][1][0] + self.buttonSize:
                    print "click!"





