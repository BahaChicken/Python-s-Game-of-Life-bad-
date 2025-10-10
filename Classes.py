class VerticalLine():
    def __init__(self, w, h, x, y, color, id, surf, rect):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.color = color
        self.id = id
        self.surf = surf
        self.rect = rect
class HorizontalLine():
    def __init__(self, w, h, x, y, color, id, surf, rect):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.color = color
        self.id = id
        self.surf = surf
        self.rect = rect
class Cell():
    def __init__(self, x, y, gridx, gridy,  color, surf, rect, adjacent, near, state, willLive):
        self.x = x
        self.y = y
        self.gridx = gridx
        self.gridy = gridy
        self.color = color
        self.surf = surf
        self.rect = rect
        self.adjacent = adjacent
        self.near = near
        self.isAlive = state
        self.willLive = willLive
class Game:
    def __init__(self, auto = False, step = False, FFD = False):
        self.auto = bool(auto)
        self.step = bool(step)
        self.FFD = bool(FFD)
