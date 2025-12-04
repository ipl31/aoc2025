"""https://adventofcode.com/2025/day/3"""

def _find_bank_max_joltage(bank: int) -> int:
    batteries = 12
    bank_str = str(bank)
    bank_len = len(bank_str)
    assert bank_len > batteries

    batteries_to_power = []
    start_idx = 0

    for pos in range(batteries):
        remaining_batteries = batteries - pos
        # last place we can start from to fulfill remaining bat slots.
        max_bound = bank_len - remaining_batteries

        max_value_found = -1
        max_value_idx = start_idx

        for i in range(start_idx, max_bound + 1):
            value = int(bank_str[i])
            if value > max_value_found:
                max_value_found = value
                max_value_idx = i
                # won't find higher than 9
                if value == 9:
                    break

        batteries_to_power.append(str(max_value_found))
        start_idx = max_value_idx + 1
    assert len(batteries_to_power) == batteries
    return int("".join(batteries_to_power))


def solve(banks: list):
    """Solve day 3 part 1"""
    joltages = [_find_bank_max_joltage(int(i)) for i in banks]
    return sum(joltages)


def test_e2e():
    """Test using data from aoc."""
    # Samples from actual problem data.
    test_input = [
        3282814631552455223845495229522528935222522885339443346562862666812722932213358593727594192835645138,
        6863545545464444555563676447546566665474647664456666634564545557666345664476667556444246656467666764,
    ]
    assert solve(test_input) == 1877777776422
    # Sample data provided in explanation.
    test_input = [987654321111111, 811111111111119, 234234234234278, 818181911112111]
    assert solve(test_input) == 3121910778619


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        banks = fp.readlines()
        print(f"Total banks {len(banks)}")
        joltage = solve(banks)
        print(f"total joltage is {joltage}")
