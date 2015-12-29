#coding=utf8
import pygame
import os
import thread
import Event.EventListener
import iContext

from pygame.locals import *


screenHight = 295
screenWidth = 475


if __name__=='__main__':
    pygame.init()
    pygame.mixer.init()
    context = iContext.iContext()

    screen = context.createScreen(screenWidth, screenHight)
    # create a displayer for displaying
    displayer = context.createDisplayer()
    funcHdl = context.createFuncHdl()
    displayer.start()
    #must implement EventListener this way.
    try:
        thread.start_new_thread(Event.EventListener.EventListener(context), ())
    except Exception as err:
        print err