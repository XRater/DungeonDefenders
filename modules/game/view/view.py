from cocos.layer import Layer, ColorLayer
        
class GameView(Layer):
    
    def __init__(self):
        super(GameView, self).__init__()
        self.add(ColorLayer(255, 0, 0, 100))        
        