from cocos.scene import Scene
from cocos.sprite import Sprite

import pyglet

class Background( Sprite ):
	
    def __init__(self):
        super(Background, self).__init__(pyglet.resource.image('Resources/Background.png'), (320, 240))

class DDScene(Scene):
    
    def __init__(self):
        super(DDScene, self).__init__()
        self.add(Background())