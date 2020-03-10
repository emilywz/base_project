from bll import GameCoreController
from model import DirectionModel

# 导入系统
import os


class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def main(self):
        self._start()
        self.__update()

    def _start(self):
        # 产生两个数字
        self.__controller.generate_random_number()
        self.__controller.generate_random_number()
        # 绘制界面
        self.__draw_list_map()

    def __update(self):
        # 循环
        while True:
            # 判断玩家的输入--->移动地图
            self.__move_list_map()

            # 产生新数字
            self.__controller.generate_random_number()

            # 绘制界面
            self.__draw_list_map()

            # 游戏结束判断-->提示
            if self.__controller.is_game_over():
                print("游戏结束")
                break

    def __draw_list_map(self):
        # 清空控制台
        os.system("clear")
        for line in self.__controller.list_map:  # 行
            for item in line:  # 列
                print(item, end=" ")
            print()

    def __move_list_map(self):
        dir = input("请输入方向（wsda）：")

        dict_dir = {
            "w": DirectionModel.UP,
            "s": DirectionModel.DOWN,
            "a": DirectionModel.LEFT,
            "d": DirectionModel.RIGHT
        }

        if dir in dict_dir:
            self.__controller.move(dict_dir[dir])

# -------------------------------------测试--------------------------
# if __name__=="__main__":
#     view=GameConsoleView()
#     view.main()
