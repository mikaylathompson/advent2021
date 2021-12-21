import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

def deterministic_die():
    i = 0
    while True:
        yield (i % 100) + 1
        i += 1    

ns = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def take_turn(starting_position, die):
    new_position = (starting_position + next(die) + next(die) + next(die))
    return ns[new_position % 10]

def do_part_1(inpt):
    players = []
    for line in inpt:
        players.append(int(parselib.parse("Player {p} starting position: {x}", line)['x']))
    scores = [0, 0]

    die = deterministic_die()
    roll_count = 0
    done = False
    while not done:
        for i in range(2):
            # print(f"{players} / {scores} / {roll_count}")        
            new_position = take_turn(players[i], die)
            # print(f"New position: {new_position}")
            roll_count += 3
            players[i] = new_position
            scores[i] += new_position
            if scores[i] >= 1000:
                done = True
                break
    print(scores)
    print(roll_count)
    return min(scores) * roll_count


# after one turn, there are 27 new universes, however, there are only 7 possible new states.
# therefore, I only have to keep track of how many universes are in each state

distribution = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

@functools.lru_cache()
def take_quantum_turn(starting_position):
    return {ns[(starting_position + roll) % 10]: count for roll, count in distribution.items()}


def do_part_2(inpt):
    players = []
    for line in inpt:
        players.append(int(parselib.parse("Player {p} starting position: {x}", line)['x']))
    
    open_games = collections.defaultdict(int)
    open_games[(players[0], players[1], 0, 0, True)] += 1
    won_games = [0, 0]

    while len(open_games) > 0:
        print(f"{len(open_games)}, {won_games}")
        game, start_count = open_games.popitem()
        player1turn = game[-1]
        
        if player1turn:
            new_p1 = take_quantum_turn(game[0])
            for p1_pos, addtl_count in new_p1.items():
                new_game = (p1_pos, game[1], game[2] + p1_pos, game[3], False)
                # print(f"Looking at new position {p1_pos} ({addtl_count}): {new_game}")
                if new_game[2] >= 21:
                    won_games[0] += (start_count * addtl_count)
                else:
                    open_games[new_game] += (start_count * addtl_count)
        else:
            new_p2 = take_quantum_turn(game[1])
            for p2_pos, addtl_count in new_p2.items():
                new_game = (game[0], p2_pos, game[2], game[3] + p2_pos, True)
                if new_game[3] >= 21:
                    won_games[1] += (start_count * addtl_count)
                else:
                    open_games[new_game] += (start_count * addtl_count)
        # player1turn = not player1turn        

    return max(won_games)

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)
