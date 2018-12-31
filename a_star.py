from collections import namedtuple
from maze import CellType, Coords, Maze

BaseCandidate = namedtuple('Candidate',
                           'coords parent dist_from_start dist_to_goal')


class Candidate(BaseCandidate):
    @property
    def score(self):
        return self.dist_from_start + self.dist_to_goal

    def reconstruct_path(self):
        if self.parent:
            return self.parent.reconstruct_path() + [self.coords]
        return [self.coords]

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score


def find_path(maze, start, goal):
    visited = set()
    discovered = [Candidate(start, None, 0, start.manhattan(goal))]
    while discovered:
        current = min(discovered)
        discovered.remove(current)

        if current.coords == goal:
            return current.reconstruct_path()

        visited.add(current.coords)

        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = filter(
           lambda n: maze.cell_at(n) == CellType.EMPTY and n not in visited,
           [current.coords + Coords(*delta) for delta in deltas]
        )

        for neighbor in neighbors:
            dist_from_start = (current.dist_from_start
                               + current.coords.manhattan(neighbor))
            dist_to_goal = goal.manhattan(neighbor)

            cand = Candidate(neighbor, current, dist_from_start, dist_to_goal)

            previously_discovered = None
            for c in discovered:
                if c.coords == neighbor:
                    previously_discovered = c
                    discovered.remove(previously_discovered)
                    break

            if previously_discovered:
                cand = min(cand, previously_discovered)
            discovered.append(cand)
    return None
