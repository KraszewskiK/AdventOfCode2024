def solution1(data):
    list1, list2 = get_lists(data)
    list1.sort()
    list2.sort()
    distances = [abs(list1[i] - list2[i]) for i in range(len(list1))]
    return sum(distances)


def solution2(data):
    list1, list2 = get_lists(data)
    similarity = [x * sum([x == y for y in list2]) for x in list1]
    return sum(similarity)


def get_lists(data):
    data = data.split("\n")
    data = [x.split() for x in data if x]
    data = [[int(x) for x in y] for y in data]
    list1 = [x[0] for x in data]
    list2 = [x[1] for x in data]
    return list1, list2


if __name__ == '__main__':
    import os

    example_file = "example.txt"
    input_file = "input.txt"
    files = [example_file, input_file]

    for file in files:
        if os.path.exists(file):
            with open(file, "r") as f:
                content = f.read()
                print(f"Solution of PART 1 for {file} is: {solution1(content)}.")
                print(f"Solution of PART 2 for {file} is: {solution2(content)}.")
