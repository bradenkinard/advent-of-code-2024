from collections import Counter
from pathlib import Path

from .constants import INPUTS_FOLDER

INPUT_FILE = f"{INPUTS_FOLDER}/day_1/input.txt"


def read_input(filename: str) -> tuple[list[int]]:
    """Read the input data from a text file."""
    list1, list2 = [], []
    with Path.open(filename, "r") as f:
        for line in f:
            vals = line.split()
            list1.append(int(vals[0]))
            list2.append(int(vals[1]))

    return list1, list2


def solve_part1(list1: list[int], list2: list[int]) -> int:
    """Solution for part 1 of the problem.

    Sorts the two lists.
    Finds the pairwise differences.
    Returns the sum of the differences.
    """
    list1.sort()
    list2.sort()
    total = 0
    for pair in zip(list1, list2, strict=True):
        total += abs(pair[0] - pair[1])
    return total


def solve_part2(list1: list[int], list2: list[int]) -> int:
    """Solution for part 2 of the problem.

    Count the number of times each item in list1 appears in list 2.
    Multiply the occurence by the number value.
    Returns the sum of these products.
    """
    frequencies = Counter(list2)
    score = 0
    for i in list1:
        score += frequencies.get(i, 0) * i

    return score


def solve() -> None:
    list1, list2 = read_input(INPUT_FILE)

    solution = solve_part1(list1, list2)
    print(f"Part 1 Solution: {solution}")

    solution2 = solve_part2(list1, list2)
    print(f"Part 2 Solution: {solution2}")
