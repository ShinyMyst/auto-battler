from display import Display
from data import Data

class Game():
    def __init__(self):
        self.active_scene = None
        self.display = Display()
        self.data = Data(self.display, self.active_scene)


    def run(self):
        self.display.render()
        user_input = input('-->')




