####################
# Data
####################
from scene import all_scenes

class Data():
    def __init__(self, display, active_scene):
	self.display = display
	self.active_scene = active_scene
        self.scenes = all_scenes
