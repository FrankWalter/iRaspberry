import pygame
import sys

def EventHandler(event, funcHdl):
    if event.type == pygame.MOUSEBUTTONDOWN:
        # check if it's a Func switching command
        for k, v in funcHdl.buttonDict.items():
            if v.cursorInsideButton([event.pos[0], event.pos[1]]):
                funcHdl.swithTo(k)
                return
        # checking for robot function
        if funcHdl.robotFunc.funcInUse:
            for k, v in funcHdl.robotFunc.buttonDict.items():
                if v.cursorInsideButton([event.pos[0], event.pos[1]]):
                    funcHdl.robotFunc.TreatRobot(k)
                    return
        for k, v in funcHdl.musicFunc.songListDict.items():
            if v.cursorInsideText([event.pos[0], event.pos[1]]):
                funcHdl.musicFunc.upDateList(k)
                return
        for k, v in funcHdl.musicFunc.ctrButtonDict.items():
            if v.cursorInsideButton([event.pos[0], event.pos[1]]):
                funcHdl.musicFunc.performAction(k)
                return
    elif event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
