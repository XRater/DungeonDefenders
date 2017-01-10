from cocos.layer import Layer, ColorLayer
from cocos.sprite import Sprite
        
from view import GameView
        
class PGameView(GameView):
    
    def __init__(self):
        super(PGameView, self).__init__()
        self.add(ColorLayer(0, 0, 255, 100))    