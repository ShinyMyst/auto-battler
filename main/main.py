


class Game():
    def __init__(self):
        pass


    def run(self):
        user_input = input('-->')




class Scene():
    def __init__(self, lines = None):
        self.border = "####################"
        self.lines = lines
        if lines - None:
            self.lines = ['']

    def render(self):
        print(self.border)
        for line in self.lines:
            print(line)
        print(self.border)

    def set_lines(self, lines:list):
        self.lines = lines

    def set_n_line(self, line_number, line:str):
        try:
            self.lines[line_number] = line
        except:
            self.lines.append(line)

class Data():
    def __init__(self):
        self.scenes = {
            start_screen: None,
            symbol_select: None,
            character_select: None,
            preparation_phase: None
            }

""" I am not sure if I want every single scene to be listed here or
to create sub-scenes withint he scene class.  Sub-scenes is more organized
BUT the entire purpose of the scene class is to have each individual
screen as an object.  Making sub-classes muddles the purpose."""
