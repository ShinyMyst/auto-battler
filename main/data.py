####################
# Data
####################
from scene import all_scenes
from commands import Commands

class Data():
    def __init__(self, display):
        print("INIT Data")
        self.display = display
        self.all_scenes = all_scenes
        self.commands = Commands(self)
        
        # Load First Scene
        print("CALLIT")
        self.commands.set_active_scene("title_scene")

        
    def set_active_scene(self, scene_name:str):
        """Changes the scene currently being displayed."""
        scene = self.all_scenes[scene_name]
        self.display.set_scene(scene)
        self.active_scene = scene
        
    def process_input(input_str):
        """Check if current input is an existing scene command.
        Execute if yes.  Return invalid command if not."""
        pass
    
# TODO:
# Process input checks commands in command dict.