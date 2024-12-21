def solve_part1(input_data: str, min_save: int = 100) -> int:
    map_ = input_data.splitlines()
    start = find_in_map(map_, "S")
    end = find_in_map(map_, "E")
    distances = get_distances(map_, start, end)
    cheats = dict()
    for position in distances:
        cheats.update(get_cheats_at_position(map_, position, distances, 2))
    return sum(value >= min_save for value in cheats.values())


def solve_part2(input_data: str, min_save: int = 100) -> int:
    map_ = input_data.splitlines()
    start = find_in_map(map_, "S")
    end = find_in_map(map_, "E")
    distances = get_distances(map_, start, end)
    cheats = dict()
    for position in distances:
        cheats.update(get_cheats_at_position(map_, position, distances, 20))
    return sum(value >= min_save for value in cheats.values())


def find_in_map(map_: list[str], symbol: str) -> tuple[int, int]:
    for x, row in enumerate(map_):
        for y, cell in enumerate(row):
            if cell == symbol:
                return x, y


def get_distances(map_: list[str], start: tuple[int, int], end: tuple[int, int]) -> dict[tuple[int, int], int]:
    current = start
    distance = 0
    distances = dict()

    while current != end:
        distances[current] = distance
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = current[0] + x, current[1] + y
            if map_[neighbor[0]][neighbor[1]] != '#' and neighbor not in distances:
                current = neighbor
                break
        distance += 1

    distances[end] = distance

    return distances


def get_cheats_at_position(map_: list[str], position: tuple[int, int], distances: dict[tuple[int, int], int],
                           max_skip_distance: int) -> dict[tuple[tuple[int, int], tuple[int, int]], int]:
    cheat_results = dict()

    for x in range(max(0, position[0] - max_skip_distance), min(len(map_), position[0] + max_skip_distance + 1)):
        for y in range(max(0, position[1] - (max_skip_distance - abs(position[0] - x))),
                       min(len(map_[0]), position[1] + (max_skip_distance - abs(position[0] - x)) + 1)):
            if map_[x][y] != '#':
                saving = distances[x, y] - distances[position] - abs(x - position[0]) - abs(y - position[1])
                if saving > 0:
                    cheat_results[position, (x, y)] = saving

    return cheat_results
