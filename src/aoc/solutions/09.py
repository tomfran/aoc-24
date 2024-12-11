from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution


@solution
def solve_first(cells):
    disk = []

    free = False
    i = 0
    for e in cells:
        value = -1 if free else i

        if value != -1:
            i += 1

        for _ in range(e):
            disk.append(value)

        free = not free

    i = 0
    j = len(disk) - 1

    while i < j:
        while disk[i] != -1:
            i += 1

        if i >= j:
            break

        disk[i], disk[j] = disk[j], disk[i]
        j -= 1

    print(compute_checksum(disk))


@solution
def solve_second(cells):
    disk = []

    free = False
    idx = 0

    for e in cells:
        disk.append((-1 if free else idx, e))
        idx = idx if free else idx + 1
        free = not free

    disk = disk[::-1]

    i = 0
    while i < len(disk):
        id_i, w_i = disk[i]

        if id_i == -1:
            i += 1
            continue

        for j in range(len(disk) - 1, i, -1):
            id_j, w_j = disk[j]

            if id_j != -1 or w_j < w_i:
                continue

            disk[i] = (-1, w_i)

            swapped = [(id_i, w_i)]
            if rem := w_j - w_i:
                swapped.insert(0, (-1, rem))

            disk = disk[:j] + swapped + disk[j + 1 :]
            break

        i += 1

    cells = []
    for idx, w in disk[::-1]:
        cells += [idx] * w

    print(compute_checksum(cells))


def compute_checksum(cells):
    ans = 0
    for i, e in enumerate(cells):
        if e == -1:
            continue
        ans += i * e

    return ans


data = get_input(9)
cells = list(map(int, list(data)))

solve_first(cells)
solve_second(cells)
