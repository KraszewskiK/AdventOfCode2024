def solve_part1(input_data: str) -> int:
    machines = process_input(input_data)
    tokens = 0

    for button_a, button_b, prize in machines:
        tokens += find_min_tokens(button_a, button_b, prize)

    return tokens


def solve_part2(input_data: str) -> int:
    machines = process_input(input_data)
    tokens = 0

    for button_a, button_b, prize in machines:
        tokens += find_min_tokens(button_a, button_b,
                                  (prize[0] + 10000000000000, prize[1] + 10000000000000))

    return tokens


def process_input(input_data: str) -> list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    input_data = input_data.strip().split("\n\n")
    machines = []

    for machine in input_data:
        machine = machine.split("\n")
        machine = [line.split(" ") for line in machine]
        button_a = int(machine[0][2][2:-1]), int(machine[0][3][2:])
        button_b = int(machine[1][2][2:-1]), int(machine[1][3][2:])
        prize = int(machine[2][1][2:-1]), int(machine[2][2][2:])
        machines.append((button_a, button_b, prize))

    return machines


def find_min_tokens(button_a: tuple[int, int], button_b: tuple[int, int], prize: tuple[int, int]) -> int:
    det = (button_a[0] * button_b[1] - button_a[1] * button_b[0])
    if det == 0:
        return 0
    a = (button_b[1] * prize[0] - button_b[0] * prize[1]) / det
    b = (-button_a[1] * prize[0] + button_a[0] * prize[1]) / det

    if int(a) != a or int(b) != b or a < 0 or b < 0:
        return 0
    return int(3 * a + b)
