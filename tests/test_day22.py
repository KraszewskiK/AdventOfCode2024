import textwrap

from aoc.day22 import solve_part1, solve_part2


def test_solve_part1():
    input_data = textwrap.dedent("""\
        1
        10
        100
        2024""")
    assert solve_part1(input_data) == 37327623


def test_solve_part2():
    input_data = textwrap.dedent(
        """\
        1
        2
        3
        2024""")
    assert solve_part2(input_data) == 23
