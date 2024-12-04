import re


def solve_part1(input_data: str) -> int:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, input_data)
    result = 0
    for match in matches:
        numbers = re.findall(r"\d{1,3}", match)
        result += int(numbers[0]) * int(numbers[1])
    return result


def solve_part2(input_data: str) -> int:
    # first attempt - for some reason it doesn't work
    # input_data = input_data.split("don't()")
    # enabled = [input_data[0]]
    # for part in input_data[1:]:
    #     if "do()" in part:
    #         enabled.append(part.split("do()", 2)[1])
    # result = sum(solve_part1(part) for part in enabled)
    # return result

    # second attempt - works
    enabled = True
    result = 0
    for i, char in enumerate(input_data):
        if input_data[i:i+4] == "do()":
            enabled = True
        if input_data[i:i+7] == "don't()":
            enabled = False
        if enabled and input_data[i:i+4] == "mul(":
            end = input_data.find(")", i+7, i+12)
            if end == -1:
                continue
            numbers = input_data[i+4:end].split(",")
            if len(numbers) == 2 and all([n.isdigit() for n in numbers]):
                result += int(numbers[0]) * int(numbers[1])
    return result
