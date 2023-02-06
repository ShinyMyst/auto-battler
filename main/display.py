####################
# Display
####################
class Display():
    """Stores images and commands for a particular screen."""
    def __init__(self):
        self.ascii = ['']
        self.scene = None
        

    def set_scene(self, scene):
        """Replaces list of current ascii objects when a new set."""
        self.ascii = scene.get_ascii()


    def render(self):
        """Refreshes terminal & displays all ascii objects in current scene"""
        print("RENDER")
        for img in self.ascii:
            print(img)
    
    
# TODO
# Scene should hold the class object
# Render pulls the visuals from that object
# Scene can change so need to pull it from there directly