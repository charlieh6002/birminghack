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

#title text

titleText = pixeboyMedium.render("file ressurector yay", True, (255,255,255))
titleRect = titleText.get_rect(center = (screenWidth/2, screenHeight/2))