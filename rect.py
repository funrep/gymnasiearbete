# coding=utf-8

# I denna modulen har vi en klass för en rektangel, detta gör det enklare att implementera collision detection

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.top = y
        self.bottom = y + height 
        self.left = x
        self.right = x + width

    def upd_x(self, x):
        self.x = x
        self.left = x
        self.right = x + self.width

    def upd_y(self, y):
        self.y = y
        self.top = y
        self.bottom = y + self.height

    def intersect(self, rect):
        intersectX = not((self.left > rect.right) or (rect.left > self.right))
        intersectY = not((self.top > rect.bottom) or (rect.top > self.bottom))
        return intersectX and intersectY 
