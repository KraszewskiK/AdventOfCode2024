def solve_part1(input_data: str) -> int:
    map_, directions = get_map_and_directions(input_data)
    robot_x, robot_y = find_initial_position(map_)

    for direction in directions:
        robot_x, robot_y, map_ = move_robot(map_, robot_x, robot_y, direction)

    result = 0
    for x, row in enumerate(map_):
        for y, cell in enumerate(row):
            if cell == "O":
                result += 100 * x + y
    return result


def solve_part2(input_data: str) -> int:
    map_, directions = get_map_and_directions(input_data)
    map_ = scale_map(map_)
    robot_x, robot_y = find_initial_position(map_)

    for direction in directions:
        robot_x, robot_y, map_ = move_robot(map_, robot_x, robot_y, direction, is_map_scaled=True)

    result = 0
    for x, row in enumerate(map_):
        for y, cell in enumerate(row):
            if cell == "[":
                result += 100 * x + y
    return result


def get_map_and_directions(input_data: str) -> tuple[list[str], str]:
    input_data = input_data.split("\n\n")
    map_ = input_data[0].strip().splitlines()
    directions = ''.join(input_data[1].strip().splitlines())
    return map_, directions


def find_initial_position(map_: list[str]) -> tuple[int, int]:
    robot_x, robot_y = -1, -1
    for x, row in enumerate(map_):
        for y, cell in enumerate(row):
            if cell == "@":
                robot_x, robot_y = x, y
                break
        if robot_x != -1:
            break
    return robot_x, robot_y


def move_robot(map_: list[str], robot_x: int, robot_y: int, direction: str, is_map_scaled: bool = False) -> tuple[
    int, int, list[str]]:
    direction = (1 if direction == "v" else (-1 if direction == "^" else 0),
                 1 if direction == ">" else (-1 if direction == "<" else 0))

    if (not is_map_scaled) or direction[0] == 0:
        next_x, next_y = robot_x + direction[0], robot_y + direction[1]

        while map_[next_x][next_y] not in ".#":
            next_x, next_y = next_x + direction[0], next_y + direction[1]

        if map_[next_x][next_y] == ".":
            while next_x != robot_x or next_y != robot_y:
                prev_x, prev_y = next_x - direction[0], next_y - direction[1]
                cur = map_[next_x][next_y]
                prev = map_[prev_x][prev_y]
                map_[next_x] = map_[next_x][:next_y] + prev + map_[next_x][next_y + 1:]
                map_[prev_x] = map_[prev_x][:prev_y] + cur + map_[prev_x][prev_y + 1:]
                next_x, next_y = prev_x, prev_y

            robot_x, robot_y = robot_x + direction[0], robot_y + direction[1]
    else:
        indices = [set()]
        indices[-1].add(robot_y)
        next_x = robot_x + direction[0]

        while all(map_[next_x][y] != "#" for y in indices[-1]) and any(map_[next_x][y] != "." for y in indices[-1]):
            new_indices = set()
            for y in indices[-1]:
                if map_[next_x][y] in "[]":
                    new_indices.add(y)
                    new_indices.add(y + (1 if map_[next_x][y] == "[" else -1))
            indices.append(new_indices)
            next_x += direction[0]

        if all(map_[next_x][y] == "." for y in indices[-1]):
            while next_x != robot_x:
                prev_x = next_x - direction[0]
                for y in indices[-1]:
                    cur = map_[next_x][y]
                    prev = map_[prev_x][y]
                    map_[next_x] = map_[next_x][:y] + prev + map_[next_x][y + 1:]
                    map_[prev_x] = map_[prev_x][:y] + cur + map_[prev_x][y + 1:]
                next_x = prev_x
                indices.pop()

            robot_x += direction[0]

    return robot_x, robot_y, map_


def scale_map(map_: list[str]) -> list[str]:
    new_map = []
    scale = 2
    for row in map_:
        new_map.append(row
                       .replace("#", "#" * scale)
                       .replace(".", "." * scale)
                       .replace("O", "[]")
                       .replace("@", "@.")
                       )
    return new_map
