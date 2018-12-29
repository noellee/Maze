from enum import Enum
import random


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

    def in_bounds(self, coords):
        row, col = coords
        return 0 <= row < self.size and 0 <= col < self.size

    def set_cell(self, coords, value):
        row, col = coords
        self.grid[row][col] = value

    @classmethod
    def generate(cls, size=None, verbose=False):
        if size is None:
            maze = cls()
        else:
            maze = cls(size)

        start = (1, 1)
        stack = [start]
        visited = {start}
        maze.set_cell(start, CellType.EMPTY)
        while stack:
            current = stack[-1]
            curr_row, curr_col = current
            neighbors = [
                (curr_row - 2, curr_col),
                (curr_row + 2, curr_col),
                (curr_row, curr_col - 2),
                (curr_row, curr_col + 2),
            ]
            neighbors = [n for n in neighbors
                         if maze.in_bounds(n) and n not in visited]

            if not neighbors:
                # backtrack
                stack.pop()
                continue

            next_cell = random.choice(neighbors)
            next_row, next_col = next_cell

            wall = ((curr_row + next_row) // 2, (curr_col + next_col) // 2)
            maze.set_cell(wall, CellType.EMPTY)
            maze.set_cell(next_cell, CellType.EMPTY)

            visited.add(next_cell)
            stack.append(next_cell)

            if verbose:
                print(maze)
                print()

        return maze
