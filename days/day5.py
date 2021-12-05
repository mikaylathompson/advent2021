import collections
import functools
import itertools
import math
import re
import parse

import utils


class Line():
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    
    def covers(self, incl_diag=False):
        if self.x0 == self.x1:
            return [(self.x0, y) for y in range(min(self.y0, self.y1), max(self.y0, self.y1) + 1)]
        elif self.y0 == self.y1:
            return [(x, self.y0) for x in range(min(self.x0, self.x1), max(self.x0, self.x1) + 1)]
        elif incl_diag:
            l = [(self.x0, self.y0)]
            i = 1
            xmultiplier = 1 if self.x0 < self.x1 else -1
            ymultiplier = 1 if self.y0 < self.y1 else -1
            while (self.x0 + (i * xmultiplier) != self.x1):
                l.append((self.x0 + (i * xmultiplier), self.y0 + (i * ymultiplier)))
                i += 1
            l.append((self.x1, self.y1))
            return l
        else:
            return []

def get_lines(inpt):
    lines = []
    for line in inpt:
        p0, p1 = line.split(' -> ')
        x0, y0 = p0.split(',')
        x1, y1 = p1.split(',')
        lines.append(Line(int(x0), int(y0), int(x1), int(y1)))
    return lines



def do_part_1(inpt):
    lines = get_lines(inpt)

    covered_points = utils.flatten([p.covers() for p in lines])
    c = collections.Counter(covered_points)
    return len([k for k, v in c.items() if v >= 2])

def do_part_2(inpt):
    lines = get_lines(inpt)

    covered_points = utils.flatten([p.covers(incl_diag=True) for p in lines])
    c = collections.Counter(covered_points)
    return len([k for k, v in c.items() if v >= 2])


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
