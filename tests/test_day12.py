import textwrap

from aoc.day12 import solve_part1, solve_part2

input_data = """\
AAAA
BBCD
BBCC
EEEC"""

input_data2 = """\
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

input_data3 = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def test_solve_part1_1():
    assert solve_part1(input_data) == 140


def test_solve_part1_2():
    assert solve_part1(input_data2) == 772


def test_solve_part1_3():
    assert solve_part1(input_data3) == 1930


def test_solve_part2_1():
    assert solve_part2(input_data) == 80


def test_solve_part2_2():
    assert solve_part2(input_data2) == 436


def test_solve_part2_3():
    assert solve_part2(input_data3) == 1206


def test_solve_part2_4():
    input_data4 = textwrap.dedent("""\
        EEEEE
        EXXXX
        EEEEE
        EXXXX
        EEEEE""")
    assert solve_part2(input_data4) == 236


def test_solve_part2_5():
    input_data4 = textwrap.dedent("""\
        AAAAAA
        AAABBA
        AAABBA
        ABBAAA
        ABBAAA
        AAAAAA""")
    assert solve_part2(input_data4) == 368
