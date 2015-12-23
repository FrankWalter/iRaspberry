# coding=utf8
import pygame
import os
import thread
import Event.EventListener
import Display.Displayer
from pygame.locals import *
from Functions.FuncHandler import *

screenHight = 350
screenWidth = 475
# the values of the dict are used for layer, you can see the utilization of the values in Displayer.displayAll


def initScreen():
    #force the screen to be displayed in full window
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
    screen = pygame.display.set_caption('Screen!')
    screen = pygame.display.set_mode((screenWidth, screenHight), pygame.NOFRAME)
    screen.fill([255,255,255])
    return screen


if __name__=='__main__':
    pygame.init()
    screen = initScreen()
    # create a displayer for displaying
    displayer = Display.Displayer.Displayer(screen, None)
    displayer.start()

    funcHdl = FuncHandler(screen, displayer)

    #must implement EventListener this way.
    try:
        thread.start_new_thread(Event.EventListener.EventListener(funcHdl), ())
    except Exception as err:
        print err


    #rob.speak("肥料掺了金坷垃一带能顶两袋撒")

