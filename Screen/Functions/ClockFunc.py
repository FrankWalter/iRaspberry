import time
class ClockFunc():
    ISOTIMEFORMAT="%Y-%m-%d %X"
    def __init__(self, screen, displayer):
        self.screen = screen
        self.displayer = displayer
        self.screenHight = screen.get_height()
        self.screenWidth = screen.get_width()
    def displayClock(self):
        self.screen.fill([255, 255, 255])
        stepHori = self.screenWidth / 20
        stepVert = self.screenHight / 20
        location1 = [0, stepVert * 5]
        location2 = [stepHori * 5, stepVert * 5]
        location31 = [stepHori / 4 * 40, stepVert * 6]
        location32 = [stepHori / 4 * 40,  stepVert * 8]
        location4 = [stepHori * 10, stepVert * 5]
        location5 = [stepHori * 15, stepVert * 5]
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min
        second = now.tm_sec
        self.screen.blit(self.numbers[hour / 10], location1)
        self.screen.blit(self.numbers[hour % 10], location2)
        self.screen.blit(self.numbers[minute / 10], location4)
        self.screen.blit(self.numbers[minute % 10], location5)

        if second % 2 == 0:
            pygame.draw.circle(self.screen, [205, 0, 0], location31, self.screenWidth / 45)
            pygame.draw.circle(self.screen, [205, 0, 0], location32, self.screenWidth / 45)