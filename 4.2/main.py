"""https://adventofcode.com/2025/day/4"""

import copy


def _get_neighbors(grid, pos):
    """Get adajent cells for a given x,y"""
    neighbors = []
    x, y = pos
    neighbors_rel_xy = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    assert len(neighbors_rel_xy) == 8

    for _x, _y in neighbors_rel_xy:
        if 0 <= _x < len(grid) and 0 <= _y < len(grid[0]):
            neighbors.append(grid[_x][_y])
    return neighbors


def _move_paper(grid: list) -> (int, list):
    """Remove all moveable paper rolls (less than 4 neighbors) in grids starting state.
    Return a count of moved paper rolls and an updated grid reflecting removed rolls."""
    # All rows should be the same len
    assert len(set(len(i) for i in grid)) == 1
    grid_copy = copy.deepcopy(grid)
    movables_count = 0
    PAPER_CHAR = "@"
    EMPTY_CHAR = "."
    for row_idx, row in enumerate(grid):
        for cell_idx, cell in enumerate(row):
            if (
                grid[row_idx][cell_idx] == PAPER_CHAR
                and _get_neighbors(grid, (row_idx, cell_idx)).count(PAPER_CHAR) < 4
            ):
                grid_copy[row_idx][cell_idx] = EMPTY_CHAR
                movables_count += 1
    return movables_count, grid_copy


def solve(rows: list) -> int:
    grid = [[i for i in row] for row in rows]
    keep_working = True
    total_count = 0
    while keep_working:
        count, grid = _move_paper(grid)
        assert count >= 0
        total_count += count
        keep_working = False if count == 0 else True
    return total_count


def test_e2e():
    """Test using data from aoc."""
    test_input = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
    assert solve(test_input) == 43 


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        count = solve(fp.readlines())
        print(f"Can move {count}")
