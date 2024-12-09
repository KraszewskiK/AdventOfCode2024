from aoc.day09 import solve_part1, solve_part2

input_data = """\
2333133121414131402"""


def test_solve_part1():
    assert solve_part1(input_data) == 1928


def test_solve_part2():
    assert solve_part2(input_data) == 2858
