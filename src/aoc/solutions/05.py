from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution
from collections import defaultdict
from functools import cmp_to_key


def parse(data):
    edges = defaultdict(set)
    updates = []

    for line in data.splitlines():
        if "|" in line:
            a, b = map(int, line.split("|"))
            edges[a].add(b)
        elif line:
            updates.append(list(map(int, line.split(","))))

    return edges, updates


@solution
def solve_first(edges, updates):
    ans = sum(x for pages in updates if (x := check_valid(edges, pages)) != -1)
    print(ans)


@solution
def solve_second(edges, updates):
    def comparator(i, j):
        if j in edges[i]:
            return -1
        return 1

    ans = 0
    for pages in updates:
        if check_valid(edges, pages) != -1:
            continue

        key = cmp_to_key(comparator)
        pages.sort(key=key)

        ans += pages[len(pages) // 2]

    print(ans)


def check_valid(edges, pages):
    n = len(pages)

    for i in range(n):
        for j in range(i + 1, n):
            if pages[i] in edges[pages[j]]:
                return -1

    return pages[n // 2]


data = get_input(5)
edges, updates = parse(data)

solve_first(edges, updates)
solve_second(edges, updates)
