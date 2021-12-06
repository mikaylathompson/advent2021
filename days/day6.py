import collections
import functools
import itertools
import math
import re
import parse

import utils

TIME_TO_REPRO = 6
TIME_TO_FIRST_REPRO = 8

def next_day(fish):
    zeros = fish.count(0)
    return [f-1 if f > 0 else TIME_TO_REPRO for f in fish] + [TIME_TO_FIRST_REPRO] * zeros

def next_day_2(fish):
    return {
        0: fish[1],
        1: fish[2],
        2: fish[3],
        3: fish[4],
        4: fish[5],
        5: fish[6],
        6: (fish[7] if 7 in fish else 0) + fish[0],
        7: fish[8] if 8 in fish else 0,
        8: fish[0]
    }


def do_part_1(inpt):
    fish = utils.ints(inpt[0])
    for _ in range(80):
        # print(fish)
        fish = next_day(fish)
    return len(fish)

def do_part_2(inpt):
    fish = collections.Counter(utils.ints(inpt[0]))
    for i in range(256):
        # print(f"Day {i}: {fish} = {sum(fish.values())}")
        fish = next_day_2(fish)
    print(fish)
    return sum(fish.values())


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
