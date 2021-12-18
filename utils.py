import requests
import os
import math
import re

USER_AGENT = "adventofcode_working_directories_creator"
YEAR = 2021


# Input file things

def load_input_file(fname):
    with open('inputs/' + fname, 'r') as f:
        return [l.strip() for l in f.readlines()]


def load_as_ints(fname):
    return [int(x) for x in load_input_file(fname)]

def load_as_grid(fname, type_=int, sep=" "):
    grid = []
    for line in load_input_file(fname):
        if sep is None:
            grid.append([type_(x) for x in list(line)])
        else:
            grid.append([type_(x) for x in line.split(sep)])
    return grid


def download_input(day):
    user_session_id = os.environ.get('AOC_USER_SESSION_ID')
    link = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    with requests.get(url=link, cookies={"session": user_session_id}, headers={"User-Agent": USER_AGENT}) as response:
        if response.ok:
            data = response.text
            if not os.path.exists("inputs"):
                os.mkdir("inputs")
            input = open(f"inputs/day{day}.input", "w+")
            input.write(data.rstrip("\n"))
            input.close()
            return f"day{day}.input"
        else:
            print("Server response for input is not valid.")


# Solving things
def transpose(l):
    return list(map(list, zip(*l)))


FOUR_DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

EIGHT_DIRECTIONS = FOUR_DIRECTIONS + [
    (1, 1),
    (-1, 1),
    (-1, -1),
    (1, -1)
]

CARDINAL_DIRECTIONS = {
    'N': FOUR_DIRECTIONS[0],
    'S': FOUR_DIRECTIONS[2],
    'E': FOUR_DIRECTIONS[1],
    'W': FOUR_DIRECTIONS[3]
}

def grid(x, y, default=None):
    return [[default for _ in range(x)] for _ in range(y)]

def get_neighbor_coordinates(point, grid_dimensions, incl_diagonals=False):
    neighbors = set()
    for d in (FOUR_DIRECTIONS if not incl_diagonals else EIGHT_DIRECTIONS):
        x = point[0] + d[0]
        y = point[1] + d[1]
        if 0 <= x <= (grid_dimensions[0] - 1) and 0 <= y <= (grid_dimensions[1] - 1):
            neighbors.add((x, y))
    return neighbors

letters = set('abcdefghijklmnopqrstuvwxyz')
vowels = set('aeiou')
consonants = letters - vowels

def lcm(a, b):
    return a * b / math.gcd(a, b)

def ints(s):
    return [int(x) for x in re.findall(r"[\d-]+", s)]

def flatten(lst):
    return [item for sublist in lst for item in sublist]