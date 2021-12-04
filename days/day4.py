import collections
import functools
import itertools
import math
from operator import is_
import re
import parse

from pprint import pprint
import utils


def process_inpt(inpt):
    draws = [int(x) for x in inpt[0].split(',')]
    boards = []
    board = []
    for line in inpt[2:]:
        if line == "":
            boards.append(board)
            board = []
            continue
        ns = [int(x) for x in line.strip().split()]
        board.append(ns)
    boards.append(board)
    return draws, boards

def mark_n(board, n):
    for row in board:
        if n in row:
            row[row.index(n)] = True
    return board

def is_a_bingo(board):
    for row in board:
        if all(val == True for val in row):
            return True
    for row in utils.transpose(board):
        if all(val == True for val in row):
            return True
    return False

def sum_unmarked(board):
    sum_ = 0
    for row in board:
        sum_ += sum([n for n in row if n != True])
    return sum_


def do_part_1(inpt):
    draws, boards = process_inpt(inpt)
    for n in draws[0:5]:
        for b in boards:
            mark_n(b, n)
    board_statuses = [is_a_bingo(b) for b in boards]
    has_a_winner = any(board_statuses)
    last_n = draws[4]
    for n in draws[5:]:
        if has_a_winner:
            break
        for b in boards:
            mark_n(b, n)
        board_statuses = [is_a_bingo(b) for b in boards]
        has_a_winner = any(board_statuses)
        last_n = n
    
    winning_board = boards[board_statuses.index(True)]
    # print(winning_board)
    # print(last_n)
    # pprint(winning_board)
    return sum_unmarked(winning_board) * last_n



def do_part_2(inpt):
    draws, boards = process_inpt(inpt)
    for n in draws[0:5]:
        for b in boards:
            mark_n(b, n)
    board_statuses = [is_a_bingo(b) for b in boards]
    one_left = board_statuses.count(False) == 1
    last_i = 4
    for i, n in enumerate(draws[5:]):
        if len(boards) == 1:
            last_i = i + 5
            break
        for b in boards:
            mark_n(b, n)
        boards = [b for b in boards if not(is_a_bingo(b))]

    for n in draws[last_i:]:
        mark_n(boards[0], n)
        if is_a_bingo(boards[0]):
            return sum_unmarked(boards[0]) * n

    return None


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
