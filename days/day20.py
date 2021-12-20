import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

def parse_grid(inpt, buffer=4):
    grid = []
    for line in inpt:
        grid.append(([0] * buffer) + [1 if x == '#' else 0 for x in line] + ([0] * buffer))
    line_length = len(grid[0])
    for _ in range(buffer):
        grid.insert(0, [0] * line_length)
        grid.append([0] * line_length)
    return grid

def get_neighbor_value(r, c, grid, default=0):
    bits = []
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if i < 0 or j < 0:
                bits.append(default)
                continue
            try:
                bits.append(grid[i][j])
            except IndexError:
                bits.append(default)
    return int(''.join([str(x) for x in bits]), 2)

def get_output_pixel(r, c, grid, algorithm):
    val = get_neighbor_value(r, c, grid, default=grid[0][0])
    return algorithm[val]

def get_next_grid(grid, algorithm, default):
    print(f"getting grid with default {default}")
    buffer = 1
    rows = len(grid)
    cols = len(grid[0])
    new_grid = utils.grid(rows + (buffer * 2), cols + (buffer * 2), default=default)
    for i in range(0, rows + (buffer * 2)):
        for j in range(0, cols + (buffer * 2)):
            new_grid[i][j] = get_output_pixel(i-buffer, j-buffer, grid, algorithm)
    return new_grid

def count_pixels(grid):
    return sum([sum(row) for row in grid])

def do_part_1(inpt):
    algorithm = [1 if x == '#' else 0 for x in inpt[0]]
    assert len(algorithm) == 512
    grid = parse_grid(inpt[2:], buffer=3)
    default = 0
    for _ in range(2):
        default = algorithm[0 if default == 0 else -1]
        grid = get_next_grid(grid, algorithm, default=default)
    
    return count_pixels(grid)

def do_part_2(inpt):
    algorithm = [1 if x == '#' else 0 for x in inpt[0]]
    assert len(algorithm) == 512
    grid = parse_grid(inpt[2:], buffer=3)
    default = 0
    for _ in range(50):
        default = algorithm[0 if default == 0 else -1]
        grid = get_next_grid(grid, algorithm, default=default)
    
    return count_pixels(grid)

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
