import collections
import functools
import itertools
import math
import re
import parse
from pprint import pprint

import utils

def parse(inpt):
    grid = []
    for line in inpt:
        grid.append([int(x) for x in list(line)])
    return grid

def is_low_point(grid, r, c):
    for d in utils.FOUR_DIRECTIONS:
        try:
            if grid[r][c] >= grid[r+d[0]][c+d[1]]:
                return False
        except IndexError:
            continue
    return True

def do_part_1(inpt):
    grid = parse(inpt)
    risk = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_low_point(grid, r, c):
                risk += grid[r][c] + 1
    return risk

def get_basin_members(lp, grid):
    members = {lp}
    tried = set()
    grid_dimensions = (len(grid), len(grid[0]))
    candidates = utils.get_neighbor_coordinates(lp, grid_dimensions)
    while len(candidates) > 0:
        cand = candidates.pop()
        if cand in tried or cand in members:
            continue
        elif grid[cand[0]][cand[1]] < 9:
            members.add(cand)
            candidates.update(utils.get_neighbor_coordinates(cand, grid_dimensions))
        else:
            tried.add(cand)
    return frozenset(members)


def do_part_2(inpt):
    grid = parse(inpt)
    low_points = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_low_point(grid, r, c):
                low_points.append((r, c))

    basins = {get_basin_members(lp, grid) for lp in low_points}
    basin_sizes = sorted([len(basin) for basin in basins])
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
