from aoc.day18 import solve_part1, solve_part2

input_data = """\
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def test_solve_part1():
    assert solve_part1(input_data, 12, 6) == 22


def test_solve_part2():
    assert solve_part2(input_data, 6) == "6,1"
