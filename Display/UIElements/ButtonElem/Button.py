import pygame
class Button():
    def __init__(self, name, img, Location, width, height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(Location[0], Location[1], self.width, self.height)
        self.img = img
        self.name = name

    def cursorInsideButton(self, point):
        return self.rect.collidepoint(point[0], point[1])
