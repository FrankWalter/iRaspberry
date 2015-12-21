# coding=utf8
import pygame
import os


import sys
sys.path.append('..')
from pygame.locals import *
from Robot.robot import *

screenHight = 350
screenWidth = 475

def terminate():
    pygame.quit()
    sys.exit()
def initScreen():
    #force the screen to be displayed in full window
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
    screen = pygame.display.set_caption('Alarm Robot!')
    screen = pygame.display.set_mode((screenWidth, screenHight), pygame.NOFRAME)
    screen.fill([255,255,255])
    return screen
if __name__=='__main__':
    pygame.init()
    screen = initScreen()
    rob = robot(screen)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
    #rob.speak("肥料掺了金坷垃一带能顶两袋撒")

