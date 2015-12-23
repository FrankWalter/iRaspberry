import pygame
import sys

def EventHandler(event, funcHdl):
    if event.type == pygame.MOUSEBUTTONDOWN:
        # check if it's a Func switching command
        for k, v in funcHdl.buttonDict.items():
            if v.cursorInsideButton([event.pos[0], event.pos[1]]):
                print k
        for k, v in funcHdl.robotFunc.buttonDict.items():
            if v.cursorInsideButton([event.pos[0], event.pos[1]]):
                print k
    elif event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
