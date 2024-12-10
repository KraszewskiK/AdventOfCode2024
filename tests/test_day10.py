from aoc.day10 import solve_part1, solve_part2

input_data = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def test_solve_part1():
    assert solve_part1(input_data) == 36


def test_solve_part2():
    assert solve_part2(input_data) == 81
