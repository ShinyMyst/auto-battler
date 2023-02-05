####################
# Data
####################
from scene import all_scenes

class Data():
    def __init__(self, display):
        self.display = display
        self.all_scenes = all_scenes
        self.active_scene = None
        self.set_active_scene("title_scene")
        
    def set_active_scene(self, scene_name:str):
        """Changes the scene currently being displayed."""
        scene = self.all_scenes[scene_name]
        print("Setting display")
        self.display.set_scene(scene)
        self.active_scene = scene
        
    def process_input(input_str):
        """Check if current input is an existing scene command.
        Execute if yes.  Return invalid command if not."""
        pass