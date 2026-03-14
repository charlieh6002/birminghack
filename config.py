import pygame
pygame.init()

screenWidth = 1080
screenHeight = 720
window = pygame.display.set_mode((screenWidth, screenHeight))

#fonts
pixeboyLarge = pygame.font.Font("assets/Pixeboy.ttf", 150)
pixeboyMedium = pygame.font.Font("assets/Pixeboy.ttf", 100)
pixeboySmall = pygame.font.Font("assets/Pixeboy.ttf", 50)

#images

#title 
titleText1 = pixeboyMedium.render("pdf resurrector", True, (255,255,255))
titleText2 = pixeboyMedium.render("pdf resurrector", True, (100,100,100))
titleRect = titleText1.get_rect(center = (screenWidth/2, 128))

backgroundImage = pygame.image.load("assets/tombstone.png")
backgroundImageScaled = pygame.transform.scale_by(backgroundImage, 8.1)
happybackgroundImage = pygame.image.load("assets/happytombstone.png")
happybackgroundImageScaled = pygame.transform.scale_by(happybackgroundImage, 8.1)


deadFileImage = pygame.image.load("assets/deadfile.png")
deadFileImageScaled = pygame.transform.scale_by(deadFileImage, 10)
aliveFileImage = pygame.image.load("assets/aliveFile.png")
aliveFileImageScaled = pygame.transform.scale_by(aliveFileImage, 10)

#drop file here 
drop = pixeboySmall.render("drop", True, (255,255,255))
file = pixeboySmall.render("file", True, (255,255,255))
here = pixeboySmall.render("here", True, (255,255,255))
dRect = drop.get_rect(center = (screenWidth/2, screenHeight/2 + 32))
fRect = file.get_rect(center = (screenWidth/2, screenHeight/2 + 32 + 64))
hRect = here.get_rect(center = (screenWidth/2, screenHeight/2 + 32 + 128))

nextFile = pixeboySmall.render("press enter to upload another file", True, (255,255,255))
nextFileRect = nextFile.get_rect(center = (screenWidth/2, 600))