import collections
import functools
import itertools
import math
import re
import parse

import utils


displays = """
0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 """

activated_segments = [set('abcefg'), set('cf'), set('acdeg'), set('acdfg'), set('bcdf'),
    set('abdfg'), set('abdefg'), set('acf'), set('abcdefg'), set('abcdfg')]
segments_per_number = [len(segs) for segs in activated_segments]
numbers_of_unique_length = [1, 4, 7, 8]
lengths_of_unique_length = [segments_per_number[i] for i in numbers_of_unique_length]

all_possible_orderings = list(itertools.permutations('abcdefg'))
all_translation_tables = [str.maketrans(''.join(all_possible_orderings[0]), ''.join(x)) for x in all_possible_orderings]

def parse(line):
    samples, values = line.split('|')
    return samples.split(), values.split()

def do_part_1(inpt):
    count = 0
    for line in inpt:
        _, values = parse(line)
        for v in values:
            if len(v) in lengths_of_unique_length:
                count += 1
    return count


def is_valid_permutation(trans, samples):
    for s in samples:
        translated = s.translate(trans)
        if set(translated) not in activated_segments:
            return False
    return True

def translated_value(trans, value):
    return activated_segments.index(set(value.translate(trans)))

def determine_mapping(samples):
    potential_mappings = [t for t in all_translation_tables if is_valid_permutation(t, samples)]
    assert len(potential_mappings) == 1
    return potential_mappings[0]

def concat_values(values):
    return int(''.join(str(v) for v in values))

def do_part_2(inpt):
    total = 0
    for line in inpt:
        samples, values = parse(line)
        mapping = determine_mapping(samples)
        total += concat_values([translated_value(mapping, v) for v in values])
    return total


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
