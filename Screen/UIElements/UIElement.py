import pygame
from abc import ABCMeta, abstractmethod
class UIElement():
    def __init__(self, name, index,Location, width, height, active):
        self.width = width
        self.height = height
        self.location = Location
        self.rect = pygame.Rect(Location[0], Location[1], self.width, self.height)
        self.name = name
        self.index = index
        self.active = active