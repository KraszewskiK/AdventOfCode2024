def solve_part1(input_data: str) -> int:
    antennas = [coors for _, coors in get_antennas(input_data).items() if len(coors) > 1]
    antinodes = set()

    for antenna_coors in antennas:
        antinodes.update(set(get_antinodes(antenna_coors, len(input_data.splitlines()), len(input_data.splitlines()[0]))))

    return len(antinodes)


def solve_part2(input_data: str) -> int:
    antennas = [coors for _, coors in get_antennas(input_data).items() if len(coors) > 1]
    antinodes = set()

    for antenna_coors in antennas:
        antinodes.update(set(get_antinodes(antenna_coors,
                                           len(input_data.splitlines()),
                                           len(input_data.splitlines()[0]),
                                           use_resonant_harmonics=True)))

    return len(antinodes)


def get_antennas(input_data: str) -> dict[str, list[tuple[int, int]]]:
    antennas = {}
    for i, line in enumerate(input_data.splitlines()):
        for j, char in enumerate(line):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((i, j))
    return antennas


def get_antinodes(antennas: list[tuple[int, int]], lim_i: int, lim_j: int, use_resonant_harmonics: bool = False) -> list[tuple[int, int]]:
    antinodes = []

    for i, antenna1 in enumerate(antennas[:-1]):
        for antenna2 in antennas[i+1:]:
            antinodes.extend(
                get_2_antinodes_for_2_antennas(antenna1, antenna2) if not use_resonant_harmonics
                else get_all_antinodes_for_2_antennas(antenna1, antenna2, lim_i, lim_j))

    antinodes = [(i, j) for i, j in antinodes if 0 <= i < lim_i and 0 <= j < lim_j]

    return antinodes


def get_2_antinodes_for_2_antennas(antenna1: tuple[int, int], antenna2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    antinode1 = antenna1[0] + (antenna1[0] - antenna2[0]), antenna1[1] + (antenna1[1] - antenna2[1])
    antinode2 = antenna2[0] + (antenna2[0] - antenna1[0]), antenna2[1] + (antenna2[1] - antenna1[1])
    return antinode1, antinode2


def get_all_antinodes_for_2_antennas(antenna1: tuple[int, int], antenna2: tuple[int, int], lim_i: int, lim_j: int) -> list[tuple[int, int]]:
    delta = (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])
    antinodes = []

    gcd = 1
    for i in range(2, min(abs(delta[0]), abs(delta[1])) + 1):
        if delta[0] % i == 0 and delta[1] % i == 0:
            gcd = i

    delta = (delta[0] // gcd, delta[1] // gcd)

    i, j = antenna1
    while 0 <= i < lim_i and 0 <= j < lim_j:
        antinodes.append((i, j))
        i += delta[0]
        j += delta[1]

    i, j = antenna1[0] - delta[0], antenna1[1] - delta[1]
    while 0 <= i < lim_i and 0 <= j < lim_j:
        antinodes.append((i, j))
        i -= delta[0]
        j -= delta[1]

    return antinodes
