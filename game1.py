# coding=utf-8
import sys, pygame
import parse
from utils import calc_offset

pygame.init()

try:
    gamemap = parse.parse_map("test.tmx")
    image = gamemap.tilesets[0].image
except:
    print "error: skrev du in rätt filnamn?"
    raise

width = int(gamemap.width) * int(gamemap.tilewidth)
height = int(gamemap.height) * int(gamemap.tileheight)
size = width, height
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

image = gamemap.tilesets[0].image
try:
    tileset = pygame.image.load(image.source)
except:
    print "error: hittar inte bildfilen"
    raise

tiles = []
for tile in gamemap.layers[0].tiles:
    tiles.append(int(tile))

rectX = 50
rectY = height - 50
velX, velY = 0, 0
speed = 0.5
jump = False

def render_map():
    worldH, worldW = int(gamemap.height), int(gamemap.width)
    posX, posY = 0, 0
    i = 0
    for tile in tiles:
        offset = calc_offset(tile, image)
        screen.blit(tileset, (posX, posY), offset)
        if i == (worldW - 1):
            posX = 0
            posY += 16
            i = 0
        else:
            posX += 16
            i += 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    dt = clock.tick(60)
    
    pressed = pygame.key.get_pressed()

    velX = 0
    if pressed[pygame.K_LEFT]:
        velX = -speed
    if pressed[pygame.K_RIGHT]:
        velX = speed

    if (velY == 0) and pressed[pygame.K_SPACE]:
        velY = -0.8
        jump = True
    if jump and velY < 0.8:
       velY += 0.05
    elif rectY > (height - 50):
        velY = 0
        rectY = height - 50
        jump = False

    rectX += velX * dt
    rectY += velY * dt

    screen.fill(black)
    # renderar banan
    render_map()
    # renderar spelaren
    pygame.draw.rect(screen, white, (rectX, rectY, 50, 50), 0)
    pygame.display.flip()
