import pygame
import threading
from UIElements.TextItem import *
class Displayer(threading.Thread):
    def __init__(self, context, elems):
        threading.Thread.__init__(self)
        self.screen = context.screen
        self.elems = elems

    def run(self):
        while True:
            self.displayAll()
            pygame.display.flip()

    def displayAll(self):
        self.screen.fill([255,255,255])
        if self.elems != None:
            tmp = map(lambda x: x[1], sorted(self.elems.iteritems(), key = lambda x: x[1].index, reverse = True))
            map(self.displayOne, tmp)

    def displayOne(self, elem):
        if elem.active == True:
            if not isinstance(elem, TextItem):
                if elem.img == None:
                    try:
                        elem.loadImg()
                    except Exception as err:
                        print err
                self.screen.blit(elem.img, elem.location)
            else:
                self.screen.blit(elem.text, elem.location)

    def addElem(self, elem):
        self.elems[elem.name] = elem

    def removeElem(self, key):
        del self.elems[key]

    def addDict(self, otherDict):
        if self.elems == None:
            self.elems = otherDict
        else:
            self.elems = dict(self.elems, **otherDict)
