def solve_part1(input_data: str) -> int:
    patrol_map, x, y = get_map_and_initial_position(input_data)
    face = -1, 0
    visited = 1

    if x == -1 or y == -1:
        raise ValueError("No starting position found")

    while not (x in (0, len(patrol_map[0]) - 1) or y in (0, len(patrol_map) - 1)):
        next_x, next_y = x + face[0], y + face[1]
        if patrol_map[next_x][next_y] == '#':
            face = face[1], -face[0]
            continue
        elif patrol_map[next_x][next_y] == '.':
            visited += 1
        patrol_map[x] = patrol_map[x][:y] + 'X' + patrol_map[x][y + 1:]
        x, y = next_x, next_y

    return visited


def solve_part2(input_data: str) -> int:
    patrol_map, x, y = get_map_and_initial_position(input_data)
    face = -1, 0
    positions = 0
    visited = dict()

    def turn_face(_face: tuple[int, int]) -> tuple[int, int]:
        return _face[1], -_face[0]

    def make_step(_x: int, _y: int, _face: tuple[int, int], _map: list[str]) -> tuple[int, int, tuple[int, int]]:
        if _map[_x + _face[0]][_y + _face[1]] == '#':
            return _x, _y, turn_face(_face)
        return _x + _face[0], _y + _face[1], _face

    while not (x in (0, len(patrol_map[0]) - 1) or y in (0, len(patrol_map) - 1)):
        if (x, y) not in visited:
            visited[(x, y)] = set()
        visited[(x, y)].add(face)
        patrol_map[x] = patrol_map[x][:y] + 'X' + patrol_map[x][y + 1:]

        next_x, next_y = x + face[0], y + face[1]

        if patrol_map[next_x][next_y] not in ('#', 'O', 'X'):
            x_i, y_i = x, y
            f = turn_face(face)
            m = patrol_map.copy()
            m[next_x] = m[next_x][:next_y] + '#' + m[next_x][next_y + 1:]
            v = dict()
            while not (x_i in (0, len(patrol_map[0]) - 1) or y_i in (0, len(patrol_map) - 1)):
                if f in visited.get((x_i, y_i), set()).union(v.get((x_i, y_i), set())):
                    positions += 1
                    # patrol_map[next_x] = patrol_map[next_x][:next_y] + 'O' + patrol_map[next_x][next_y + 1:]
                    break
                if (x_i, y_i) not in v:
                    v[(x_i, y_i)] = set()
                v[(x_i, y_i)].add(f)
                x_i, y_i, f = make_step(x_i, y_i, f, m)

        x, y, face = make_step(x, y, face, patrol_map)

    return positions


def get_map_and_initial_position(input_data: str) -> tuple[list[str], int, int]:
    patrol_map = [line for line in input_data.splitlines() if line.strip()]
    x, y = -1, -1

    for i, line in enumerate(patrol_map):
        if '^' in line:
            x = i
            y = line.index('^')
            break

    if x == -1 or y == -1:
        raise ValueError("No starting position found")

    return patrol_map, x, y