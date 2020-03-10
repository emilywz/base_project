"""
    Logic:Game2048
"""
import random

from model import DirectionModel
from model import Location


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__list_map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []

    @property
    def list_map(self):
        return self.__list_map

    def __zero_to_end(self):
        """
           zero to end.
        """
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            merge same number
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __move_left(self):
        """
            move number to left
        """
        for line in self.__list_map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        """
            move number to right
        """
        for line in self.__list_map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge
　
    def __move_up(self):
        """
            move number up
        """
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()


    def __move_down(self):
        """
            move number down
        """
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
            matrix transpose
        """
        for c in range(1, len(self.__list_map)):
            for r in range(c, len(self.__list_map)):
                self.__list_map[r][c - 1], self.__list_map[c - 1][r] = self.__list_map[c - 1][r], self.__list_map[r][c - 1]

    def move(self, dir):
        """
            move direction
        :param dir: direction
        :return: 
        """
        if dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()
        elif dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()

    def generate_random_number(self):

        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        location = random.choice(self.__list_empty_location)
        self.__list_map[location.row_index][location.column_index] = self.__select_random_number()
        self.__list_empty_location.remove(location)

    def __select_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        """
        get left empty location
        """

        self.__list_empty_location.clear()

        for r in range(len(self.__list_map)):
            for c in range(len(self.__list_map[r])):
                if self.__list_map[r][c] == 0:
                    self.__list_empty_location.append((Location(r, c)))

    def is_game_over(self):

        if len(self.__list_empty_location) > 0:
            return False
        for r in range(len(self.__list_map)):
            for c in range(len(self.__list_map[r]) - 1):
                if self.__list_map[r][c] == self.__list_map[r][c + 1] or self.__list_map[c][r] == self.__list_map[c + 1][r]:
                    return False
        else:
            return True


# ---------------------------test--------------------
if __name__ == "__main__":
    controller = GameCoreController()
    # controller.move("w")
    controller.generate_random_number()
    controller.generate_random_number()

    print(controller.list_map)
    print(controller.is_game_over())
