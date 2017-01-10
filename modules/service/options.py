import pyglet
#from pyglet import event
import socket

class OptionsClass:
    
    def __init__(self):
        self.width = 800
        self.height = 600
        self.fullscreen = 0
    
    def get_config(self):
        config = open("config.txt", 'r')
        self.width = int(config.readline().split()[2])
        self.height = int(config.readline().split()[2])
        self.fullscreen = int(config.readline().split()[2])
        config.close()
        
    def safe_config(self):
        config = open("config.txt", 'w')
        config.write("SCREEN_WIDTH = " + str(self.width) + "\n")
        config.write("SCREEN_HEIGHT = " + str(self.height) + "\n")
        config.write("FULLSCREEN = " + str(self.fullscreen) + "\n")
        config.close()
        
class ConnectionClass(pyglet.event.EventDispatcher):
    
    def init_server(self):
        self.sock = socket.socket()
        try:
            self.sock.bind(('0.0.0.0', 9050))
            self.sock.listen(1)
            self.conn, addr = self.sock.accept()
        except socket.error:
            self.dispatch_event('on_connection_failed')
        else:
            print('connected:', addr)
            self.dispatch_event('on_connection_set', 'server')
    
    def connect_to_server(self):
        self.sock = socket.socket()
        try:
            self.sock.connect(('localhost', 9050))
        except socket.error:
            self.dispatch_event('on_connection_failed')
        else:
            self.dispatch_event('on_connection_set', 'client')
            
    def close_connection(self):
        self.sock.close()

ConnectionClass.register_event_type('on_connection_set')        
ConnectionClass.register_event_type('on_connection_failed')

Connection = ConnectionClass()
Options = OptionsClass()