"""https://adventofcode.com/2025/day/1"""

from typing import Any

import numpy as np
from numpy.typing import NDArray


def _turn_dial(dial: NDArray[Any], adjustment: str) -> NDArray[Any]:
    """Simulate dial turn with np array roll."""
    LEFT = "l"
    RIGHT = "r"
    direction, count = adjustment[:1].lower(), int(adjustment[1:])
    print(f"Turn requested {adjustment} {direction} {count}")
    assert direction in (LEFT, RIGHT)
    assert count in range(0, 100)
    if direction == LEFT:
        count = -count
        print(count)
    return np.roll(dial, count)

def solve(turns: list) -> int:
    """Solve day 1, count times dial is in pos 0, start dial at 50"""
    dial = np.array(range(0, 100))
    dial = np.roll(dial, 50)
    assert dial.item(0) == 50
    z_count = 0
    for turn in turns:
        dial = _turn_dial(dial, turn)
        if dial.item(0) == 0:
            z_count += 1
    return z_count


def test_e2e():
    """Test using example data from aoc."""
    turns = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    assert solve(turns) == 3

if __name__ == "__main__":
    turns = []
    print(f"Password is {solve(turns)}")
