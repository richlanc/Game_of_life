'''
Created on 3 Nov 2013

@author: richard
'''

# Imports
import os
import sys
import time
from argparse import ArgumentParser, RawTextHelpFormatter
from game_of_life.engine.game_of_life import GameOfLife
from game_of_life.engine.rule_sets import RuleSetStandard
from game_of_life.data_structures.grid import Grid
from game_of_life.data_structures.cell import Cell
from game_of_life.data_structures.state import Alive

DEAD_CHAR = '-'
ALIVE_CHAR = '*'
pattern_guide = """
    Guide for inputing Game of Life pattern:
        - The width of the grid is based upon the first line you enter
        - '-' denotes an dead cell
        - '+' denotes an alive cell
        - An empty lines marks the end of the grid and the pattern complete
        - Any character that isn't '+' will be considered dead
"""


def _get_grid():
    grid_s = ""
    print("Please enter your pattern:")
    print(pattern_guide)
    while True:
        line = sys.stdin.readline()
        if not line or line == "\n":
            break
        grid_s += line
    return grid_s


def _parse_grid_string(grid_string):
    rows = []
    row_len = grid_string.find('\n')
    for row in grid_string.split('\n')[:-1]:
        cols = []
        for col in row:
            if col == ALIVE_CHAR:
                cols.append(Cell(Alive()))
            else:
                cols.append(Cell())
        for _ in range(0, row_len):
            cols.append(Cell())
        cols = cols[:row_len]
        rows.append(cols)
    return Grid(rows)


def _print_grid(grid):
    os.system('clear')

    for row in grid.get_cells():
        line = ""
        for col in row:
            if col.get_state() == Alive():
                line += ALIVE_CHAR
            else:
                line += DEAD_CHAR
        print(line)


def main(automated, turn_limit, grid_string):
    grid = _parse_grid_string(grid_string)
    gol = GameOfLife(RuleSetStandard(), grid)

    turns = 0
    running = True
    while running:

        _print_grid(gol.get_current_generation())
        print('Turn:  %s' % turns)

        if not automated:
            r = input('Press enter for next turn, "exit" to exit: ')
            running = not r.lower()[1:] == "e"

        gol.next_turn()

        if turn_limit and turn_limit >= turns:
            running = False

        if automated:
            time.sleep(0.5)
        turns += 1

if __name__ == '__main__':
    # Variables needed:
    #    - Users's pattern
    #        - Read lines, "-" for dead, "*" for alive
    #        - This could be read from a file
    #        - Empty line means end
    #    - Automated ?
    #        Limited number of turns?
    #    - Else user controlled turns

    # Set up parser
    des = '''Command line output for the CO600 Game of life object''' + pattern_guide
    parser = ArgumentParser(description=des,
                                     formatter_class=RawTextHelpFormatter)

    # Add argument options
    parser.add_argument('-a', '--automated', type=bool, default=False,
                        help='Run the game of life without pausing for input')
    parser.add_argument('-t', '--turn_limit', type=int,
                        help='Run the game of life without pausing for input')
    parser.add_argument('-f', '--file', type=str,
                        help='Specify a file containing a grid')
    args = parser.parse_args()

    # Set up args for main
    if not args.automated and args.turn_limit:
        print("Turn limit can only be used with automated enabled")
        sys.exit(1)
    if args.file:
        with open(args.file, "r") as file:
            grid_s = file.read()
    else:
        grid_s = _get_grid()

    main(args.automated, args.turn_limit, grid_s)
