import pygame

def calc_offset(gid, img):
    columns = int(img.width) / 16
    rows = int(img.height) / 16
    tile_count = columns * rows
    tileX, tileY = 0, 0
    gid -= 1
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
