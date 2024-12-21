def solve_part1(input_data: str) -> int:
    available_patterns, designs = parse_input(input_data)
    return sum(is_design_possible(design, set(available_patterns)) for design in designs)


def solve_part2(input_data: str) -> int:
    available_patterns, designs = parse_input(input_data)
    return sum(get_number_of_arrangements(design, set(available_patterns)) for design in designs)


def parse_input(input_data: str) -> tuple[list[str], list[str]]:
    input_data = input_data.strip().split("\n\n")
    available_patterns = input_data[0].split(", ")
    designs = input_data[1].split("\n")
    return available_patterns, designs


def is_design_possible(design: str, available_patterns: set[str]) -> bool:
    if design in design_mem:
        return design_mem[design]
    if design in available_patterns:
        design_mem[design] = True
        return True
    for pattern in available_patterns:
        if design.startswith(pattern):
            if is_design_possible(design[len(pattern):], available_patterns):
                design_mem[design] = True
                return True
    design_mem[design] = False
    return False


design_mem = dict()


def get_number_of_arrangements(design: str, available_patterns: set[str]) -> int:
    if design in n_arrangements_mem:
        return n_arrangements_mem[design]
    total = 0
    if design in available_patterns:
        total += 1
    for pattern in available_patterns:
        if design.startswith(pattern):
            total += get_number_of_arrangements(design[len(pattern):], available_patterns)
    n_arrangements_mem[design] = total
    return total


n_arrangements_mem = dict()
