import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

def parse_inpt(inpt):
    pts = []
    folds = []
    for line in inpt:
        if ',' in line:
            pts.append(tuple(utils.ints(line)))
        elif '=' in line:
            folds.append(line.split()[-1])
    return pts, folds


def place_dots(rows, cols, points):
    grid = utils.grid(cols, rows, default=False)
    for c, r in points:
        grid[r][c] = True
    return grid

def fold(grid, instruction):
    axis, n = instruction.split('=')
    n = int(n)
    new_grid = utils.grid(len(grid[0]), len(grid), default=False)
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if axis == 'x':
                # same row, diff column
                new_grid[r][c if c < n else n - (c-n)] |= grid[r][c]
            else:
                new_grid[r if r < n else n - (r - n)][c] |= grid[r][c]
    return new_grid

def count_dots(grid):
    return utils.flatten(grid).count(True)

def print_grid(grid):
    for row in grid:
        if any(row):
            print(''.join(['#' if x else ' ' for x in row]))

def do_part_1(inpt):
    pts, folds = parse_inpt(inpt)
    rows = max([y for _, y in pts]) + 1
    cols = max([x for x, _ in pts]) + 1
    grid = place_dots(rows, cols, pts)
    grid = fold(grid, folds[0])
    return count_dots(grid)


def do_part_2(inpt):
    pts, folds = parse_inpt(inpt)
    rows = max([y for _, y in pts]) + 1
    cols = max([x for x, _ in pts]) + 1
    grid = place_dots(rows, cols, pts)
    for f in folds:
        grid = fold(grid, f)
    print_grid(grid)

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
