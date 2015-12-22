# coding=utf8
import pygame
import os
import sys

from pygame.locals import *
from Functions.FuncHandler import *

screenHight = 350
screenWidth = 475

def initScreen():
    #force the screen to be displayed in full window
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
    screen = pygame.display.set_caption('Display!')
    screen = pygame.display.set_mode((screenWidth, screenHight), pygame.NOFRAME)
    screen.fill([255,255,255])
    return screen

if __name__=='__main__':
    pygame.init()
    screen = initScreen()
    funcHdl = FuncHandler(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for k,v in funcHdl.buttonDict.items():
                    print [event.pos[0], event.pos[1]]
                    print v.rect
                    if v.cursorInsideButton([event.pos[0], event.pos[1]]):
                        print k
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    #rob.speak("肥料掺了金坷垃一带能顶两袋撒")

