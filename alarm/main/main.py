# coding=utf8
import pygame, sys, random
from pygame.locals import *
import Robot
screenHight = 500
screenWidth = 500
def sleep_by_counter(threshold):
    i = 0;
    while i < threshold:
        i += 1
    return

def initScreen():
    screen = pygame.display.set_caption('Alarm Robot!')
    screen = pygame.display.set_mode([screenWidth, screenHight], pygame.NOFRAME)
    screen.fill([255,255,255])
    return screen
if __name__=='__main__':
    pygame.init()
    screen = initScreen()
    rob = Robot.robot()
    rob.speak("我从未见过有如此厚颜无耻之人")

