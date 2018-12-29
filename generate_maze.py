import argparse
from maze import Maze

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a random maze')
    parser.add_argument('width', type=int, nargs='?',
                        help='Width of the generated maze')
    parser.add_argument('height', type=int, nargs='?',
                        help='Height of the generated maze')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()
    width, height = args.width, args.height
    if width is None:
        maze = Maze.generate(verbose=args.verbose)
    else:
        maze = Maze.generate(width, height, verbose=args.verbose)
    print(f'Dimensions: {maze.width}x{maze.height}')
    print(maze)
