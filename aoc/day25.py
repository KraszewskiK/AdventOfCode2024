def solve_part1(input_data: str) -> int:
    locks, keys = parse_input(input_data)
    height = len(input_data.split("\n\n")[0].splitlines()) - 2
    result = 0

    for lock in locks:
        for key in keys:
            if all([key[i] + lock[i] <= height for i in range(len(key))]):
                result += 1

    return result


def parse_input(data: str) -> tuple:
    data = data.split("\n\n")
    locks, keys = set(), set()

    for schematic in data:
        schematic = schematic.splitlines()
        pins = [0] * len(schematic[0])
        for row in schematic[1:-1]:
            for i, position in enumerate(row):
                if position == "#":
                    pins[i] += 1
        pins = tuple(pins)
        if schematic[0] == "#" * len(schematic[0]):
            locks.add(pins)
        else:
            keys.add(pins)

    return locks, keys
