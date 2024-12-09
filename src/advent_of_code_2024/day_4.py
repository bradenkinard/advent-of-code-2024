from pathlib import Path

from .constants import INPUTS_FOLDER

INPUT_FILE = f"{INPUTS_FOLDER}/day_4/input.txt"


def read_input(filename: str) -> list[str]:
    """Read the input data from a text file."""
    with Path.open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def search_right(i: int, j: int, length: int) -> str:
    i_idx = [i] * length
    j_idx = list(range(j, j + length))
    return list(zip(i_idx, j_idx))


def search_left(i: int, j: int, length: int) -> str:
    i_idx = [i] * length
    j_idx = list(range(j, j - length, -1))
    return list(zip(i_idx, j_idx))


def search_up(i: int, j: int, length: int) -> str:
    i_idx = list(range(i, i - length, -1))
    j_idx = [j] * length
    return list(zip(i_idx, j_idx))


def search_down(i: int, j: int, length: int) -> str:
    i_idx = list(range(i, i + length))
    j_idx = [j] * length
    return list(zip(i_idx, j_idx))


def search_upleft(i: int, j: int, length: int) -> str:
    i_idx = list(range(i, i - length, -1))
    j_idx = list(range(j, j - length, -1))
    return list(zip(i_idx, j_idx))


def search_downleft(i: int, j: int, length: int) -> str:
    i_idx = list(range(i, i + length))
    j_idx = list(range(j, j - length, -1))
    return list(zip(i_idx, j_idx))


def search_upright(i: int, j: int, length: int) -> str:
    i_idx = list(range(i, i - length, -1))
    j_idx = list(range(j, j + length))
    return list(zip(i_idx, j_idx))


def search_downright(i: int, j: int, length: int) -> str:
    i_idx = list(range(i, i + length))
    j_idx = list(range(j, j + length))
    return list(zip(i_idx, j_idx))


def get_substring(idx_list: list[tuple[int]], lines: list[str]) -> str:
    substr = []
    for i, j in idx_list:
        if i >= 0 and i < len(lines) and j >= 0 and j < len(lines[0]):
            substr.append(lines[i][j])
    return "".join(substr)


def solve_part_1(lines: list[str]) -> int:
    """"""
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "X":
                substr_idx = [
                    f(i, j, 4)
                    for f in [
                        search_left,
                        search_right,
                        search_down,
                        search_up,
                        search_upleft,
                        search_downleft,
                        search_upright,
                        search_downright,
                    ]
                ]
                for idx in substr_idx:
                    total += int(get_substring(idx, lines) == "XMAS")
    return total


def solve() -> None:
    text = read_input(INPUT_FILE)
    print(f"Part 1 Solution: {solve_part_1(text)}")
