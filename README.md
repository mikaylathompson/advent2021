# Advent of Code 2021

This repo contains my runner script and template code, as well as daily solutions for Advent of Code 2021.
It can be used simply by cloning and using the `./advent.py` script as described below, but for `--download` to work,
you need to obtain your User Sesssion Id cookie from the AoC site, and set it as a `AOC_USER_SESSION_ID` env var.

# Usage:

```
./advent.py [--day D] [--part P] [--test] [--download] [--setup]
```

Run the code found in `days/day{D}.py`, using the specified D, or by default one day past the present (to account for
release at midnight eastern time, which is on the previous day in Mountain time)
If `--part P` is provided (valid values are 1 or 2), only that part will be run, otherwise both will be.
`--test` means that the input file used will be `inputs/day{D}.test`, otherwise it will be `inputs/day{D}.input`
If `--download` is included, the script will use the env var AOC_USER_SESSION_ID to download the input from the source,
and save it as `inputs/day{D}.input`.
If `--setup` is provided, no daily code is run, but it will set up the template file for day D in `days/day{D}.py`


As an example of a daily workflow, shortly before the puzzle opens, you can run:
```
./advent.py --setup
```
to create new dayX.py and dayX.test files.

Once the puzzle is open, copy the test input into dayX.test, write code and test it with 
```
./advent.py --test
```

To download and run on the real input, use
```
./advent.py --download
```

If Part 1 is time intensive, run only Part 2 with
```
./advent.py --part 2
```