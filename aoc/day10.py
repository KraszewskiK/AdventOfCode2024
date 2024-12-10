def solve_part1(input_data: str) -> int:
    input_data = get_map(input_data)
    result = 0

    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if int(input_data[i][j]) == 0:
                peaks = find_peaks(input_data, (i, j))
                result += len(peaks)

    return result


def solve_part2(input_data: str) -> int:
    input_data = get_map(input_data)
    result = 0

    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if int(input_data[i][j]) == 0:
                result += find_trails(input_data, (i, j))

    return result


def get_map(data: str) -> list[str]:
    return [line for line in data.splitlines() if line]


def find_peaks(data: list[str], start: tuple[int, int]) -> set[tuple[int, int]]:
    if int(data[start[0]][start[1]]) == 9:
        return {(start[0], start[1])}

    peaks = set()

    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = start[0] + i, start[1] + j
        if 0 <= x < len(data) and 0 <= y < len(data[0]):
            if int(data[x][y]) == int(data[start[0]][start[1]]) + 1:
                reachable_peaks = find_peaks(data, (x, y))
                peaks.update(reachable_peaks)

    return peaks


def find_trails(data: list[str], start: tuple[int, int]) -> int:
    if int(data[start[0]][start[1]]) == 9:
        return 1

    trails = 0

    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = start[0] + i, start[1] + j
        if 0 <= x < len(data) and 0 <= y < len(data[0]):
            if int(data[x][y]) == int(data[start[0]][start[1]]) + 1:
                trails += find_trails(data, (x, y))

    return trails
