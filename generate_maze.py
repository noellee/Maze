import argparse
from maze import Maze

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a random maze')
    parser.add_argument('size', type=int, nargs='?',
                        help='Size of the generated maze')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()
    print(args)
    if args.size is None:
        maze = Maze.generate(verbose=args.verbose)
    else:
        maze = Maze.generate(args.size, verbose=args.verbose)
    print(f'Size: {args.size}')
    print(maze)
