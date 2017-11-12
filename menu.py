import pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,200)
gray = (200, 200, 200)

class menu:

    def __init__(self, options, z, w):
        self.eixo_x = z
        self.eixo_y = w
        self.menutext = options
        self.pointer = 0
    def createmenu(self):
        self.textFont = pygame.font.Font('ffmenu.ttf', 40)
        self.x_backup = self.eixo_x
        self.y_backup = self.eixo_y
        self.i = 0
        self.rectHeights = []
        self.rectWidths = []
        self.biggestwidth = 0
        self.optCoordinates = []
        for each in self.menutext:
            self.textSurface = self.textFont.render(each, True, white, blue)
            self.rectHeights.append(self.textSurface.get_height())
            self.rectWidths.append(self.textSurface.get_width())
            if self.textSurface.get_width() > self.biggestwidth:
                self.biggestwidth = self.textSurface.get_width()
            self.i+=1
        pygame.draw.rect(gameDisplay, blue, (self.eixo_x-80, self.eixo_y-11, 89+self.biggestwidth, sum(self.rectHeights)+2*len(self.menutext)+20))
        pygame.draw.rect(gameDisplay, gray, (self.eixo_x-80, self.eixo_y-11, 89+self.biggestwidth, sum(self.rectHeights)+2*len(self.menutext)+20), 9)
        self.i = 0
        while self.i <= len(self.menutext)-1:
            self.textSurface = self.textFont.render(self.menutext[self.i], True, white, blue)
            gameDisplay.blit(self.textSurface, (self.eixo_x,self.y_backup))
            self.optCoordinates.append([self.eixo_x - 40, self.y_backup])
            self.y_backup = self.y_backup + self.rectHeights[self.i] + 2
            self.i+=1

    def menucursor(self):
        gameDisplay.blit(cursor, self.optCoordinates[self.pointer])
