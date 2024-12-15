def solve_part1(input_data: str, width: int = 101, height: int = 103) -> int:
    seconds = 100
    robots = get_robots(input_data)
    robots = simulate(robots, seconds, height, width)
    quadrants = count_robots_in_quadrants(robots, height, width)
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def solve_part2(input_data: str) -> int:
    robots = get_robots(input_data)
    step = 0

    while not step > 10000:
        robot_map = [[0 for _ in range(101)] for _ in range(103)]
        for robot in robots:
            robot_map[robot[0][1]][robot[0][0]] += 1
        map_str = "\n".join("".join('#' if x > 0 else '.' for x in row) for row in robot_map)
        if '############' in map_str:
            print(map_str)
            return step
        robots = simulate(robots, 1, 103, 101)
        step += 1


def get_robots(input_data: str) -> list[list[tuple[int, int]]]:
    robots = input_data.strip().splitlines()
    robots = [robot.split(maxsplit=2) for robot in robots]
    robots = [[p.split(",", maxsplit=1), v.split(",", maxsplit=1)] for p, v in robots]
    robots = [[(int(p[0][2:]), int(p[1])), (int(v[0][2:]), int(v[1]))] for p, v in robots]
    return robots


def simulate(robots: list[list[tuple[int, int]]], steps: int, height: int, width: int) -> list[list[tuple[int, int]]]:
    for robot in robots:
        robot[0] = (
            (robot[0][0] + robot[1][0] * steps) % width,
            (robot[0][1] + robot[1][1] * steps) % height
        )
    return robots


def count_robots_in_quadrants(robots: list[list[tuple[int, int]]], height: int, width: int) -> list[int]:
    quadrants = [0, 0, 0, 0]
    width_half = (width - 1) / 2
    height_half = (height - 1) / 2

    for robot in robots:
        if robot[0][0] < width_half:
            if robot[0][1] < height_half:
                quadrants[0] += 1
            elif robot[0][1] > height_half:
                quadrants[2] += 1
        elif robot[0][0] > width_half:
            if robot[0][1] < height_half:
                quadrants[1] += 1
            elif robot[0][1] > height_half:
                quadrants[3] += 1
    return quadrants
