"""https://adventofcode.com/2025/day/2"""


def _enumerate_ids(ranges_csv) -> list:
    """enumerate all the ids in the problem input csv of dashed ranges."""
    ranges = ranges_csv.split(",")
    ids = []
    for r in ranges:
        assert len(r.split("-")) == 2
        start = int(r.split("-")[0])
        end = 1 + int(r.split("-")[1])
        ids += list(range(start, end))
    return ids


def _is_id_busted(product_id: str) -> bool:
    """check if an id is bad."""
    assert isinstance(product_id, str)
    slice_index = int(len(product_id) / 2)
    first, last = product_id[:slice_index], product_id[slice_index:]
    assert len(first) == len(last)
    if first == last:
        return True
    return False


def _filter_busted_ids(product_ids: list) -> list:
    """Find ids composed of repeating numbers."""
    # assuming ids are never negative.
    even_len_ids = [str(abs(i)) for i in product_ids if len(str(abs(i))) % 2 == 0]
    return [int(i) for i in even_len_ids if _is_id_busted(i)]


def solve(id_ranges):
    """Solve day 2 part 1"""
    ids = _enumerate_ids(id_ranges)
    return sum(_filter_busted_ids(ids))


def test_e2e():
    """Test using example data from aoc."""
    test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    assert solve(test_input) == 1227775554


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        busted_id_sum = solve(fp.readlines()[0])
        print(f"Sum of busted ids is {busted_id_sum}")
