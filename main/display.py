####################
# Display
####################
class Display():
    """Stores images and commands for a particular screen."""
    def __init__(self):
        self.ascii = ['']
        

    def set_scene(self, scene):
        """Replaces list of current ascii objects when a new set."""
        self.ascii = self.scene.get_ascii()


    def render(self):
        """Refreshes terminal & displays all ascii objects in current scene"""
        for img in self.ascii:
            print(img)
        
