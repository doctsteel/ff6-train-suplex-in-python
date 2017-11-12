import pygame
import time
import random
import pygameMenu
from pygameMenu.locals import *


# inicia o aplicativo
pygame.init()

#tamanho da janela
display_width = 800
display_height = 600
cur_width = 38
cur_height = 37

gameDisplay = pygame.display.set_mode((display_width,display_height))
#nome do jogo
pygame.display.set_caption('train suplex')
#cores
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
fontdir = pygameMenu.fonts.NEVIS
clock = pygame.time.Clock()


#carregar o cursor
curImg = pygame.image.load('Cursor.png')
shadowImg = pygame.image.load('shadow.png')
terraImg = pygame.image.load('terra.png')
#botar o cursor num ponto da imagem
def cursor(x,y):
    gameDisplay.blit(curImg, (x,y))
def characters():
    gameDisplay.blit(shadowImg, (650, 150))
    gameDisplay.blit(terraImg, (650, 250))



def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text, wid, hgt, scale):
    largeText = pygame.font.Font('freesansbold.ttf', scale)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((wid),(hgt))
    gameDisplay.blit(TextSurf, TextRect)

def crash():
    message_display('no move selected', display_width/2, display_height/2, 25)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def attackmenu(fontscale):
    message_display('Attack', 600, 500, fontscale)
def defendmenu(fontscale):
    message_display('Defend', 700, 500, fontscale)
def ninjamenu(fontscale):
    message_display('Ninjutsu', 600, 530, fontscale)
def itemmenu(fontscale):
    message_display('Item', 700, 530, fontscale)
def menu():
    fontscale = 15
    pygame.draw.rect(gameDisplay, blue, [557, 480, 175, 70])
    attackmenu(fontscale)
    defendmenu(fontscale)
    ninjamenu(fontscale)
    itemmenu(fontscale)

def menuEvent():
    pygameMenu.menu(gameDisplay, 800, 600, )



def game_loop():
    x = 530
    y = 490
    x_change = 0
    y_change = 0

#manter o estado de jogo continuo até fechar
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and x == 530:
                    x = 630
                elif event.key == pygame.K_LEFT and x == 630:
                    x = 530
                if event.key == pygame.K_RIGHT and x == 530:
                    x = 630
                elif event.key == pygame.K_RIGHT and x == 630:
                    x = 530
                elif event.key == pygame.K_UP and y == 490:
                    y = 520
                elif event.key == pygame.K_UP and y == 520:
                    y = 490
                elif event.key == pygame.K_DOWN and y == 490:
                    y = 520
                elif event.key == pygame.K_DOWN and y == 520:
                    y = 490
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         x_change = 0
            #     elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            #         y_change = 0



        gameDisplay.fill(black)
        characters()
        menu()
        cursor(x,y)


        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
