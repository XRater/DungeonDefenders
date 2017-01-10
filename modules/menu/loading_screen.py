from cocos.director import director
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions import *

from pyglet.window import key

from images import Images
from options import Options, Connection

class Loading_circle(Sprite):
    
    def __init__(self):
        super(Loading_circle, self).__init__(Images.loading_circle, (320, 240))
        act = Repeat(RotateBy(360/12, 0) + Delay(0.1))
        self.do(act)
        
class WaitingLayer(Layer):
    
    is_event_handler = True
    
    def __init__(self):
        super(WaitingLayer, self).__init__()
        self.killed = False
        self.add(Loading_circle())
        Connection.set_handlers(self.on_connection_set, self.on_connection_failed)
    
    def on_connection_set(self, side):
        from initgame import get_new_game
        director.replace(get_new_game(side))
    
    def on_connection_failed(self):
        if not(self.killed):
            self.on_quit()
 
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.on_quit()
            return True
     
    def on_quit(self):
        self.killed = True
        Connection.close_connection()
        self.parent.end()
        