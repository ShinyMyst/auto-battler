####################
# Commands
####################
"""Commands should edit data values."""


class Commands():
    def __init__(self, data):
        # Create reference to data variables
        self.data = data
        self.display = data.display
        self.all_scenes = data.all_scenes
        
        
    def set_active_scene(self, scene_name:str):
        scene = self.all_scenes[scene_name]
        self.display.set_scene(scene)
        


# Changing scene should somehow change what commands are mapped to on this page