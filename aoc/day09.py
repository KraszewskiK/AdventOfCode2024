def solve_part1(input_data: str) -> int:
    input_data = input_data.strip()
    checksum = 0
    block_position = 0
    left = 0
    right = len(input_data) - (2 if len(input_data) % 2 == 0 else 1)
    p_right = int(input_data[right])
    while left < right:
        n_left_blocks = int(input_data[left])
        if left % 2 == 0:
            for i in range(n_left_blocks):
                checksum += block_position * (left // 2)
                block_position += 1
        else:
            for i in range(n_left_blocks):
                if p_right == 0:
                    right -= 2
                    if left > right:
                        right = 0
                    p_right = int(input_data[right])
                checksum += block_position * (right // 2)
                block_position += 1
                p_right -= 1
            if right == 0:
                break
        left += 1
        if left == right:
            for i in range(p_right):
                checksum += block_position * (right // 2)
                block_position += 1
    return checksum


def solve_part2(input_data: str) -> int:
    blocks = diskmap2blocks(input_data.strip())
    blocks = move_files(blocks)
    return get_checksum(blocks)


def diskmap2blocks(diskmap: str) -> list[tuple[int|str, int]]:
    blocks = []
    for i, block in enumerate(diskmap):
        blocks.append((i//2 if i % 2 == 0 else '.', int(block)))
    return blocks


def move_files(blocks: list[tuple[int|str, int]]) -> list[tuple[int|str, int]]:
    for i, n in blocks[::-1]:
        if i == '.':
            continue
        for j in range(blocks.index((i, n))):
            if blocks[j][0] == '.' and blocks[j][1] >= n:
                blocks[j] = ('.', blocks[j][1] - n)
                blocks[blocks.index((i, n))] = ('.', n)
                blocks.insert(j, (i, n))
                break
    return blocks


def get_checksum(blocks: list[tuple[int|str, int]]) -> int:
    result = 0
    position = 0
    for i, n in blocks:
        if i != '.':
            result += i * sum([position + j for j in range(n)])
        position += n
    return result


def print_filesystem(blocks: list[tuple[int|str, int]]) -> None:
    print("".join([str(i)*n for i, n in blocks]))