from aoc.day01 import solve_part1, solve_part2

input_data = """\
3   4
4   3
2   5
1   3
3   9
3   3"""


def test_solve_part1():
    assert solve_part1(input_data) == 11


def test_solve_part2():
    assert solve_part2(input_data) == 31
