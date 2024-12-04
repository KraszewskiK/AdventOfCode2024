from aoc.day02 import solve_part1, solve_part2

input_data = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_solve_part1():
    assert solve_part1(input_data) == 2


def test_solve_part2():
    assert solve_part2(input_data) == 4
