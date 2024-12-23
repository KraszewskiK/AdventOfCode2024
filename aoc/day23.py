from itertools import combinations


def solve_part1(input_data: str) -> int:
    connections = get_connections(input_data)
    groups = set()

    for computer in connections:
        if computer.startswith("t"):
            for computer2 in connections[computer]:
                for computer3 in connections[computer].intersection(connections[computer2]):
                    groups.add(frozenset([computer, computer2, computer3]))

    return len(groups)


def solve_part2(input_data: str) -> str:
    connections = get_connections(input_data)
    cliques = []
    l = 0
    r = len(connections)

    while l < r:
        m = (l + r) // 2
        clique = find_clique(connections, m)
        if clique:
            l = m + 1
            cliques.append(clique)
        else:
            r = m

    return ",".join(sorted(cliques[-1]))


def get_connections(data: str) -> dict[str, set[str]]:
    connections = dict()

    for line in data.splitlines():
        a, b = line.split("-")
        if a not in connections:
            connections[a] = set()
        if b not in connections:
            connections[b] = set()
        connections[a].add(b)
        connections[b].add(a)

    return connections


def is_clique(connections: dict[str, set[str]], clique: set[str]) -> bool:
    for computer in clique:
        if not connections[computer].issuperset(clique.difference({computer})):
            return False
    return True


def find_clique(connections: dict[str, set[str]], size: int) -> set[str]:
    while any(len(connections[computer]) < size - 1 for computer in connections):
        connections = {computer: connections[computer] for computer in connections if
                       len(connections[computer]) >= size - 1}
        connections = {computer: set(comp for comp in connections[computer] if comp in connections) for computer in
                       connections}
    potential_members = [computer for computer in connections]

    if len(potential_members) >= size:
        for computer in potential_members:
            for clique in combinations(connections[computer], size - 1):
                if is_clique(connections, set(clique)):
                    return set(clique).union({computer})

    return set()
