import requests
import os

USER_AGENT = "adventofcode_working_directories_creator"
YEAR = 2021

def load_file(fname):
    with open('inputs/' + fname, 'r') as f:
        return [l.strip() for l in f.readlines()]


def load_as_ints(fname):
    return [int(x) for x in load_file(fname)]


def download_input(day):
    user_session_id = os.environ.get('AOC_USER_SESSION_ID')
    link = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    with requests.get(url=link, cookies={"session": user_session_id}, headers={"User-Agent": USER_AGENT}) as response:
        if response.ok:
            data = response.text
            input = open(f"inputs/day{day}.input", "w+")
            input.write(data.rstrip("\n"))
            input.close()
            return f"day{day}.input"
        else:
            print("Server response for input is not valid.")
