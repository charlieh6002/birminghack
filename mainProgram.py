from config import *

import pygame
pygame.init()

class Game:

    def __init__(self):
        self.window = window

    def newGame(self):
        pass

clock = pygame.time.Clock()
game = Game()
game.newGame()
running = True

tick = 0

def centerx(x):
    extrax = screenWidth - x
    newx = extrax / 2
    return newx

def centery(y):
    extray = screenHeight - y
    newy = extray / 2
    return newy

#------MAIN-LOOP------

while running:
    tick += 1
    if tick == 60:
        tick = 0
    window.blit(backgroundImageScaled, (centerx(backgroundImageScaled.get_width()), 0))
    if 0 <= tick < 10 or 20 <= tick < 30 or 40 <= tick < 50:
        window.blit(titleText1, titleRect)
    else:
        window.blit(titleText2, titleRect)

    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get(): #iterates through possible events
            if event.type == pygame.KEYDOWN: 
                pass
            elif event.type == pygame.QUIT:
                pygame.quit()