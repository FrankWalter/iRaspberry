import pygame, sys
import main
import Voice
from pygame.locals import *
faces = {'smile':'smile', 'smile2': 'smile2', 'angry':'angry', \
         'contempt': 'contempt', 'crafty': 'crafty', 'cute': 'cute',\
         'love': 'love', 'shy': 'shy', 'threaten': 'threaten'}
class robot():
    face = faces['smile']
    def changeFace(self, face):
        self.face = face

    def displayFace(self, screen):
        img = pygame.image.load('../resources/img/' + self.face + '.png').convert()
        img = pygame.transform.scale(img, (main.screenWidth, main.screenHight))
        location=[0, 0]
        screen.blit(img,location)
        pygame.display.flip()

    def speak(self, sentence):
        Voice.speak(sentence)

