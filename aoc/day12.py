def solve_part1(input_data: str) -> int:
    plots = input_data.splitlines()
    regions = get_regions(plots)
    region_areas_and_perimeters = get_region_areas_and_perimeters(regions)
    return sum([area * perimeter for area, perimeter in region_areas_and_perimeters.values()])


def solve_part2(input_data: str) -> int:
    plots = input_data.splitlines()
    regions = get_regions(plots)
    region_areas_and_sides = get_region_areas_and_sides(regions)
    return sum([area * perimeter for area, perimeter in region_areas_and_sides.values()])


def get_regions(plots: list[str]) -> list[list[int]]:
    regions = [[0 for _ in range(len(plots[0]))] for _ in range(len(plots))]
    region = 1

    def set_region(x: int, y: int, region_label: int) -> None:
        regions[x][y] = region_label
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(plots) and 0 <= new_y < len(plots[0]):
                if plots[new_x][new_y] == plots[x][y] and regions[new_x][new_y] == 0:
                    set_region(new_x, new_y, region_label)

    for i in range(len(plots)):
        for j in range(len(plots[0])):
            if regions[i][j] == 0:
                set_region(i, j, region)
                region += 1

    return regions


def get_region_areas_and_perimeters(regions: list[list[int]]) -> dict[int, tuple[int, int]]:
    region_areas = {}
    region_perimeters = {}

    for i in range(len(regions)):
        for j in range(len(regions[0])):
            region_label = regions[i][j]
            if region_label not in region_areas:
                region_areas[region_label] = 0
                region_perimeters[region_label] = 0

            region_areas[region_label] += 1
            region_perimeters[region_label] += sum([i == 0, j == 0, i == len(regions) - 1, j == len(regions[0]) - 1])
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < len(regions) and 0 <= new_y < len(regions[0]):
                    if regions[new_x][new_y] != region_label:
                        region_perimeters[region_label] += 1

    return {k: (region_areas[k], region_perimeters[k]) for k in region_areas}


def get_region_areas_and_sides(regions: list[list[int]]) -> dict[int, tuple[int, int]]:
    region_areas = {}
    region_sides = {}

    for i in range(len(regions)):
        for j in range(len(regions[0])):
            region_label = regions[i][j]
            if region_label not in region_areas:
                region_areas[region_label] = 0
                region_sides[region_label] = 0

            region_areas[region_label] += 1
            for dx, dy in [(a, b) for a in (-1, 1) for b in (-1, 1)]:
                if i + dx in (-1, len(regions)) or regions[i + dx][j] != region_label:
                    if j + dy in (-1, len(regions[0])) or regions[i][j + dy] != region_label:
                        region_sides[region_label] += 1
                else:
                    if j + dy not in (-1, len(regions[0])) and regions[i][j + dy] == region_label:
                        if regions[i + dx][j + dy] != region_label:
                            region_sides[region_label] += 1

    return {k: (region_areas[k], region_sides[k]) for k in region_areas}
