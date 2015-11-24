# coding=utf8
import pygame
import sys
from pygame.locals import *

from Robot.robot import *

screenHight = 500
screenWidth = 500
def sleep_by_counter(threshold):
    i = 0;
    while i < threshold:
        i += 1
    return

def terminate():
    pygame.quit()
    sys.exit()
def initScreen():
    screen = pygame.display.set_caption('Alarm Robot!')
    screen = pygame.display.set_mode([screenWidth, screenHight], pygame.NOFRAME)
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
    rob.speak("肥料掺了金坷垃一带能顶两袋撒")

