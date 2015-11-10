import sys, pygame
import parse

pygame.init()

gamemap = parse.parse_map("test.tmx")

width = int(gamemap.width) * int(gamemap.tilewidth)
height = int(gamemap.height) * int(gamemap.tileheight)
size = width, height

black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

tiles = pygame.image.load(gamemap.tileset[0].image.source)

calc_offset(gid, img):
    tile_count = calc_tiles(img)
    columns = img.width / 16
    rows = img.height / 16
    w, h = 0, 0
    for i in range(0, tile_count):
        if foobar(i, columns, tile_count):
            h += 1
        if i == gid:
            return (16 * (i - (columns * h)), 16 * h, 16, 16)

foobar(x,y,z):
    for i in range(0, z):
        if x == y * i:
            return True
    return False

calc_tiles(img):
    columns = img.width / 16
    rows = img.height / 16
    return columns * rows

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    pygame.display.flip()
