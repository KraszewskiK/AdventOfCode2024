import importlib
from aoc import read_input

def run_day(day):
    module = importlib.import_module(f"aoc.day{day:02}")
    input_data = read_input(day)
    print(f"Part 1: {module.solve_part1(input_data)}")
    print(f"Part 2: {module.solve_part2(input_data)}")

if __name__ == "__main__":
    import sys

    run_day(int(sys.argv[1]))
