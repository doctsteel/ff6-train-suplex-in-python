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


def createmenu(options,x, y):
    textFont = pygame.font.Font('ffmenu.ttf', 40)
    i = 0
    rectHeights = []
    rectWidths = []
    biggestwidth = 0
    while i <= len(options)-1:
        textSurface = textFont.render(options[i], True, white, blue)
        rectHeights.append(textSurface.get_height())
        rectWidths.append(textSurface.get_width())
        if textSurface.get_width() > biggestwidth:
            biggestwidth = textSurface.get_width()
        i+=1
    pygame.draw.rect(gameDisplay, blue, (x-80, y-11, 89+biggestwidth, sum(rectHeights)+2*len(options)+20))
    pygame.draw.rect(gameDisplay, gray, (x-80, y-11, 89+biggestwidth, sum(rectHeights)+2*len(options)+20), 9)
    i = 0
    while i <= len(options)-1:
        textSurface = textFont.render(options[i], True, white, blue)
        gameDisplay.blit(textSurface, (x,y))
        y = y + rectHeights[i] + 2
        i+=1


def game_loop():
    gameExit = False
    x = 0

    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                quit()




        gameDisplay.blit(bg1, (x, 0))
        gameDisplay.blit(bg2, (x-display_width, 0))

        pygame.draw.rect(gameDisplay, blue, (0,400, display_width, display_height))
        pygame.draw.line(gameDisplay, gray, (0,400),(800,400), 9)
        pygame.draw.line(gameDisplay, gray, (250,400),(250,600), 9)
        createmenu(battleMenu,100, 420)


        pygame.display.flip()
        x+=10
        if x >= display_width:
            x = 0

        clock.tick(60)

game_loop()
pygame.quit()
quit()
