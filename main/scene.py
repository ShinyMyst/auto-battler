####################
# Scene
####################

# We currently have an import loop going on.
# Commands needs data.  Data needs scenes.  Scenes needs commands.
# This triangle needs fixed.

from commands import Commands

class Scenes():
    def __init__(self, commands: Commands):
        self.commands = commands
        self.all_scenes = None

class Scene():
    """Stores images and commands for a particular screen."""
    def __init__(self, ascii_list, command_dict):
        self.commands = command_dict
        self.ascii_objects = ascii_list

    def get_ascii(self):
        """Returns a list of all ascii objects in the class"""
        return self.ascii_objects
 
    def get_command(self, key_press):
        """Run command associated with the key press."""
        self.commands['key_press']

 
class TitleScene(Scenes):
    def __init__(self, assets):
        self.scene_elements = []
        self._load_assets(assets)
        

    def _load_assets(self, assets):
        for object in self.assets:
            action = object[0]
            content = object[1]
            if action == 'load':
                content = self._load_file(content)
            # If action == 'text', no steps required

            self.scene_elements.append(content)
            
    def _load_file(self, path:str):
        """Load and return the information from file at given path"""
        f = open(path)
        content = f.read()
        return content
      
title_visuals = [
    ('load', 'Desktop/git-projects/auto-battler/main/ascii_exhume.txt')
    ('load', 'Desktop/git-projects/auto-battler/main/ascii_skull.txt')
    ('text', 'Rise of the Necromancer')
]

#### Title Scene #####
# Create Visuals
f = open('Desktop/git-projects/auto-battler/main/ascii_exhume.txt')
ascii_exhume = f.read()
f = open('Desktop/git-projects/auto-battler/main/ascii_skull.txt')
ascii_skull = f.read()
ascii_text = 'Rise of the Necromancer'
# Commands
command_dict = {
    '': None
    
    
}


# Configure Scene
ascii_list = [ascii_exhume, ascii_skull, ascii_text]
title_scene = Scene(ascii_list, command_dict)


#### Briefing Info #####
briefing_line_1 = 'Welcome traveler.'
briefing_line_2 = 'Lord Nero of Undeath has promised to share with you the secrets of Lichdom.'
briefing_line_3 = 'But theres a catch.  You are now that only one.'
briefing_line_4 = 'You must brave his dungeons and be the last man standing to achieve immortality.'
briefing_line_5 = 'Do you have what it takes?'
briefing_line_6 = "Press 'y' or 'n'"
ascii_list = [briefing_line_1, briefing_line_2, briefing_line_3, briefing_line_4, briefing_line_5, briefing_line_6]
briefing_scene = Scene(ascii_list, None)


###############
# All Scenes
###############
all_scenes = {
    "title_scene": title_scene,
    "briefing_scene": briefing_scene
}

# TODO
# Make a subclass object for each scene instead?