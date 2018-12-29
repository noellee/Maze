from collections import namedtuple
from enum import Enum
import random


class CellType(Enum):
    EMPTY = ' '
    WALL = 'X'


class Coords(namedtuple('Coords', 'row col')):
    def __repr__(self):
        return f'({self.row}, {self.col})'

    def __add__(self, other):
        return Coords(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Coords(-self.row, -self.col)

    def __floordiv__(self, other):
        return Coords(self.row // other, self.col // other)

    def __div__(self, other):
        return Coords(self.row / other, self.col / other)

    def midpoint(self, other):
        return (self + other) // 2


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

    def in_bounds(self, coords):
        return 0 <= coords.row < self.size and 0 <= coords.col < self.size

    def set_cell(self, coords, value):
        self.grid[coords.row][coords.col] = value

    @classmethod
    def generate(cls, size=None, verbose=False):
        if size is None:
            maze = cls()
        else:
            maze = cls(size)

        start = Coords(1, 1)
        stack = [start]
        visited = {start}
        maze.set_cell(start, CellType.EMPTY)
        while stack:
            current = stack[-1]
            neighbors = [
                current + Coords(-2, 0),
                current + Coords(2, 0),
                current + Coords(0, -2),
                current + Coords(0, 2),
            ]
            neighbors = [n for n in neighbors
                         if maze.in_bounds(n) and n not in visited]

            if not neighbors:
                # backtrack
                stack.pop()
                continue

            next_cell = random.choice(neighbors)

            wall = current.midpoint(next_cell)
            maze.set_cell(wall, CellType.EMPTY)
            maze.set_cell(next_cell, CellType.EMPTY)

            visited.add(next_cell)
            stack.append(next_cell)

            if verbose:
                print(maze)
                print()

        return maze
