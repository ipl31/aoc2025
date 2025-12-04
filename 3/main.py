"""https://adventofcode.com/2025/day/3"""

import itertools


def _find_bank_max_joltage(bank: int) -> int:
    """Find all permutations for a joltage bank regardless of order, then check
    each value highest to lowest to see if the order is valid for the puzzle."""

    permutations_iter = itertools.permutations(str(bank), 2)
    perms = list(set([int("".join(p)) for p in permutations_iter]))
    perms.sort(reverse=True)
    for p in perms:
        first = str(bank).find(str(p)[0])
        second = str(bank).find(str(p)[1], first + 1)
        if first != -1 and second != -1:
            return p
    raise Exception("This should never happen. Values not found in joltage bank.")


def solve(banks: list):
    """Solve day 3 part 1"""
    joltages = [_find_bank_max_joltage(i) for i in banks]
    return sum(joltages)


def test_e2e():
    """Test using example data from aoc."""
    test_input = [987654321111111, 811111111111119, 234234234234278, 818181911112111]
    assert solve(test_input) == 357


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        banks = fp.readlines()
        print(len(banks))
        joltage = solve(banks)
        print(f"total joltage is {joltage}")
