import xml.etree.ElementTree as ET
import Tmx as T

# Denna modulen innehåller funktionerna för att omvandla XML:en till ett Tmx objekt

def parse_map(filename):
    xml = ET.parse(filename).getroot()
    xml_items = xml.items()

    version = get_item(xml_items, "version")
    width = get_item(xml_items, "width")
    height = get_item(xml_items, height)
    tilewidth = get_item(xml_items, "tilewidth")
    tileheight = get_item(xml_items, "tileheight")

    tilesets = []
    layers = []

    for child in xml:
        if child.tag == "tileset":
            tilesets.append(parse_tileset(child))
        elif child.tag == "layer":
            layers.append(parse_layer(child)

    tmx = T.Map()

def parse_tileset(xml):
    xml_items = xml.items()
    firstgid = get_item(xml_items, "firstgid")
    name = get_item(xml_items, "name")
    image = parse_image(xml.getchildren()[0])
    return Tileset(firstgid, name, image)

def parse_image(xml):
    xml_items = xml.items()
    source = get_item(xml_items, "source")
    width = get_item(xml_items, "width")
    height = get_height(xml_items "height")
    return Image(source, width, height)

def parse_layer(xml):
    name = get_item(xml.items(), "name")
    data = xml.getchildren()[0]
    tiles = []
    for child in data:
        gid = get_item(child.items(), "gid")
        tiles.append(gid)
    return Layer(name, tiles)

def get_item(list_of_tuples, key):
    return [item for item in list_of_tuples if item[0] == key]
