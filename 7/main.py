"""https://adventofcode.com/2025/day/7"""

from functools import cache

START = "S"
SPLIT = "^"
AIR = "."


def solve_part1(lines: list) -> int:
    """Part 1 count # of splits"""
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


def solve_part2(lines: list) -> int:
    """Part 2 count total time lines."""
    data = [list(x.strip()) for x in lines]

    start_col = data[0].index(START)

    split_rows = [i for i in data if SPLIT in i]
    assert split_rows

    @cache
    def dp(row_idx: int, col_idx: int) -> int:
        """Number of paths starting at row_idx/col_idx, memoize with @cache."""
        # At the end.
        if row_idx == len(split_rows):
            return 1

        cur_row = split_rows[row_idx]
        print(f"Row idx: {row_idx}, col_idx: {col_idx}")
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


def test_e2e_part1():
    """Test part 1 solution."""
    with open("test_input.txt", "r") as fp:
        assert solve_part1(fp.readlines()) == 21


def test_e2e_part2():
    """Test part 2 solution."""
    with open("test_input.txt", "r") as fp:
        assert solve_part2(fp.readlines()) == 40


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        print(solve_part1(fp.readlines()))
    with open("input.txt", "r") as fp:
        print(solve_part2(fp.readlines()))
