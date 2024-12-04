from aoc.utilities.fetch import get_input
from collections import Counter


def split(input):
    first, second = [], []
    for line in input.splitlines():
        a, b = map(int, line.split())
        first.append(a)
        second.append(b)

    return first, second


def solve_first(first, second):
    ans = 0
    for a, b in zip(sorted(first), sorted(second)):
        ans += abs(a - b)

    print(ans)


def solve_second(first, second):
    c = Counter(second)

    ans = 0
    for e in first:
        ans += e * c.get(e, 0)

    print(ans)


first, second = split(get_input(1))

solve_first(first, second)
solve_second(first, second)
