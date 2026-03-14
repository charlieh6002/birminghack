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
titleText1 = pixeboyMedium.render("file ressurector", True, (255,255,255))
titleText2 = pixeboyMedium.render("file ressurector", True, (100,100,100))
titleRect = titleText1.get_rect(center = (screenWidth/2, 128))

backgroundImage = pygame.image.load("assets/tombstone.png")
backgroundImageScaled = pygame.transform.scale_by(backgroundImage, 8.1)
