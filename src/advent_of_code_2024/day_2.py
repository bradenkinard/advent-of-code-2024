from pathlib import Path

from .constants import INPUTS_FOLDER

INPUT_FILE = f"{INPUTS_FOLDER}/day_2/input.txt"


def read_inputs(filename: str) -> list[list[int]]:
    with Path.open(filename, "r") as f:
        return [[int(i) for i in line.split()] for line in f]


def report_is_safe(report: list[int], min_diff: int = 1, max_diff: int = 3) -> bool:
    sign = 1 if report[0] < report[1] else -1
    for i in range(len(report) - 1):
        diff = (report[i + 1] - report[i]) * sign
        if diff < min_diff or diff > max_diff:
            return False
    return True


def solve() -> None:
    reports = read_inputs(INPUT_FILE)
    total_safe = 0
    for report in reports:
        if report_is_safe(report, min_diff=1, max_diff=3):
            total_safe += 1

    print(f"Part 1 Solution: {total_safe}")
