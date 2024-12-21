from aoc.day20 import solve_part1, solve_part2

input_data = """\
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def test_solve_part1():
    assert solve_part1(input_data, 0) == 44


def test_solve_part2():
    assert solve_part2(input_data, 50) == 285
