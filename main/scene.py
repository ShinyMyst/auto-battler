class Scene():
    """Stores images and commands for a particular screen."""
    def __init__(self, ascii_list = None):
        self.ascii_objects = []
        if ascii_list:
            self.ascii_object = ascii_list

    def add_ascii(self, ascii_object):
        """Add a new object to end of the list."""
        ascii_objects.append(ascii_object)

    def get_ascii(self):
	return ascii_objects



        

###############
# Title Scene
###############
# Create Visuals
f = open('ascii_exhume')
ascii_exhume = f.read()
f = open('ascii_skull')
ascii_skull = f.read()
ascii_text = 'Rise of the Necromancer'
# Configure Scene
ascii_list = [ascii_exhume, ascii_skull, ascii_text]
title_scene = Scene(ascii_list)





###############
# All Scenes
###############
all_scenes = {
    "title_scene": title_scene
}
