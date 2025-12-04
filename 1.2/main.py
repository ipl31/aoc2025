"""https://adventofcode.com/2025/day/2"""

import itertools
from typing import Any, Tuple

import numpy as np
from numpy.typing import NDArray


def _turn_dial_and_count_zeroes(
    dial: NDArray[Any], adjustment: str
) -> tuple[NDArray[Any], int]:
    """Simulate dial turn with np array roll and count clicks landing on zero."""
    LEFT = "l"
    RIGHT = "r"
    direction, clicks = adjustment[:1].lower(), int(adjustment[1:])
    print(f"Turn requested {adjustment}")
    assert direction in (LEFT, RIGHT)

    z_count = 0
    for i in itertools.count(1):
        if i > clicks:
            break
        single_click = -1 if direction == LEFT else 1
        dial = np.roll(dial, single_click)
        if dial.item(0) == 0:
            z_count += 1

    return (dial, z_count)


def solve(turns: list) -> int:
    """Solve day 1 part 2, count times dial is in pos 0, start dial at 50"""
    dial = np.array(range(0, 100))
    dial = np.roll(dial, 50)
    assert dial.item(0) == 50
    z_count = 0
    for turn in turns:
        dial, _z_count = _turn_dial_and_count_zeroes(dial, turn)
        z_count += _z_count
    return z_count


def test_e2e():
    """Test using example data from aoc."""
    turns = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    assert solve(turns) == 6


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        count = solve(fp.readlines())
        print(f"Password is {count}")
