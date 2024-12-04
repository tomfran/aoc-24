from aoc.utilities.fetch import get_input


FIRST_PATTERN = "XMAS"


def check_first_internal(i, j, di, dj, level):
    if not (0 <= i < len(data) and 0 <= j < len(data[0])):
        return 0

    if data[i][j] != FIRST_PATTERN[level]:
        return 0

    if level == 3:
        return 1

    return check_first_internal(i + di, j + dj, di, dj, level + 1)


def check_first(i, j, data):
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    return sum(map(lambda x: check_first_internal(i, j, x[0], x[1], 0), deltas))


def solve_first(data):
    n, m, ans = len(data), len(data[0]), 0

    for i in range(n):
        for j in range(m):
            ans += check_first(i, j, data)

    print(ans)


def check_second(i, j, data):
    deltas = [(1, 1), (-1, 1)]
    starts = [(i, j), (i + 2, j)]

    for (di, dj), (si, sj) in zip(deltas, starts):
        word = ""
        for x in range(3):
            word += data[si + di * x][sj + dj * x]

        if word not in ["MAS", "SAM"]:
            return 0

    return 1


def solve_second(data):
    n, m, ans = len(data), len(data[0]), 0

    for i in range(n - 2):
        for j in range(m - 2):
            ans += check_second(i, j, data)

    print(ans)


data = list(map(list, get_input(4).splitlines()))

solve_first(data)
solve_second(data)