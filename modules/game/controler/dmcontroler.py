from pyglet.window import key

from controler import Controler
            
class DMControler(Controler):
                
    def __init__(self, model):
        super(DMControler, self).__init__(model)
        
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.on_quit()
            return True
        if symbol == key.P:
            print('server')
            return True