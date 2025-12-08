"""https://adventofcode.com/2025/day/6"""

import math

COMPUTE = {"+": sum, "*": math.prod}

""" Part 1 """


def solve_part1(lines: list) -> int:
    # pop the operators off
    ops = lines.pop().split()
    # seed the array with the first set of values
    totals = [int(x) for x in lines.pop().split()]

    for line in lines:
        totals = [
            COMPUTE[ops[x]]([totals[x], int(item)])
            for x, item in enumerate(line.split())
        ]
    return sum(totals)


def test_e2e_part1():
    """Test using data from aoc."""
    test_input = ["123 328  51 64", "45 64  387 23", "6 98  215 314", " *   +   *   +"]
    assert solve_part1(test_input) == 4277556


""" Part 2 """


def solve_part2(lines: list) -> int:
    data = [list(l.strip("\n")) for l in lines]
    assert len({len(d) for d in data}) == 1
    data_row_len = len(data[0])
    ops_index = len(data) - 1

    work = []
    total = 0

    for col_idx in reversed(range(data_row_len)):
        number = []
        for row_idx, row in enumerate(data):
            if row[col_idx] in COMPUTE:
                work.append(int("".join(number)))
                total += COMPUTE[row[col_idx]](work)
                work = []
                number = []
            elif row_idx == ops_index:
                continue
            else:
                number.append(row[col_idx])

        try:
            work.append(int("".join(number)))
        except ValueError:
            print("Skipping column, no number.")

    return total


def test_e2e_part2():
    """Test using data from aoc."""
    with open("test_input.txt", "r") as fp:
        assert solve_part2(fp.readlines()) == 3263827


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        total = solve_part1(fp.readlines())
        print(f"Part 1 total is {total}")
    with open("input.txt", "r") as fp:
        total = solve_part2(fp.readlines())
        print(f"Part 2 total is {total}")
