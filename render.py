import sys, pygame
import parse

pygame.init()

gamemap = parse.parse_map("test.tmx")
image = gamemap.tilesets[0].image

width = int(gamemap.width) * int(gamemap.tilewidth)
height = int(gamemap.height) * int(gamemap.tileheight)
size = width, height

black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

tiles = pygame.image.load(gamemap.tilesets[0].image.source)

def calc_offset(gid, img):
    columns = int(img.width) / 16
    rows = int(img.height) / 16
    tile_count = columns * rows
    tileX, tileY = 1, 1 
    i = 1
    while tileX <= columns:
        if i == gid:
            return (16 * tileX, 16 * tileY, 16, 16)
        elif tileX == columns:
            tileX = 1
            tileY += 1
        else:
            tileX += 1
        i += 1

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#     screen.fill(black)
#     pygame.display.flip()
