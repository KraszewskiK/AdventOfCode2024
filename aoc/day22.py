def solve_part1(input_data: str) -> int:
    initial_secret_numbers = [int(line) for line in input_data.splitlines() if line]
    result = 0

    for secret_number in initial_secret_numbers:
        for i in range(2000):
            secret_number = get_next_secret_number(secret_number)
        result += secret_number

    return result


def solve_part2(input_data: str) -> int:
    initial_secret_numbers = [int(line) for line in input_data.splitlines() if line]
    results = dict()

    for secret_number in initial_secret_numbers:
        changes_occurred = set()
        changes = [None]
        current = secret_number

        for _ in range(3):
            previous = current % 10
            current = get_next_secret_number(current)
            changes.append(current % 10 - previous)

        changes = tuple(changes)

        for _ in range(2000 - 3):
            previous = current % 10
            current = get_next_secret_number(current)
            changes = changes[1:] + (current % 10 - previous,)
            if changes not in changes_occurred:
                changes_occurred.add(changes)
                if changes not in results:
                    results[changes] = 0
                results[changes] += current % 10

    return max(results.values())


def mix(secret_number: int, number: int) -> int:
    return number ^ secret_number


def prune(secret_number: int) -> int:
    return secret_number % 16777216


def get_next_secret_number(secret_number: int) -> int:
    secret_number = prune(mix(secret_number, secret_number * 64))
    secret_number = prune(mix(secret_number, int(secret_number / 32)))
    secret_number = prune(mix(secret_number, secret_number * 2048))
    return secret_number
