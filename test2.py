import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,200)
gray = (200, 200, 200)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('test')
clock = pygame.time.Clock()

bg1 = pygame.image.load('background.png').convert()
bg2 = pygame.image.load('background.png').convert()


battleMenu = ['Attack','Defend','Magic','Item']
cursor = pygame.image.load('Cursor.png')





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

battmenu = menu(battleMenu, 100,420)


def game_loop():
    gameExit = False
    x = 0

    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN and battmenu.pointer < len(battmenu.optCoordinates)-1:
                    battmenu.pointer += 1

                if event.key == pygame.K_UP and battmenu.pointer > 0:
                    battmenu.pointer -= 1

        gameDisplay.blit(bg1, (x, 0))
        gameDisplay.blit(bg2, (x-display_width, 0))

        pygame.draw.rect(gameDisplay, blue, (0,400, display_width, display_height))
        pygame.draw.line(gameDisplay, gray, (0,400),(800,400), 9)
        pygame.draw.line(gameDisplay, gray, (250,400),(250,600), 9)
        battmenu.createmenu()
        battmenu.menucursor()


        pygame.display.update()
        x+=10
        if x >= display_width:
            x = 0

        clock.tick(60)

game_loop()
pygame.quit()
quit()
