from pyglet.window import key

from controler import Controler

class PControler(Controler):
                
    def __init__(self, model):
        super(PControler, self).__init__(model)
        
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.on_quit()
            return True
        if symbol == key.P:
            print('client')
            return True
         