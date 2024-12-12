def solve_part1(input_data: str) -> int:
    stones = [int(stone) for stone in input_data.split()]
    return count_stones(stones, 25)


def solve_part2(input_data: str) -> int:
    stones = [int(stone) for stone in input_data.split()]
    return count_stones(stones, 75)


def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    stone = str(stone)
    if len(stone) % 2 == 0:
        return [int(stone[:len(stone) // 2]), int(stone[len(stone) // 2:])]
    return [int(stone) * 2024]


memoize = {}


def count_stones(stones: list[int], blinks: int) -> int:
    if blinks == 0:
        return len(stones)
    else:
        result = 0
        for stone in stones:
            if (stone, blinks - 1) not in memoize:
                memoize[(stone, blinks - 1)] = count_stones(blink(stone), blinks - 1)
            result += memoize[(stone, blinks - 1)]
        return result
