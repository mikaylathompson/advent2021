import collections
import functools
import itertools
import math
import re
import parse
from copy import deepcopy

import utils


def do_part_1(inpt):
    digit_counts = [0] * len(inpt[0])
    for line in inpt:
        for i in range(len(line)):
            if line[i] == '0':
                digit_counts[i] -= 1
            else:
                digit_counts[i] += 1

    gamma = ''.join(['0' if d < 0 else '1' for d in digit_counts])
    epsilon = ''.join(['1' if d < 0 else '0' for d in digit_counts])

    return int(gamma, base=2) * int(epsilon, base=2)

def get_counts(inpt, i):
    count = 0
    for line in inpt:
        if line[i] == '0':
            count -= 1
        else:
            count += 1
    return count

def oxygen_generator_rating(inpt):
    candidates = deepcopy(inpt)
    i = 0
    while len(candidates) > 1:
        required_value = '0' if get_counts(candidates, i) < 0 else '1'
        candidates = [c for c in candidates if c[i] == required_value]
        i += 1
    return int(candidates[0], base=2)

def co2_scrubber_rating(inpt):
    candidates = deepcopy(inpt)
    i = 0
    while len(candidates) > 1:
        required_value = '1' if get_counts(candidates, i) < 0 else '0'
        candidates = [c for c in candidates if c[i] == required_value]
        i += 1
    return int(candidates[0], base=2)

def do_part_2(inpt):
    oxy = oxygen_generator_rating(inpt)
    co2 = co2_scrubber_rating(inpt)
    return oxy * co2

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
