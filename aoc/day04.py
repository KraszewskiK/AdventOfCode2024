def solve_part1(input_data: str) -> int:
    input_data = input_data.splitlines()
    word_count = 0

    for i, line in enumerate(input_data):
        for j, char in enumerate(line):
            if char == 'X':
                up = i >= 3
                down = i <= len(input_data) - 4
                left = j >= 3
                right = j <= len(line) - 4
                if up:
                    if input_data[i - 1][j] == 'M' and input_data[i - 2][j] == 'A' and input_data[i - 3][j] == 'S':
                        word_count += 1
                    if left:
                        if input_data[i - 1][j - 1] == 'M' and input_data[i - 2][j - 2] == 'A' and input_data[i - 3][j - 3] == 'S':
                            word_count += 1
                    if right:
                        if input_data[i - 1][j + 1] == 'M' and input_data[i - 2][j + 2] == 'A' and input_data[i - 3][j + 3] == 'S':
                            word_count += 1
                if down:
                    if input_data[i + 1][j] == 'M' and input_data[i + 2][j] == 'A' and input_data[i + 3][j] == 'S':
                        word_count += 1
                    if left:
                        if input_data[i + 1][j - 1] == 'M' and input_data[i + 2][j - 2] == 'A' and input_data[i + 3][j - 3] == 'S':
                            word_count += 1
                    if right:
                        if input_data[i + 1][j + 1] == 'M' and input_data[i + 2][j + 2] == 'A' and input_data[i + 3][j + 3] == 'S':
                            word_count += 1
                if left:
                    if input_data[i][j - 1] == 'M' and input_data[i][j - 2] == 'A' and input_data[i][j - 3] == 'S':
                        word_count += 1
                if right:
                    if input_data[i][j + 1] == 'M' and input_data[i][j + 2] == 'A' and input_data[i][j + 3] == 'S':
                        word_count += 1

    return word_count


def solve_part2(input_data: str) -> int:
    input_data = input_data.splitlines()
    x_mas_count = 0

    for i, line in enumerate(input_data):
        for j, char in enumerate(line):
            if char == "A" and 1 <= i <= len(input_data) - 2 and 1 <= j <= len(line) - 2:
                diag1 = input_data[i - 1][j - 1] + input_data[i][j] + input_data[i + 1][j + 1]
                diag2 = input_data[i - 1][j + 1] + input_data[i][j] + input_data[i + 1][j - 1]
                if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                    x_mas_count += 1

    return x_mas_count
