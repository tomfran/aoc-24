from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution


def compute_checksum(disk):
    ans = 0
    for i, e in enumerate(disk):
        if e == -1:
            break
        ans += i * e

    return ans


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


# TODO
def solve_second(cells):
    pass
    # disk = []
    # free = False

    # idx = 0
    # for e in cells:
    #     disk.append((e, -1 if free else idx))
    #     idx = idx if free else idx + 1
    #     free = not free

    # idx -= 1

    # def find_idx(i):
    #     for j, (_, k) in enumerate(disk):
    #         if k == i:
    #             return j

    # def find_candidate(max_i, need_w):
    #     for j, (w, k) in enumerate(disk[:max_i]):
    #         if w >= need_w:
    #             return j
    #     return -1

    # def place(i, j):

    # while idx >= 0:
    #     i = find_idx(idx)
    #     w, j = disk[i]
    #     candidate = find_candidate(i, w)
    #     if candidate != -1:
    #         place(i, candidate)

    #     idx -= 1


data = get_input(9)
data = "12345"
cells = list(map(int, list(data)))

solve_first(cells)
solve_second(cells)
