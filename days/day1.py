import collections
import functools
import itertools
import math
import re

import utils


def do_part_1(inpt):
    count = 0
    for i in range(1, len(inpt)):
        if inpt[i] > inpt[i-1]:
            count += 1
    return count

def do_part_2(inpt):
    count = 0
    for i in range(3, len(inpt)):
        # first_window = inpt[i-1] + inpt[i-2] + inpt[i-3]
        # second_window = inpt[i] + inpt[i-1] + inpt[i-2]
        if inpt[i] > inpt[i-3]:
            count += 1
    return count


def go(input_file, part):
    inpt = utils.load_as_ints(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
