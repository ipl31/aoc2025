"""https://adventofcode.com/2025/day/3"""


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


def solve(rows: list):
    """Solve day 4"""
    grid = [[i for i in row] for row in rows]
    # All rows should be the same len
    assert len(set(len(i) for i in rows)) == 1
    movables_count = 0
    PAPER_CHAR = "@"
    for row_idx, row in enumerate(rows):
        for cell_idx, cell in enumerate(row):
            if (
                grid[row_idx][cell_idx] == PAPER_CHAR
                and _get_neighbors(grid, (row_idx, cell_idx)).count(PAPER_CHAR) < 4
            ):
                movables_count += 1
    return movables_count


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
    assert solve(test_input) == 13


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        count = solve(fp.readlines())
        print(f"Can move {count}")
