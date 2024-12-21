from aoc.day19 import solve_part1, solve_part2

input_data = """\
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def test_solve_part1():
    assert solve_part1(input_data) == 6


def test_solve_part2():
    assert solve_part2(input_data) == 16
