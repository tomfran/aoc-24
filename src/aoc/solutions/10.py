from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution


@solution
def solve_all(matrix):
    n, m = len(matrix), len(matrix[0])

    ans1, ans2 = 0, 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                continue

            ans1 += len(dfs_first(i, j, matrix))
            ans2 += dfs_second(i, j, matrix)

    print(f"{ans1}\n{ans2}")


def dfs_first(i, j, matrix):
    if matrix[i][j] == 9:
        return set([(i, j)])

    ans = set()

    for ai, aj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if (
            0 <= ai < len(matrix)
            and 0 <= aj < len(matrix[0])
            and matrix[ai][aj] == matrix[i][j] + 1
        ):
            ans |= dfs_first(ai, aj, matrix)

    return ans


def dfs_second(i, j, matrix):
    if matrix[i][j] == 9:
        return 1

    ans = 0
    for ai, aj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if (
            0 <= ai < len(matrix)
            and 0 <= aj < len(matrix[0])
            and matrix[ai][aj] == matrix[i][j] + 1
        ):
            ans += dfs_second(ai, aj, matrix)

    return ans


matrix = [list(map(int, line)) for line in map(list, get_input(10).splitlines())]
solve_all(matrix)
