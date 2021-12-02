import collections
import functools
import itertools
import math
import re

import parse
import utils


def do_part_1(inpt):
    depth = 0
    distance = 0
    for line in inpt:
        direction, quantity = line.split(' ')
        if direction == "forward":
            distance += int(quantity)
        elif direction == "down":
            depth += int(quantity)
        else:
            depth -= int(quantity)

    return depth * distance

def do_part_2(inpt):
    depth = 0
    distance = 0
    aim = 0
    for line in inpt:
        direction, quantity = line.split(' ')
        if direction == "forward":
            distance += int(quantity)
            depth += aim * int(quantity)
        elif direction == "down":
            aim += int(quantity)
        else:
            aim -= int(quantity)

    return depth * distance

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
