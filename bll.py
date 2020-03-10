"""
    逻辑控制：2048　游戏核心算法
"""
import random

from model import DirectionModel
from model import Location


class GameCoreController:
    def __init__(self):
        # 实例方法
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
            零元素移动到末尾.
        """
        # 思想：从后向前，如果发现零元素，删除并追加.
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并
        """
        # 先将中间的零元素移到末尾
        # 再合并相邻相同元素
        # 调用：使用实例.方法
        self.__zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                # 将后一个累加前一个之上
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __move_left(self):
        """
            向左移动
        """
        # 思想:将二维列表中每行交给merge函数进行操作
        for line in self.__list_map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        """
            向右移动
        #     由需求想到的思想，由思想体现的代码
        """
        # 思想:将二维列表中每行(从右向左)交给merge函数进行操作
        for line in self.__list_map:
            # 从右向左取出数据　形成　新列表,把右边给到左边
            self.__list_merge = line[::-1]
            self.__merge()
            # 从右向左接受　合并后的数据　
            line[::-1] = self.__list_merge

    # 向上移动　　
    def __move_up(self):
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    # 向下移动
    def __move_down(self):
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    # 提示:利用方阵转置函数
    # 优先私有
    def __square_matrix_transpose(self):
        """
            方阵转置
         二维列表类型的方阵
        """
        for c in range(1, len(self.__list_map)):
            for r in range(c, len(self.__list_map)):
                self.__list_map[r][c - 1], self.__list_map[c - 1][r] = self.__list_map[c - 1][r], self.__list_map[r][
                    c - 1]

    def move(self, dir):
        """
            移动方向
        :param dir: 移动方向
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

    # 实现的功能
    # def generate_random_number(self):
    #     # 确定哪个空白位置1 0
    #     # 思路：选出所有的空白位置，在随机调谑一个
    #     self.__list_empty_location.clear()
    #     for r in range(len(self.__list_map)):#0 1 2 3
    #         for c in range(len(self.__list_map[r])):
    #             if self.__list_map[r][c]==0:
    #                 # 记录行 列 r c
    #                 self.__list_empty_location.append((r,c))
    #
    #     location=random.choice(self.__list_empty_location)
    #     # location 是随机的元组
    #     if random.randint(1, 10) == 1:
    #         self.__list_map[location[0]][location[1]]=4
    #     else:
    #         self.__list_map[location[0]][location[1]]=2

    def generate_random_number(self):
        """
        产生随机新数字
        """
        self.__get_empty_location()
        # 判断是否有空位置
        if len(self.__list_empty_location) == 0:
            return
        location = random.choice(self.__list_empty_location)
        # if random.randint(1, 11) == 1:
        #     self.__list_map[location.row_index][location.column_index] = 4
        # else:
        #     self.__list_map[location.row_index][location.column_index] = 2
        self.__list_map[location.row_index][location.column_index] = self.__select_random_number()
        self.__list_empty_location.remove(location)

    def __select_random_number(self):
        """
        选择随机数
        :return: 
        """
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        """
        获取空白位置
        """
        # 每次统计空位置，都先清空之前的数据，避免影响本次数据
        self.__list_empty_location.clear()

        for r in range(len(self.__list_map)):
            for c in range(len(self.__list_map[r])):
                if self.__list_map[r][c] == 0:
                    # 记录行 列 r c
                    self.__list_empty_location.append((Location(r, c)))

    def is_game_over(self):
        """
        游戏是否结束
        :return: False表示游戏没有结束,True表示游戏结束
        """
        # 是否具有空位置
        if len(self.__list_empty_location) > 0:
            return False

        # 判断横向有没有相同的位置
        for r in range(len(self.__list_map)):
            for c in range(len(self.__list_map[r]) - 1):
                if self.__list_map[r][c] == self.__list_map[r][c + 1] or self.__list_map[c][r] == \
                        self.__list_map[c + 1][r]:
                    return False

        # # 判断竖向有没有相同的位置
        # for c in range(len(self.__list_map)):
        #     for r in range(len(self.__list_map[c])-1):
        #         if self.__list_map[r][c]==self.__list_map[r+1][c]:
        #             return False

        return True


# ---------------------------测试代码--------------------
if __name__ == "__main__":
    controller = GameCoreController()
    # controller.move("w")
    controller.generate_random_number()
    controller.generate_random_number()

    print(controller.list_map)
    print(controller.is_game_over())
