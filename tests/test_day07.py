from aoc.day07 import solve_part1, solve_part2

input_data = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def test_solve_part1():
    assert solve_part1(input_data) == 3749


def test_solve_part2():
    assert solve_part2(input_data) == 11387
