from display import Display
from data import Data


class Game():
    def __init__(self):
        self.display = Display()
        self.data = Data(self.display)


    def run(self):
        self.display.render()

        while True:
            user_input = input('-->')

            if user_input == 'q':
                print("Are you sure you want to quit?")
                user_input = input('-->')
                if user_input == 'y':
                    quit()
                


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

# TODO
# Consider seperating files that import each other in same area
# For example, data uses scene, so they should be in folder
# Fix the quit commands.  Integrate into command files

