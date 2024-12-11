from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution
from collections import Counter


@solution
def solve_first(input):
    print(Counter(map(check, input)).get(True, 0))


@solution
def solve_second(input):
    def brute_check(line):
        n = len(line)
        candidates = [list(line) for _ in range(n)]

        for can, i in zip(candidates, range(n)):
            can.pop(i)

        return any(map(check, candidates))

    print(Counter(map(brute_check, input)).get(True, 0))


def check(line):
    def f(line):
        for i in range(1, len(line)):
            if not (1 <= (line[i] - line[i - 1]) <= 3):
                return False
        return True

    def g(line):
        for i in range(1, len(line)):
            if not (1 <= (line[i - 1] - line[i]) <= 3):
                return False
        return True

    return f(line) or g(line)


data = [list(map(int, line.split())) for line in get_input(2).splitlines()]

solve_first(data)
solve_second(data)
