import pygame
import threading
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
        if self.elems != None:
            tmp = self.elems.values()
            tmp.sort(cmp = None, key = lambda x: x.index, reverse = True)
            map(self.displayOne, tmp)

    def displayOne(self, elem):
        if elem.active == True:
            if elem.img == None:
                try:
                    elem.loadImg()
                except Exception as err:
                    print err
            self.screen.blit(elem.img, elem.location)

    def addElem(self, key, value):
        self.elems[key] = value

    def removeElem(self, key):
        del self.elems[key]

    def addDict(self, otherDict):
        if self.elems == None:
            self.elems = otherDict
        else:
            self.elems = dict(self.elems, **otherDict)
