from enum import Enum


class CellType(Enum):
    EMPTY = ' '
    WALL = 'X'


class Maze:
    def __init__(self, size=15):
        if size % 2 == 0:
            raise ValueError('Size must be an odd number')

        if size < 0:
            raise ValueError('Size cannot be negative')

        self.grid = [[CellType.WALL] * size for _ in range(size)]
        self.size = size

    def __repr__(self):
        rows = [' '.join(cell.value for cell in row) for row in self.grid]
        return '\n'.join(rows)

    @classmethod
    def generate(cls, size=None, verbose=False):
        if size is None:
            maze = cls()
        else:
            maze = cls(size)

        # TODO

        return maze
