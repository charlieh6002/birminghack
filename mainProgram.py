from config import *
import pikepdf
import os
import pygame
pygame.init()
pygame.mixer.init()

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

#if 0 == 1:
#    try:
#        new_file = open("repaired_pdf.pdf", "r")
#        print("file opened")
#    except FileNotFoundError:
#        new_file = open("repaired_pdf.pdf", "x")
#        print("file created")
#    broken_file = "broken1.pdf"
#    new_file.close()

#def repair_pdf(input_path, output_path):
#    try:
#        new_file = open(output_path, "x")
#        with pikepdf.open(input_path, allow_overwriting_input=True) as pdf:
#            pdf.save(output_path)
#        #print("Repaired PDF saved to:", output_path)
#        new_file.close()
#    except Exception as e:
#        print("Repair failed:", e)

#repair_pdf(broken_file, "repaired_pdf.pdf")

def repairHeader(inPath, outPath, fileType):
    #PNG header should be 89 50 4E 47  
    header = b'\x00\x00\x00\x00'
    if fileType == "png" or fileType == "pdf" or fileType == "jpeg" or fileType == "jfif" : 
        if fileType == "png":
            header = b'\x89\x50\x4E\x47'
        elif fileType == "pdf":
            header = b'\x25\x50\x44\x46'
        elif fileType == "jpeg" or fileType == "jfif":
            header = b'\xFF\xD8\xFF\xE0' 
    else : 
        raise ValueError("Not a suppported fileType")

    with open(inPath, 'rb') as file: # opens a file called 'file' in the input location and reads it as binary, closes the file immediately after 
        content = file.read() #stores the bytes of the file in content 
    
    if len(content) < 4:
        raise ValueError("File is too small to be a PNG")

    fixedHeader = header + content[4:]

    with open(outPath, 'wb') as file:
        file.write(fixedHeader)
    #print("Success!  file saved to: " + outPath)

screen = 1
loadingTick = 0

channel1.play

#------MAIN-LOOP------

while running:
    tick += 1
    if tick == 60:
        tick = 0

    if screen == 2:
        loadingTick += 1
        if loadingTick == 300:
            screen = 3
            channel1.play(wowSound)
            channel2.play(revivedSound)
            channel3.play(sparkleSound)
        
    #text
    if screen ==1:
        window.blit(backgroundImageScaled, (centerx(backgroundImageScaled.get_width()), 0))
        window.blit(drop,dRect)
        window.blit(file,fRect)
        window.blit(here,hRect)
        window.blit(deadFileImageScaled, (-50, 375))

    elif screen == 2:
        #do loading screen
        if 0 <= loadingTick < 30 or 60 <= loadingTick < 90:
            window.blit(l1Scaled, (centerx(l1Scaled.get_width()), 0))
        else:
            window.blit(l2Scaled, (centerx(l2Scaled.get_width()), 0))


    elif screen == 3:
        window.blit(happybackgroundImageScaled, (centerx(backgroundImageScaled.get_width()), 0))
        window.blit(aliveFileImageScaled, (120, 100))
        window.blit(nextFile, nextFileRect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    channel1.play(knockedSound, 0, 3)
                    screen = 1
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
                channel1.play(loadingSound)
                corruptedFile = event.file
                #print(corruptedFile)
                splitFile = corruptedFile.split("/") #filename.filetype 
                newFileName = splitFile[len(splitFile) - 1] 
                corruptFileType = newFileName[1] 
                newFileName = newFileName[:-4] + "-REPAIRED." + corruptFileType
                repairHeader(corruptedFile, newFileName, corruptFileType)
                screen = 2
                #repair_pdf(corruptedFile, newFileName)
            elif event.type == pygame.QUIT:
                pygame.quit()


#add something to select the filetype which is filename[-4:] 
#add other filetype corrections to the function
