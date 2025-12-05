"""https://adventofcode.com/2025/day/5"""

import bisect


def _merge_ranges(ranges: list[str]) -> list[list[int, int]]:
    """Merge list of ranges into non-overlapping list of ranges (see test input example)."""
    RANGE_DELIM = "-"
    merged_ranges = []
    ranges = [
        [int(i.split(RANGE_DELIM)[0]), int(i.split(RANGE_DELIM)[1])] for i in ranges
    ]
    ranges.sort()
    assert set([len(x) for x in ranges]) == {2}

    """ More concise version AI generated from my code that better leverages the fact the lists are ordered. """
    for start, end in ranges:
        # if we are starting fresh or range starts after last entry just add it.
        if len(merged_ranges) == 0 or start > merged_ranges[-1][1]:
            merged_ranges.append([start, end])
        # Otherwise we are starting inclusive so extend the range if end is greater than current end.
        merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    """ My original less concise impl:

    for start, end in ranges:
        merged = False
        if len(merged_ranges) == 0:
            merged_ranges.append([start, end])
            merged = True
            continue

        for mr in merged_ranges:
            if start <= mr[1] and end <= mr[1]:
                merged = True
                break
            if start <= mr[1] and end >= mr[1]:
                mr[1] = end
                merged = True
                break
        if not merged:
            merged_ranges.append([start, end])
    """
    return merged_ranges


def _is_fresh(ranges: list[list[int, int]], starts: list[int], ingredient: int) -> bool:
    idx = bisect.bisect_right(starts, ingredient) - 1
    if idx == -1:
        return False
    start, end = ranges[idx]
    return start <= ingredient <= end


def _sum_fresh(ranges: list[list[int, int]]) -> bool:
    total = 0
    for r in ranges:
        assert r[1] >= r[0]
        if r[0] == r[1]:
            total += 1
            continue
        total += r[1] - r[0] + 1
    return total


def solve(ranges: list, ingredients: list) -> tuple[int, int]:
    merged_ranges = _merge_ranges(ranges)
    range_starts = [i for i, _ in merged_ranges]
    fresh_count = 0
    # Problem 1, count fresh ingredients available
    for i in ingredients:
        if _is_fresh(merged_ranges, range_starts, int(i)):
            fresh_count += 1
    # Problem 2, count all possible fresh ingredients
    return fresh_count, _sum_fresh(merged_ranges)


def test_e2e():
    """Test using data from aoc."""
    test_ranges = ["3-5", "10-14", "16-20", "12-18"]
    test_ingredients = [1, 5, 8, 11, 17, 32]
    assert solve(test_ranges, test_ingredients) == (3, 14)


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        lines = fp.read().splitlines()
        file_split = lines.index("")
        ranges = lines[:file_split]
        ingredients = lines[file_split + 1 :]
        count = solve(ranges, ingredients)
        print(f"Fresh ingredient and total fresh count {count}")
