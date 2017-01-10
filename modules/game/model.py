
import pyglet

from const import *

class GameModel( pyglet.event.EventDispatcher):
    
    def __init__(self):
        super(GameModel, self).__init__()
        self.board = Board()

class Board():    
    
    def __init__(self):
        self.map = {}
        for i in range (BOARD_WIDTH):
            for j in range (BOARD_HEIGHT):
                self.map[(i, j)] = Tile(i, j)
    
    def __setitem__(self, key, value):
        self.map[key] = value
    
    def __getitem__(self, key):
        return self.map.get(key, None)

        
class Tile():
    
    def __init__(self, x, y):
        self.name = 'initial'
        self.x = x
        self.y = y
       