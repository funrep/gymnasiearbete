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

image = gamemap.tilesets[0].image
tileset = pygame.image.load(image.source)

tiles = []
for tile in gamemap.layers[0].tiles:
    tiles.append(int(tile))


def calc_offset(gid, img):
    columns = int(img.width) / 16
    rows = int(img.height) / 16
    tile_count = columns * rows
    tileX, tileY = 0, 0
    i = 0
    while tileX < columns:
        # print "Gid %d Iter %d x: %d y: %d" % (gid, i, tileX, tileY)
        if i == gid:
            return (16 * tileX, 16 * tileY, 16, 16)
        elif tileX == (columns - 1):
            tileX = 0
            tileY += 1
        else:
            tileX += 1
        i += 1

# surfaces = []
# for tile in tiles:
#     offset = calc_offset(tile, image)
#     print str(offset)
#     surfaces.append(tileset.subsurface(offset))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    posX, posY = 0, 0
    tileW, tileH = gamemap.tilewidth, gamemap.tileheight
    i = 0
    for tile in tiles:
        offset = calc_offset(tile, image)
        screen.blit(tileset, (posX, posY), offset)
        if i == tileW:
            posX = 0
            posY += 16
            i = 0
        else:
            posX += 16
            i += 1

    pygame.display.flip()
