from display import Display
from data import Data
from commands import Commands
from scene import Scenes

class Game():
    def __init__(self):
        self.display = Display()
        self.data = Data(self.display)
        self.commands = Commands(self.data)
        self.scenes = Scenes(self.commands)


    def run(self):
        self.display.render()
        user_input = input('-->')


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

# TODO
# Consider seperating files that import each other in same area
# For example, data uses scene, so they should be in folder


