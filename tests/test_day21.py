from aoc.day21 import solve_part1

input_data = """\
029A
980A
179A
456A
379A"""


def test_solve_part1():
    assert solve_part1(input_data) == 126384
