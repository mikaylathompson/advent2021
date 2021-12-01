#!/usr/bin/env python3

import utils
import re
import sys
from datetime import date, timedelta
import os
import shutil

def dailyFunction(d):
    exec(f"from days import day{d}")
    return eval(f"day{d}.go")


def run(day, part, test=True, downloadInput=False):
    if downloadInput:
        inputFile = utils.download_input(day)
    elif test:
        inputFile = f"day{day}.test"
    else:
        inputFile = f"day{day}.input"

    print(f"\nDay {day} - Part {part} - {'TEST' if test else 'REAL'} - {inputFile}\n")
    print(dailyFunction(day)(inputFile, part), '\n')


def setup_daily_code(day):
    new_file = f"days/day{day}.py"
    if os.path.exists(new_file):
        print("Refusing to overwrite existing file.")
    else:
        shutil.copy("days/dayN.py", new_file)
    with open(f"inputs/day{day}.test", 'a'):
        pass

# Usage:
# ./advent.py [--day D] [--part P] [--test] [--download] [--setup]
# Run the code found in `days/day{D}.py``, using the specified D, or by default one day past the present (to account for
# release at midnight eastern time, which is on the previous day in Mountain time)
# If `--part P` is provided (valid values are 1 or 2), only that part will be run, otherwise both will be.
# `--test` means that the input file used will be `inputs/day{D}.test`, otherwise it will be `inputs/day{D}.input`
# If `--download` is included, the script will use the env var AOC_USER_SESSION_ID to download the input from the source,
# and save it as `inputs/day{D}.input`.
# If `--setup` is provided, no daily code is run, but it will set up the template file for day D in `days/day{D}.py`
#
# As an example of a daily workflow, shortly before the puzzle opens, you can run:
# `./advent.py --setup`
# to create new dayX.py and dayX.test files.
#
# Once the puzzle is open, copy the test input into dayX.test, write code and test it with 
# `./advent.py --test`
#
# To download and run on the real input, use
# `./advent.py --download`
#
# If Part 1 is time intensive, run only Part 2 with
# `./advent.py --part 2`

if __name__ == "__main__":
    day = int(sys.argv[sys.argv.index('--day') + 1]) if '--day' in sys.argv else (date.today() + timedelta(days=1)).day
    if '--setup' in sys.argv:
        setup_daily_code(day)
        sys.exit()
    part = int(sys.argv[sys.argv.index('--part') + 1]) if '--part' in sys.argv else None
    test = '--test' in sys.argv
    downloadInput = not test and '--download' in sys.argv
    if part:
        run(day, part, test=test, downloadInput=downloadInput)
    else:
        run(day, 1, test=test, downloadInput=downloadInput)
        run(day, 2, test=test, downloadInput=False)



