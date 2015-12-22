import Button
import pygame
import os
def CreateButtonDict(screen, buttonTuple):
    height = screen.get_height()
    width = screen.get_width()
    return dict(map(lambda x:
                    (buttonTuple[x], Button.Button(buttonTuple[x], loadImg(buttonTuple[x], width, height), getButtonLocation(screen, x), width, height))
                    , range(0, len(buttonTuple))))

def loadImg(x, width, height):
    return pygame.transform.scale(pygame.image.load('Resources/img/buttons/' + x + '.png').convert(), (width, height))

def getButtonLocation(screen, buttonIndex):
    screenHeight = screen.get_height()
    screenWidth = screen.get_width()
    stepHori = width / 20
    stepVert = height / 20
    return [stepHori * (2 + (buttonIndex - 3) * 4), stepVert * 1]