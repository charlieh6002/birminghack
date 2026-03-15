import pygame
pygame.init()
pygame.mixer.init()

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
titleRect = titleText1.get_rect(center = (screenWidth/2, 64))

backgroundImage = pygame.image.load("assets/tombstone.png")
backgroundImageScaled = pygame.transform.scale_by(backgroundImage, 8.1)
happybackgroundImage = pygame.image.load("assets/happytombstone.png")
happybackgroundImageScaled = pygame.transform.scale_by(happybackgroundImage, 8.1)

loadingImage1 = pygame.image.load("assets/loading1.png")
l1Scaled = pygame.transform.scale_by(loadingImage1, 8.1)
loadingImage2 = pygame.image.load("assets/loading2.png")
l2Scaled = pygame.transform.scale_by(loadingImage2, 8.1)
loadingRect = loadingImage1.get_rect(center = (screenWidth/2, screenHeight/2))

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

#BUTTONS

jpeg = pixeboySmall.render("jpeg", True, (255,255,255))
jfif = pixeboySmall.render("jfif", True, (255,255,255))
png = pixeboySmall.render("png", True, (255,255,255))
pdf = pixeboySmall.render("pdf", True, (255,255,255))
jpegTextRect = jpeg.get_rect(center = (216, 160))
jfifTextRect = jfif.get_rect(center = (432, 160))
pngTextRect = png.get_rect(center = (648, 160))
pdfTextRect = pdf.get_rect(center = (864, 160))

jpegRect = pygame.rect.Rect(216, 128, 200, 64)
jpegRect.center = (216, 160)
jfifRect = pygame.rect.Rect(432, 128, 200, 64)
jfifRect.center = (432, 160)
pngRect = pygame.rect.Rect(648, 128, 200, 64)
pngRect.center = (648, 160)
pdfRect = pygame.rect.Rect(864, 128, 200, 64)
pdfRect.center = (864, 160)

#SOUNDS

wowSound = pygame.mixer.Sound("assets/anime-wow-sound-effect.mp3")
wowSound.set_volume(0.8)

revivedSound = pygame.mixer.Sound("assets/fortnite-revive.mp3")
revivedSound.set_volume(0.8)

loadingSound = pygame.mixer.Sound("assets/loading.mp3")
loadingSound.set_volume(0.8)

sparkleSound = pygame.mixer.Sound("assets/sparkle.mp3")
sparkleSound.set_volume(0.8)

knockedSound = pygame.mixer.Sound("assets/knocked.mp3")
knockedSound.set_volume(0.8)

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)