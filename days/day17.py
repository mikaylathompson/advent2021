import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint
from more_itertools import chunked
from tqdm import t

import utils

def closer_to_0(x):
    if x > 0:
        return x - 1
    elif x < 0:
        return x + 1
    return 0

def next_step(pos, vel):
    return (pos[0] + vel[0], pos[1] + vel[1]), (closer_to_0(vel[0]), vel[1] - 1)

def get_target(inpt):
    fields = parselib.parse("target area: x={x0}..{x1}, y={y0}..{y1}", inpt)
    return {k: int(v) for k,v in fields.named.items()}

def is_within_target(target, pos):
    return target['x0'] <= pos[0] <= target['x1'] and target['y0'] <= pos[1] <= target['y1']

def is_past_target(target, pos):
    return pos[0] > target['x1'] or pos[1] < min(target['y1'], target['y0'])

def is_succesful(target, trajectory, debug=False):
    position = (0, 0)
    max_height = position[1]
    if debug:
        print(f"{position} moving at {trajectory}")
    while not is_past_target(target, position) and trajectory[0] >= 0:
        position, trajectory = next_step(position, trajectory)
        if debug:
            print(f"{position} moving at {trajectory}")
        if position[1] > max_height:
            max_height = position[1]
        if is_within_target(target, position):
            if debug:
                print("Within target.")
            return True, max_height
    if debug:
        position, trajectory = next_step(position, trajectory)
        print(f"Next would be: {position} moving at {trajectory}")
    return False, 0


def do_part_1(inpt):
    target = get_target(inpt[0])
    best_height = 0
    for x in range(0, 221):
        for y in range(0, 1000):
            success, height = is_succesful(target, (x, y))
            if success and height > best_height:
                best_height = height
    return best_height

def parse_succesful(inpt):
    pairs = []
    for line in inpt:
        pairs += [tuple(p) for p in chunked(utils.ints(line), 2)]
    return pairs

def do_part_2(inpt):
    target = get_target(inpt[0])
    print(target)

    success_count = 0
    for x in range(0, 223):
        for y in range(-400, 1600):
            success, _ = is_succesful(target, (x, y))
            if success:
                success_count += 1
    return success_count

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
