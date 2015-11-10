# coding=utf-8
# Python klass som representerar en banfil
# vi ignorerar några fält som finns i TMX-specifikationen
# för de används inte i spelet

class Map:
    def __init__(self, version,  width, height, tilewidth, tileheight,
            tilesets, layers):
        self.version = version
        self.width = width
        self.height = height
        self.tilewidth = tilewidth
        self.tileheight = tileheight
        self.tilesets = tilesets
        self.layers = layers

class Tileset:
    def __init__(self, firstgid, name, image):
        self.firstgid = firstgid
        self.name = name
        self.image = image

class Image:
    def __init__(self, source, width, height):
        self.source = source
        self.width = width
        self.height = height

class Layer:
    def __init__(self, name, tiles):
        self.name = name
        self.tiles = tiles
