from cocos.director import director
from cocos.layer import Layer

from options import Connection

class Controler(Layer):
    
    is_event_handler = True
    
    def __init__(self, model):
        super(Controler, self).__init__()
        self.model = model
    
    def on_quit(self):
        Connection.close_connection()
        director.pop()