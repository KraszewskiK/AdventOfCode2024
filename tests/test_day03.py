from aoc.day03 import solve_part1, solve_part2


def test_solve_part1():
    input_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert solve_part1(input_data) == 161


def test_solve_part2():
    input_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert solve_part2(input_data) == 48
