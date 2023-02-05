####################
# Commands
####################
"""Commands should edit data values."""
from data import Data


class Commands():
    def __init__(self, data:Data):
        self.data = data

    def swap_scene(self, target_scene:str):
         self.data.set_active_scene(target_scene)

