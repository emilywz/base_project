"""
   DataModel
"""


class DirectionModel:
    """
        Direction
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Location:
    def __init__(self, r, c):
        self.row_index = r
        self.column_index = c
