import sys
import re


def read_input(split_lines=True):
    day = sys.argv[0].split(".")[0]
    is_test = "test" in sys.argv[1:]
    name = "test" if is_test else "in"
    with open(f"data/{day}/{name}.txt") as f:
        if split_lines:
            return f.read().splitlines()
        return f.read()


DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIAG_DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def nums(s):
    return [int(x) for x in re.findall(r"-?\d+", s)]
