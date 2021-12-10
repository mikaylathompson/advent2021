import collections
import functools
import itertools
import math
import re
import parse
import statistics

from collections import deque

import utils

open_chars = '{([<'
close_chars = '})]>'
match = {open_chars[i]: close_chars[i] for i in range(4)}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
points2 = {')': 1, ']': 2, '}': 3, '>': 4}

def possible_traversal(line, stack):
    if len(line) == 0:
        return True, stack
    if line[0] in close_chars:
        if not match[stack.pop()] == line[0]:
            return False, line[0]
        else:
            return possible_traversal(line[1:], stack)
    else:
        stack.append(line[0])
        return possible_traversal(line[1:], stack)


def do_part_1(inpt):
    score = 0
    for line in inpt:
        valid, remainderOrIllegal = possible_traversal(line, deque())
        if not valid:
            score += points[remainderOrIllegal]
    return score
    

def do_part_2(inpt):
    scores = []
    for line in inpt:
        valid, stack = possible_traversal(line, deque())
        if valid:
            linescore = 0
            while len(stack) > 0:
                linescore = (linescore * 5) + points2[match[stack.pop()]]
            scores.append(linescore)
    return statistics.median(scores)

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
