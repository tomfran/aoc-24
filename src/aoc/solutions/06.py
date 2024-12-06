from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution


DIRECTION_DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
OBSTACLE = "#"
FREE = "."
START = "^"


def parse(data):
    matrix = list(map(list, data.splitlines()))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == START:
                matrix[i][j] = FREE
                return (i, j), matrix

    return None


def inside(i, j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def obstacle(i, j, matrix):
    return matrix[i][j] == OBSTACLE


@solution
def solve_first(si, sj, matrix):
    delta_idx = 0

    ci, cj = si, sj
    visited = set([(ci, cj)])

    while True:
        di, dj = DIRECTION_DELTAS[delta_idx]
        ni, nj = ci + di, cj + dj

        if not inside(ni, nj, matrix):
            break

        if obstacle(ni, nj, matrix):
            delta_idx = (delta_idx + 1) % len(DIRECTION_DELTAS)
            continue

        ci, cj = ni, nj
        visited.add((ci, cj))

    print(len(visited))
    return visited


def check_loop(si, sj, matrix):
    delta_idx = 0

    ci, cj = si, sj
    visited = set([(ci, cj, delta_idx)])

    while True:
        di, dj = DIRECTION_DELTAS[delta_idx]
        ni, nj = ci + di, cj + dj

        if not inside(ni, nj, matrix):
            break

        if obstacle(ni, nj, matrix):
            delta_idx = (delta_idx + 1) % len(DIRECTION_DELTAS)
            continue

        ci, cj = ni, nj

        if (ci, cj, delta_idx) in visited:
            return 1
        visited.add((ci, cj, delta_idx))

    return 0


@solution
def solve_second(si, sj, matrix, visited):
    ans = 0

    for i, j in visited:
        matrix[i][j] = OBSTACLE
        ans += check_loop(si, sj, matrix)
        matrix[i][j] = FREE

    print(ans)


(si, sj), matrix = parse(get_input(6))

visited = solve_first(si, sj, matrix)
solve_second(si, sj, matrix, visited)
