import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

def parse(inpt):
    grid = []
    for line in inpt:
        grid.append([int(x) for x in list(line)])
    return grid

def increment_all(grid):
    for r in range(10):
        for c in range(10):
            grid[r][c] += 1

def increment_neighbors(grid, r, c):
    neighbors = utils.get_neighbor_coordinates((r, c), (10, 10), incl_diagonals=True)
    for nr, nc in neighbors:
        grid[nr][nc] += 1

def flash(grid, flashed_this_turn):
    stable = True
    for r in range(10):
        for c in range(10):
            if grid[r][c] > 9:
                if not flashed_this_turn[r][c]:
                    stable = False
                    increment_neighbors(grid, r, c)
                flashed_this_turn[r][c] = True
    return stable

def reset_flashed(grid, flashed_this_turn):
    for r in range(10):
        for c in range(10):
            if flashed_this_turn[r][c]:
                grid[r][c] = 0

def count_flashes(flashed_this_turn):
    return utils.flatten(flashed_this_turn).count(True)


def get_flashes_and_next_step(grid):
    flashed_this_turn = utils.grid(10, 10, default=False)
    increment_all(grid)
    stable = False
    while not stable:
        stable = flash(grid, flashed_this_turn)
    count = count_flashes(flashed_this_turn)
    reset_flashed(grid, flashed_this_turn)
    return count


def do_part_1(inpt):
    grid = parse(inpt)
    flashes = 0
    for _ in range(100):
        flashes += get_flashes_and_next_step(grid)

    return flashes

def do_part_2(inpt):
    grid = parse(inpt)
    flashes = 0
    for i in range(500):
        count = get_flashes_and_next_step(grid)
        if count == 100:
            return i+1
        flashes += count


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
