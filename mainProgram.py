from config import *
import pikepdf
import os
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

if 0 == 1:
    try:
        new_file = open("repaired_pdf.pdf", "r")
        print("file opened")
    except FileNotFoundError:
        new_file = open("repaired_pdf.pdf", "x")
        print("file created")
    broken_file = "broken1.pdf"
    new_file.close()

def repair_pdf(input_path, output_path):
    try:
        new_file = open(output_path, "x")
        with pikepdf.open(input_path, allow_overwriting_input=True) as pdf:
            pdf.save(output_path)
        #print("Repaired PDF saved to:", output_path)
        new_file.close()
    except Exception as e:
        print("Repair failed:", e)

#repair_pdf(broken_file, "repaired_pdf.pdf")

fileUploaded = False

#------MAIN-LOOP------

while running:
    tick += 1
    if tick == 60:
        tick = 0
    
    
    #text
    if not fileUploaded:
        window.blit(backgroundImageScaled, (centerx(backgroundImageScaled.get_width()), 0))
        window.blit(drop,dRect)
        window.blit(file,fRect)
        window.blit(here,hRect)
        window.blit(deadFileImageScaled, (400, 200))

    if fileUploaded:
        window.blit(happybackgroundImageScaled, (centerx(backgroundImageScaled.get_width()), 0))
        window.blit(aliveFileImageScaled, (400, 200))
        #do anime thing
        
    if 0 <= tick < 30:
        window.blit(titleText1, titleRect)
    else:
        window.blit(titleText2, titleRect)

    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get(): #iterates through possible events
            if event.type == pygame.KEYDOWN: 
                pass
            if event.type == pygame.DROPFILE:
                corruptedFile = event.file
                print(corruptedFile)
                splitFile = corruptedFile.split("/")
                newFileName = splitFile[len(splitFile) - 1]
                newFileName = newFileName[:-4] + "-REPAIRED.pdf"
                fileUploaded = True
                repair_pdf(corruptedFile, newFileName)
            elif event.type == pygame.QUIT:
                pygame.quit()