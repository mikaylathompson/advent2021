from cmath import inf
import collections
import functools
import itertools
import math
import re
import parse

import utils

def fuel_spend(x, counts):
    return sum([abs(x - key) * val  for key, val in counts.items()])

def cost(x, y):
    return sum(range(1, abs(x - y) + 1))

def fuel_spend_2(x, counts):
    return sum([cost(x, key) * val for key, val in counts.items()])

def do_part_1(inpt):
    vals = utils.ints(inpt[0])
    c = collections.Counter(vals)
    fuel = inf
    for i in range(min(vals), max(vals)):
        i_fuel = fuel_spend(i, c)
        if i_fuel < fuel:
            fuel = i_fuel
    
    return fuel


def do_part_2(inpt):
    vals = utils.ints(inpt[0])
    c = collections.Counter(vals)
    fuel = inf
    for i in range(min(vals), max(vals)):
        i_fuel = fuel_spend_2(i, c)
        if i_fuel < fuel:
            fuel = i_fuel
    
    return fuel

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
