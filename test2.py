import pygame
import time
import spritesheet
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,200)
gray = (200, 200, 200)
transparentbg = (0, 64, 128)
pink = (255, 0, 255)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('test')
clock = pygame.time.Clock()
ATBCOUNTER = pygame.USEREVENT+2
pygame.time.set_timer(ATBCOUNTER, 33)
WALKANIMATION = pygame.USEREVENT+1
pygame.time.set_timer(WALKANIMATION, 100)

bg1 = pygame.image.load('betterbg.png').convert()
bg2 = pygame.image.load('betterbg.png').convert()
fg1 = pygame.image.load('foreground.png').convert()
fg2 = pygame.image.load('foreground.png').convert()
fg1.set_colorkey(transparentbg)
fg2.set_colorkey(transparentbg)
atbfont = pygame.font.Font('ffmenu.ttf', 45)

class character:
    def __init__(self, name,commandname, filename, level,  attack, defense, speed, maxhp, evasion, power):
        self.name = name
        self.commandname = commandname
        self.spritelist = []
        sheet = spritesheet.spritesheet(filename)
        self.spritelist = sheet.load_strip((0,0,96,96), 13, colorkey=(255, 255, 255))
        self.walkanim = [2,0,1,0]
        self.a = 0
        self.atk = attack
        self.defe = defense
        self.spd = speed
        self.maxhp = maxhp
        self.curhp = maxhp
        self.evasion = evasion
        self.level = level
        self.power = power
        self.atbspeed = 0
    def walk(self):
        if self.a == 3:
            self.a = 0
        else:
            self.a += 1
        return self.a
    def atb_formula(self):
        self.atbspeed = (96 * (spd + 20))/16
        return self.atbspeed


def draw_atb_bar(characterparty, x, y):
    for each in characterparty:
        nameSurface = atbfont.render(each.name, True, white, blue)
        hpSurface = atbfont.render(str(each.curhp), True, white, blue)
        nameHeight = nameSurface.get_height()
        gameDisplay.blit(nameSurface,(x,y))
        gameDisplay.blit(hpSurface,(800-(140+hpSurface.get_width()),y))
        pygame.draw.rect(gameDisplay, gray, (display_width - 140, y+14, 130, 10),3)
        y += nameHeight



class enemy:
    def __init__(self, sprite, attack, defense, speed, hp):
        self.atk = attack
        self.defe = defense
        self.spd = speed
        self.hp = hp
        self.image = pygame.image.load(sprite).convert()
        self.atbspeed = 0
    def atb_formula(self):
        self.atbspeed = ((96 *(spd +20))*(255-(1*24)))/16
        return self.atbspeed


def damageformula(str, atk, defe):
    crit = False
    notcrit = 31/32
    if random.randint(1,33) == 32:
         crit = True
    if not crit:
        damage = (str*2 + atk)
    else:
        damage = (str*2 + atk)*2
    variance = random.randint(224, 255)
    damage = ((damage * variance)/256)+1
    damage = (damage *(255 - defe)/256)+1
    return damage




shadow = character('Shadow','Ninjutsu', 'shadow_sprite.png',11, 39, 124, 40, 252, 0.28, 105)
sabin = character('Sabin','Blitz', 'sabin_sprite.png',12, 47, 117, 37, 289, 0.12, 81)
cyan = character('Cyan','Bushido', 'cyan_sprite.png',13, 40, 123, 28, 358, 0.06, 82)
boss = enemy('train.png', 10, 30, 30, 1900)
boss.image.set_colorkey(pink)

battleMenu = ['Attack','Defend','     ','Item']

cursor = pygame.image.load('Cursor.png')


party = [shadow, sabin, cyan]

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


def draw_screen(x, x2):
    gameDisplay.blit(bg1, (x, 0))
    gameDisplay.blit(bg2, (x-1474, 0))
    gameDisplay.blit(sabin.spritelist[sabin.walkanim[sabin.a]], (130, 200))
    gameDisplay.blit(shadow.spritelist[shadow.walkanim[shadow.a]], (43, 240))
    gameDisplay.blit(cyan.spritelist[cyan.walkanim[cyan.a]], (210, 150))
    gameDisplay.blit(boss.image, (display_width - 327, display_height - 600))
    gameDisplay.blit(fg1, (x2, 0))
    gameDisplay.blit(fg2, (x2 - 2511, 0))
    pygame.draw.rect(gameDisplay, blue, (0,400, display_width, display_height))
    pygame.draw.line(gameDisplay, gray, (0,400),(800,400), 9)
    pygame.draw.line(gameDisplay, gray, (250,400),(250,600), 9)


def game_loop():
    gameExit = False
    x = 0
    x2 = 0
    while not gameExit:
        draw_screen(x, x2)
        draw_atb_bar(party, 300, 420)

        battmenu.createmenu()
        battmenu.menucursor()
        pygame.display.update()
        x += 10
        x2 += 8
        if x >= 1474:
            x = 0
        if x2 >= 2511:
            x2 = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == WALKANIMATION:
                sabin.walk()
                shadow.walk()
                cyan.walk()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN and battmenu.pointer < len(battmenu.optCoordinates)-1:
                    battmenu.pointer += 1

                if event.key == pygame.K_UP and battmenu.pointer > 0:
                    battmenu.pointer -= 1

        clock.tick(60)

game_loop()
pygame.quit()
quit()
