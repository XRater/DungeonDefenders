from service import DDScene
from dmcontroler import DMControler
from pcontroler import PControler
from dmview import DMGameView
from pview import PGameView
from model import GameModel

class MainScene(DDScene):
    
    def __init__(self, side):
        super(MainScene, self).__init__()
        self.model = GameModel()
        if side == 'server':
            self.add(DMGameView())
            self.cntr = DMControler(self.model)
        if side == 'client':
            self.add(PGameView())
            self.cntr = PControler(self.model)        
        
def get_new_game(side):
    return MainScene(side)