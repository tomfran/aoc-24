from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution


def pad(matrix):
    m = len(matrix[0]) + 2

    res = [["."] * m]
    for row in matrix:
        res.append(["."] + row + ["."])
    res.append(["."] * m)

    return res


@solution
def solve_all(matrix):
    visited = set()

    ans1, ans2 = 0, 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if (i, j) in visited:
                continue

            corners = set()
            area, perimeter = dfs(i, j, matrix, visited, corners)
            ans1 += area * perimeter
            ans2 += area * (len(corners) + 1)

    print(f"{ans1}\n{ans2}")


def dfs(i, j, matrix, visited, corners):
    visited.add((i, j))

    a = 1
    p = perimeter(i, j, matrix)
    corners |= find_corners(i, j, matrix)

    for ai, aj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if matrix[i][j] == matrix[ai][aj] and (ai, aj) not in visited:
            a1, p1 = dfs(ai, aj, matrix, visited, corners)
            a += a1
            p += p1

    matrix[i][j] = "."

    return a, p


def perimeter(i, j, matrix):
    return sum(
        int(matrix[ai][aj] != matrix[i][j])
        for ai, aj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    )


def find_corners(i, j, matrix):
    return set()


data = get_input(12)
data = """AAAA
BBCD
BBCC
EEEC
"""

matrix = pad(list(map(list, data.splitlines())))
solve_all(matrix)
