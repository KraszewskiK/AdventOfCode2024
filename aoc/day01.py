def solve_part1(input_data: str) -> int:
    list1, list2 = get_lists(input_data)
    list1.sort()
    list2.sort()
    distances = [abs(list1[i] - list2[i]) for i in range(len(list1))]
    return sum(distances)


def solve_part2(input_data: str) -> int:
    list1, list2 = get_lists(input_data)
    similarity = [x * sum([x == y for y in list2]) for x in list1]
    return sum(similarity)


def get_lists(data: str) -> tuple[list[int], list[int]]:
    data = data.split("\n")
    data = [x.split() for x in data if x]
    data = [[int(x) for x in y] for y in data]
    list1 = [x[0] for x in data]
    list2 = [x[1] for x in data]
    return list1, list2
