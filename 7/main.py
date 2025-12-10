"""https://adventofcode.com/2025/day/7"""

from functools import cache

START = "S"
SPLIT = "^"
AIR = "."


""" Part 1 """


def solve_part1(lines: list) -> int:
    data = [list(x.strip()) for x in lines]

    beam_points = []
    split_counter = 0
    for row in data:
        if START not in row and SPLIT not in row:
            continue
        if START in row:
            assert not beam_points
            beam_points = [i for i, x in enumerate(row) if x == START]
            assert len(beam_points) == 1
        else:
            split_beams = {
                i for i, x in enumerate(row) if i in beam_points and x == SPLIT
            }
            unsplit_beams = {
                i for i, x in enumerate(row) if i in beam_points and x == AIR
            }
            split_counter += len(split_beams)
            beam_points = (
                [i - 1 for i in split_beams]
                + [i + 1 for i in split_beams]
                + list(unsplit_beams)
            )

    return split_counter


""" Part 2 """

def solve_part_2(lines: list) -> int:
    data = [list(x.strip() for x in lines)]
    row_count = len(data)

    start_col = data[0].index(START)

    split_rows = [i for i in data if SPLIT in i]
    assert split_rows

    @cache
    def dp(row_idx: int, col_idx: int) -> int:
        """Number of paths starting at row_idx/col_idx"""
        cur_row = split_rows[row_idx]
        worlds = 0

        if cur_row[col_idx] == SPLIT:
            # left/right shift, avoid wrap
            if col_idx - 1 >= 0:
                worlds += dp(row_idx + 1, col_idx - 1)
            if col_idx + 1 < len(cur_row):
                worlds += dp(row_idx + 1, col_idx + 1)
        else:
            worlds += dp(row_idx + 1, col_idx)
        return worlds

    # We know where the first splitter will be. First row at START col.
    return dp(0, start_col)

"""
def old_solve_part2(lines: list) -> int:
    exec_count = 50_000_000
    chunksize = 1000
    data = [list(x.strip()) for x in lines]
    start_row = data.pop(0)
    start = [i for i, x in enumerate(start_row) if x == START].pop()
    print(f"Path starts on row 0 col {start}")

    # clean rows with no splits to shorten loops.
    data = [x for x in data if SPLIT in x]

    work = partial(_sub_solve_part2, data, start)

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(work, range(exec_count), chunksize=chunksize)
    return len(set(results))


def _old_sub_solve_part2(data: list, start: int, *args, **kwargs) -> str:
    beam_point = start
    path = []
    for row in data:
        if SPLIT not in row:
            continue
        if row[beam_point] == SPLIT:
            beam_point += random.choice((-1, 1))
        path.append(beam_point)
    return ",".join(map(str, path))
"""


def test_e2e_part1():
    with open("test_input.txt", "r") as fp:
        assert solve_part1(fp.readlines()) == 21


def test_e2e_part2():
    with open("test_input.txt", "r") as fp:
        assert solve_part2(fp.readlines()) == 40


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        print(solve_part1(fp.readlines()))
    with open("input.txt", "r") as fp:
        print(solve_part2(fp.readlines()))
