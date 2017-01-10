from cocos.director import director
from cocos.menu import *
from cocos.layer import Layer

import pyglet
from pyglet.window import key

import threading
import socket

from service import DDScene
from options import Options, Connection
from loading_screen import WaitingLayer

sc = [(640, 480), (800, 600), (1024, 768), (1280, 1024)]

class DDMenu(Menu):
    
    def __init__(self, title='DD'):
        super(DDMenu, self).__init__(title) 
        
        self.font_title['font_name'] = 'Edit Undo Line BRK'
        self.font_title['font_size'] = 36
        self.font_title['color'] = (245,184,16,255)

        self.font_item['font_name'] = 'Courier New',
        self.font_item['color'] = (32,16,32,255)
        self.font_item['font_size'] = 20
        self.font_item_selected['font_name'] = 'Courier New'
        self.font_item_selected['color'] = (178, 34, 34,255)
        self.font_item_selected['font_size'] = 27

        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER
            
    
class ConnectionMenu(DDMenu):

    def __init__(self):
        super(ConnectionMenu, self).__init__('Dungeon Master') 
    
        items = []
        
        items.append(MenuItem('Server', self.on_server))
        items.append(MenuItem('Client', self.on_client))
        items.append(MenuItem('Quit', self.on_quit))
        
        self.create_menu(items, shake(), shake_back())
        
    def on_server(self):
        self.conn_thread = threading.Thread(target = Connection.init_server, daemon = True)
        self.conn_thread.start()
        director.push( DDScene().add(WaitingLayer()) )
                    
    def on_client(self):
        self.conn_thread = threading.Thread(target = Connection.connect_to_server, daemon = True)
        self.conn_thread.start()
        director.push( DDScene().add(WaitingLayer()) )
    
    def on_quit(self):
        self.parent.switch_to(0)

                
class OptionMenu(DDMenu):
        
    def __init__(self):
        super(OptionMenu, self).__init__('Options')

        items = []

        items.append(MultipleMenuItem('Screen: ', 
                                      self.on_resolution, 
                                      ['640x480', '800x600', '1024x768', '1280x1024'], 
                                      sc.index((Options.width, Options.height))))
        items.append(ToggleMenuItem('Fullscreen: ', self.on_fullscreen, director.window.fullscreen))
        items.append(MenuItem('Quit', self.on_quit))

        self.create_menu(items, shake(), shake_back())
       
    def on_resolution(self, item):
        if director.window.fullscreen == False:
            w, h = sc[item]
            director.window.set_size(w, h)
            Options.width, Options.height = w, h

    def on_fullscreen(self, item):
        director.window.set_fullscreen(fullscreen = item)
        Options.fullscreen = item
        
    def on_quit(self):
        Options.safe_config()
        self.parent.switch_to(0)
               

class MainMenu(DDMenu):

    def __init__(self):
        super(MainMenu, self).__init__('Dungeon Master') 
    
        items = []
        
        items.append(MenuItem('New Game', self.on_newgame))
        items.append(MenuItem('Options', self.on_options))
        items.append(MenuItem('Quit', self.on_quit))
        
        self.create_menu(items, shake(), shake_back())

    def on_newgame(self):
        #print(threading.active_count())
        self.parent.switch_to(2)

    def on_options(self):
        self.parent.switch_to(1)
    
    def on_quit(self):
        pyglet.app.exit()
