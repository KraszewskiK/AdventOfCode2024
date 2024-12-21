def solve_part1(input_data: str, n_bytes: int = 1024, size: int = 70) -> int:
    size += 3
    falling_bytes = parse_input(input_data)
    map_ = generate_map(size)
    map_ = add_fallen_bytes(map_, falling_bytes[:n_bytes])
    distances, _ = find_smallest_cost(map_, (1, 1))
    end = (size - 2, size - 2)
    return distances[end]


def solve_part2(input_data: str, size: int = 70) -> str:
    size += 3
    falling_bytes = parse_input(input_data)
    map_ = generate_map(size)
    l = 0
    r = len(falling_bytes)
    end = (size - 2, size - 2)
    while l < r:
        m = (l + r) // 2
        map_ = add_fallen_bytes(map_, falling_bytes[:m])
        distances, _ = find_smallest_cost(map_, (1, 1))
        if distances[end] == float("inf"):
            r = m
            map_ = generate_map(size)
        else:
            l = m + 1
    return f"{falling_bytes[l - 1][0]},{falling_bytes[l - 1][1]}"


def parse_input(input_data: str) -> list[tuple[int, int]]:
    return [(int(line.split(",")[0]), int(line.split(",")[1])) for line in input_data.splitlines() if line]


def generate_map(size: int) -> list[list[str]]:
    map_ = [['.' for _ in range(size)] for _ in range(size)]
    for x in range(size):
        map_[x][0] = "#"
        map_[x][size - 1] = "#"
        map_[0][x] = "#"
        map_[size - 1][x] = "#"
    return map_


def add_fallen_bytes(map_: list[list[str]], falling_bytes: list[tuple[int, int]]) -> list[list[str]]:
    for x, y in falling_bytes:
        map_[y + 1][x + 1] = "#"
    return map_


def find_smallest_cost(map_: list[list[str]], start: tuple[int, int]) -> tuple[
    dict[tuple[int, int], int], dict[tuple[int, int], tuple[int, int]]]:
    unvisited = set()
    distances = dict()
    predecessors = dict()

    for x, row in enumerate(map_):
        for y, cell in enumerate(row):
            if cell == "#":
                continue
            unvisited.add((x, y))
            distances[(x, y)] = float("inf")
            predecessors[(x, y)] = None

    distances[start] = 0

    while unvisited and min([distances[x] for x in unvisited]) != float("inf"):
        current = min(unvisited, key=lambda x: distances[x])
        unvisited.remove(current)

        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = current[0] + x, current[1] + y
            if map_[neighbor[0]][neighbor[1]] == "#":
                continue
            tentative_distance = distances[current] + 1
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                predecessors[neighbor] = current

    return distances, predecessors
