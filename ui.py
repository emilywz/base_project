from bll import GameCoreController
from model import DirectionModel

import os


class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def main(self):
        self._start()
        self.__update()

    def _start(self):
        self.__controller.generate_random_number()
        self.__controller.generate_random_number()
        self.__draw_list_map()

    def __update(self):
        while True:
            self.__move_list_map()

            self.__controller.generate_random_number()

            self.__draw_list_map()

            if self.__controller.is_game_over():
                print("GameOver")
                break

    def __draw_list_map(self):
        os.system("clear")
        for line in self.__controller.list_map:  
            for item in line:
                print(item, end=" ")
            print()

    def __move_list_map(self):
        dir = input("Plear input your direction（wsda）：")

        dict_dir = {
            "w": DirectionModel.UP,
            "s": DirectionModel.DOWN,
            "a": DirectionModel.LEFT,
            "d": DirectionModel.RIGHT
        }

        if dir in dict_dir:
            self.__controller.move(dict_dir[dir])

# -------------------------------------test--------------------------
# if __name__=="__main__":
#     view=GameConsoleView()
#     view.main()
