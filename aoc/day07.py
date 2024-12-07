def solve_part1(input_data: str) -> int:
    input_data = parse_input(input_data)
    result = sum([value for value, numbers in input_data if is_equation_possible(value, numbers, "+*")])
    return result


def solve_part2(input_data: str) -> int:
    input_data = parse_input(input_data)
    result = sum([value for value, numbers in input_data if is_equation_possible(value, numbers, "+*|")])
    return result


def parse_input(input_data: str) -> list[tuple[int, list[int]]]:
    lines = [line.split(":", maxsplit=2) for line in input_data.splitlines() if line]
    return [(int(line[0].strip()), [int(n) for n in line[1].split()]) for line in lines]


def is_equation_possible(value: int, numbers: list[int], operators: str) -> bool:
    if len(numbers) == 1:
        return numbers[0] == value
    if numbers[0] > value:
        return False
    else:
        results = []
        if '+' in operators:
            numbers_sum = [numbers[0] + numbers[1]] + numbers[2:]
            results.append(is_equation_possible(value, numbers_sum, operators))
        if '*' in operators:
            numbers_product = [numbers[0] * numbers[1]] + numbers[2:]
            results.append(is_equation_possible(value, numbers_product, operators))
        if '|' in operators:
            numbers_concatenation = [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:]
            results.append(is_equation_possible(value, numbers_concatenation, operators))
        return any(results)
