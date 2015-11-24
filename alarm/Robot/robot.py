import pygame
import main
import random
import thread
import time
import util.Voice
faceIndex = ('smile', 'smile2', 'angry', 'contempt', 'crafty', 'cute'\
             , 'love', 'shy', 'threaten')
faces = {'smile':'smile', 'smile2': 'smile2', 'angry':'angry', \
         'contempt': 'contempt', 'crafty': 'crafty', 'cute': 'cute',\
         'love': 'love', 'shy': 'shy', 'threaten': 'threaten'}
weathers = {'sunny': 'sunny', 'cloudy': 'cloudy', 'overcast': 'overcast'\
    , 'light_rain': 'light_rain', 'moderate_rain': 'moderate_rain',\
            'heavy_rain': 'heavy_rain', 'moderate_snow': 'moderate_snow',\
            'heavy_snow': 'heavy_snow', 'light_snow': 'light_snow', 'fog': 'fog'}
ISOTIMEFORMAT="%Y-%m-%d %X"
class robot():

    def __init__(self, screen):
        self.screen = screen
        self.initFace()
        self.initWeather()
        self.faceOrWeather = 0 #decide what to display
                               # 0 stands for face and 1 stands for weather
        try :
            thread.start_new_thread(self.displayWeather, ())
            thread.start_new_thread(self.displayFace, ())
 #           thread.start_new_thread(self.mood, ())
        except Exception as err:
            print err

    def initFace(self):
        self.face = faces['smile']
        self.faceImg = pygame.image.load('../resources/img/' + self.face + '.png').convert()
        self.faceImg = pygame.transform.scale(self.faceImg, (main.screenWidth, main.screenHight))

    def initWeather(self):
        self.weather = weathers['fog']
        self.weatherImg = pygame.image.load('../resources/img/' + self.weather + '.png').convert()
        self.weatherImg = pygame.transform.scale(self.weatherImg, (main.screenWidth, main.screenHight))

    def changeFace(self, face):
        self.face = face
        self.faceImg = pygame.image.load('../resources/img/' + self.face + '.png').convert()
        self.faceImg = pygame.transform.scale(self.faceImg, (main.screenWidth, main.screenHight))

    def changeWeather(self, weather):
        self.weather = weather
        self.weatherImg = pygame.image.load('../resources/img/' + self.weather + '.png').convert()
        self.weatherImg = pygame.transform.scale(self.weatherImg, (main.screenWidth, main.screenHight))

    def displayImg(self, img, location):
        self.screen.blit(img,location)

    def displayFace(self):
        location = [0, 0]
        while True:
            if self.faceOrWeather == 0:
                self.displayImg(self.faceImg, location)
                pygame.display.flip()

    def displayWeather(self):
        location = [0,0]
        while True:
            if self.faceOrWeather == 1:
                self.displayImg(self.weatherImg, location)
                self.displayClock()
                pygame.display.flip()

    def displayClock(self):
        location = [0, main.screenHight / 2]
        my_font = pygame.font.SysFont(None, main.screenWidth / 8)
        textstr = time.strftime( ISOTIMEFORMAT, time.localtime() )
        text_screen = my_font.render(textstr, True, (255, 0, 0))
        self.displayImg(text_screen, location)

    def speak(self, sentence):
        util.Voice.speak(sentence)

    def mood(self):
        while True:
            time.sleep(2)
            self.faceOrWeather = random.randint(0, 1)







