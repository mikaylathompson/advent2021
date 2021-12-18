import collections
import functools
import itertools
import math
import re
import parse as parselib
# from pprint import pprint

import utils
of_interest = r"\d+|[\[\]]"

def reconstitute_chars(chars):
    lst = [chars[0]]
    last_char = chars[0]
    for char in chars[1:]:
        if last_char == '[' and char == '[':
            lst.append(char)
        elif last_char == ']' and char == ']':
            lst.append(char)
        elif last_char == ']' and char == '[':
            lst.append(', ')
            lst.append(char)
        elif last_char == '[': # char must be an int
            lst.append(char)
        elif last_char == ']': # char must be an int
            lst.append(', ')
            lst.append(char)
        elif char == ']': # last_char is an int
            lst.append(char)
        else: # last_char is an int
            lst.append(', ')
            lst.append(char)
        last_char = char
    return eval(''.join(lst))


def reduce(x):
    static = True
    chars_of_interest = re.findall(of_interest, str(x))

    # EXPLODE
    depth_count = 0
    to_left = None
    start_of_nested_pair = None
    end_of_nested_pair = None
    # print("pre reduction")
    # print(x)
    # print([f"{i}:{char}" for i, char in enumerate(chars_of_interest)])
    for i, char in enumerate(chars_of_interest):
        if char == '[':
            depth_count += 1
        elif char == ']':
            depth_count -= 1
        else:
            val = int(char)
            # possible uses for this number:
            # - it is the to-the-left value
            if depth_count < 5 and not end_of_nested_pair:
                to_left = i
            # it is the to-the-right value
            elif end_of_nested_pair:
                chars_of_interest[i] = str(val + int(chars_of_interest[end_of_nested_pair-1]))
                static = False
                break
            else:
                # - it is the left entry of a 5 deep pair
                if not start_of_nested_pair: # pair hasn't been found yet
                    start_of_nested_pair = i - 1 # bracket to the left
                    if to_left:
                        chars_of_interest[to_left] = str(val + int(chars_of_interest[to_left]))
                # - it is the right entry of a 5 deep pair
                elif not end_of_nested_pair:
                    end_of_nested_pair = i + 1 # bracket to the right
                    static = False
    if start_of_nested_pair:
        chars_of_interest[start_of_nested_pair:end_of_nested_pair+1] = ['0']

    # print(' '.join(chars_of_interest))
    # print(reconstitute_chars(chars_of_interest))
    if not static:
        # print("EXPLODE")
        return reduce(reconstitute_chars(chars_of_interest))

    # If any regular number is 10 or greater, the leftmost such regular number splits.
    # SPLIT
    for i, char in enumerate(chars_of_interest):
        if char.isnumeric() and int(char) >= 10:
            static = False
            val = int(char)
            chars_of_interest.pop(i)
            chars_of_interest.insert(i, '[')
            chars_of_interest.insert(i+1, str(val // 2))
            chars_of_interest.insert(i+2, str(math.ceil(val / 2)))
            chars_of_interest.insert(i+3, ']')
            break
    
    if not static:
        # print("SPLIT")
        return reduce(reconstitute_chars(chars_of_interest))

    return reconstitute_chars(chars_of_interest)


def add(x, y):
    # print([x, y])
    return reduce([x, y])


def magnitude(x):
    if type(x) is list:
        return magnitude(x[0]) * 3 + magnitude(x[1]) * 2
    else:
        return x

def do_part_1(inpt):
    ns = [eval(line) for line in inpt]
    result = ns[0]
    for n in ns[1:]:
        # print(f"Adding {n}")
        result = add(result, n)
        # print(result)
    return magnitude(reduce(result))

def do_part_2(inpt):
    ns = [eval(line) for line in inpt]
    largest_mag = 0
    for x, y in itertools.product(ns, ns):
        if x != y:
            mag = magnitude(add(x, y))
            if mag > largest_mag:
                largest_mag = mag
    return largest_mag
        

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
