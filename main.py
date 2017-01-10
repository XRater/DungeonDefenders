
#import six

import sys, os
sys.path.append(os.path.join(sys.path[0], 'modules/menu'))
sys.path.append(os.path.join(sys.path[0], 'modules/service'))
sys.path.append(os.path.join(sys.path[0], 'modules/game'))
sys.path.append(os.path.join(sys.path[0], 'modules/game/view'))
sys.path.append(os.path.join(sys.path[0], 'modules/game/controler'))


from menu import *

from cocos.director import director
from cocos.layer import MultiplexLayer

from pyglet.window import BaseWindow

from service import DDScene
from options import Options
from images import Images        
          
def init_game_window():
    director.init(caption="Dungeon master", fullscreen = False,
                  autoscale = True, resizable = False)
    Options.get_config()
    director.window.set_size(Options.width, Options.height)
    director.window.set_fullscreen(fullscreen = Options.fullscreen)

    
if __name__ == "__main__":	
	
    init_game_window()
    main_scene = DDScene()
    menu_layer = MultiplexLayer(MainMenu(), OptionMenu(), ConnectionMenu())
    main_scene.add(menu_layer, z = 1)
    director.run(main_scene)    
    