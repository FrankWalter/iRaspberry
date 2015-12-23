import pygame
import threading
import sys
import time
import EventHandler
def EventListener(funcHdl):
    while True:
        for event in pygame.event.get():
            EventHandler.EventHandler(event, funcHdl)
