from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution
from collections import defaultdict


def coefficient(x1, y1, x2, y2):
    dx, dy = x1 - x2, y1 - y2
    return float("inf") if dx == 0 else dy / dx


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def first_check(xr, yr, x1, y1, x2, y2):
    if coefficient(xr, yr, x1, y1) != coefficient(xr, yr, x2, y2):
        return False

    dist_a = distance(xr, yr, x1, y1)
    dist_b = distance(xr, yr, x2, y2)
    return dist_a == dist_b * 2 or dist_a * 2 == dist_b


def second_check(xr, yr, x1, y1, x2, y2):
    return coefficient(xr, yr, x1, y1) == coefficient(xr, yr, x2, y2)


def compute_antinodes(n, m, coordinates, valid_check):
    res = []
    c = len(coordinates)

    for i in range(c):
        for j in range(i + 1, c):
            point_a, point_b = coordinates[i], coordinates[j]

            res += [
                (x, y)
                for x in range(n)
                for y in range(m)
                if valid_check(x, y, *point_a, *point_b)
            ]

    return set(res)


@solution
def solve_all(data):
    d = defaultdict(list)
    n, m = len(data), len(data[0])

    for i in range(n):
        for j in range(m):
            if data[i][j] == ".":
                continue
            d[data[i][j]].append((i, j))

    ans1, ans2 = set(), set()

    for v in d.values():
        ans1 |= compute_antinodes(n, m, v, first_check)
        ans2 |= compute_antinodes(n, m, v, second_check) | set(v)

    print(f"{len(ans1)}\n{len(ans2)}")


data = list(map(list, get_input(8).splitlines()))
solve_all(data)
