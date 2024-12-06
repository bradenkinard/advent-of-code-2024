from pathlib import Path

from .constants import INPUTS_FOLDER

INPUT_FILE = f"{INPUTS_FOLDER}/day_2/input.txt"


def read_inputs(filename: str) -> list[list[int]]:
    with Path.open(filename, "r") as f:
        return [[int(i) for i in line.split()] for line in f]


def levels_safe(
    level1: int,
    level2: int,
    direction: int,
) -> bool:
    diff = level2 - level1
    sign = -1 if diff < 0 else 1
    abs_diff = abs(diff)
    if sign == direction and abs_diff >= 1 and abs_diff <= 3:
        return True
    return False


def report_is_safe(report: list[int]) -> bool:
    increasing = True
    decreasing = True

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if diff > 0:
            decreasing = False
        if diff < 0:
            increasing = False

    return increasing or decreasing


def report_is_safe_with_dampener(report: list[int]) -> bool:
    if report_is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if report_is_safe(modified_report):
            return True

    return False


def solve() -> None:
    reports = read_inputs(INPUT_FILE)
    total_safe = 0
    for report in reports:
        if report_is_safe(report):
            total_safe += 1

    print(f"Part 1 Solution: {total_safe}")

    total_safe = 0
    for report in reports:
        if report_is_safe_with_dampener(report):
            total_safe += 1

    print(f"Part 2 Solution: {total_safe}")
