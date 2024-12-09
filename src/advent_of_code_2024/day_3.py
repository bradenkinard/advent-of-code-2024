from dataclasses import dataclass
from pathlib import Path
import re

from .constants import INPUTS_FOLDER

INPUT_FILE = f"{INPUTS_FOLDER}/day_3/input.txt"


def read_input(filename: str) -> str:
    """Read the input data from a text file."""
    with Path.open(filename, "r") as f:
        return f.read()


@dataclass
class MulExpression:
    m1: int
    m2: int

    def evaluate(self) -> int:
        return self.m1 * self.m2


def extract_valid_expressions(text: str) -> list[MulExpression]:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, text)


def parse_expression(exp_str: str) -> MulExpression:
    int1, int2 = exp_str.strip("mul(").strip(")").split(",")
    return MulExpression(int(int1), int(int2))


def solve_part_1(text: str) -> int:
    sum = 0
    for exp in extract_valid_expressions(text):
        sum += parse_expression(exp).evaluate()
    return sum


def solve() -> None:
    text = read_input(INPUT_FILE)
    print(f"Part 1 Solution: {solve_part_1(text)}")
