from aoc.day23 import solve_part1, solve_part2

input_data = """\
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def test_solve_part1():
    assert solve_part1(input_data) == 7


def test_solve_part2():
    assert solve_part2(input_data) == "co,de,ka,ta"
