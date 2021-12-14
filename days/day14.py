import collections
from email.mime import base
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint
from more_itertools import windowed

import utils


def parse_inpt(inpt):
    template = inpt[0]
    subs = {}
    for line in inpt[2:]:
        i, o = line.split(' -> ')
        subs[i] = o
    return template, subs

def apply_subs(template, subs):
    pairs = windowed(list(template), 2)
    new_polymer = [template[0]]
    for p in pairs:
        new_polymer.append(subs[''.join(p)])
        new_polymer.append(p[1])

    subs[template] = new_polymer
    return ''.join(new_polymer)

def do_part_1(inpt):
    polymer, subs = parse_inpt(inpt)
    for _ in range(10):
        polymer = apply_subs(polymer, subs)
    
    c = collections.Counter(list(polymer))
    ranks = c.most_common()
    most_common = ranks[0][1]
    least_common = ranks[-1][1]
    return most_common - least_common


def extrapolate_counts(template, subs, n):
    pairs = windowed(list(template), 2)
    base_counts = collections.Counter([''.join(p) for p in pairs])

    for _ in range(n):
        new_counts = collections.Counter()
        for x in base_counts.keys():
            new_counts[x[0] + subs[x]] += base_counts[x]
            new_counts[subs[x] + x[1]] += base_counts[x]
        base_counts = new_counts
    
    final_counts = collections.Counter(template[-1])
    for x in base_counts.keys():
        final_counts[x[0]] += base_counts[x]
    return final_counts


def do_part_2(inpt):
    polymer, subs = parse_inpt(inpt)
    c = extrapolate_counts(polymer, subs, 40)
    ranks = c.most_common()
    return ranks[0][1] - ranks[-1][1]

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
