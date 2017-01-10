from cocos.layer import Layer, ColorLayer
from cocos.sprite import Sprite
        
from view import GameView
        
class DMGameView(GameView):
    
    def __init__(self):
        super(DMGameView, self).__init__()
        self.add(ColorLayer(0, 255, 0, 100))    