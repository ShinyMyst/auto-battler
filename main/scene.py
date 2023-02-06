####################
# Scene
####################

# We currently have an import loop going on.
# Commands needs data.  Data needs scenes.  Scenes needs commands.
# This triangle needs fixed.


class Scene():
    """Stores images and commands for a particular screen."""
    def __init__(self, assets):
        self.scene_elements = [] 
        self._save_assets(assets)
       

    def get_elements(self):
        """Returns a list of all ascii objects in the class"""
        return self.scene_elements
    
    def _save_assets(self, assets):
        """Save list of assets to the class.  Asset list has specific format."""
        print("SAVE")
        for object in assets:
            action = object[0]
            payload = object[1]
            if action == 'load':
                content = self._load_file(payload)
                self.scene_elements.append(content)
            elif action == 'text':
                self.scene_elements.append(payload)
            
    def _load_file(self, path:str):
        """Load and return the information from file at given path"""
        f = open(path)
        content = f.read()
        return content

      
title_visuals = [
    ('load', 'Desktop/git-projects/auto-battler/main/ascii_exhume.txt'),
    ('load', 'Desktop/git-projects/auto-battler/main/ascii_skull.txt'),
    ('text', 'Rise of the Necromancer')
]


title_scene = Scene(title_visuals)


#### Briefing Info #####
briefing_line_1 = 'Welcome traveler.'
briefing_line_2 = 'Lord Nero of Undeath has promised to share with you the secrets of Lichdom.'
briefing_line_3 = 'But theres a catch.  You are now that only one.'
briefing_line_4 = 'You must brave his dungeons and be the last man standing to achieve immortality.'
briefing_line_5 = 'Do you have what it takes?'
briefing_line_6 = "Press 'y' or 'n'"
ascii_list = [briefing_line_1, briefing_line_2, briefing_line_3, briefing_line_4, briefing_line_5, briefing_line_6]



###############
# All Scenes
###############
all_scenes = {
    "title_scene": title_scene,
    "briefing_scene": None
}

# TODO
# Make a subclass object for each scene instead?