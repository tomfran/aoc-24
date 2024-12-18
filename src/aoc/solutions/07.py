from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution


OPS = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "|": lambda a, b: int(str(a) + str(b)),
}


def parse(line):
    target, res = line.split(":")
    return int(target), list(map(int, res.split()))


@solution
def solve_all(parsed):
    ans1, ans2 = 0, 0

    for target, parts in parsed:
        ans1 += solve(target, parts, "*+")
        ans2 += solve(target, parts, "*+|")

    print(f"{ans1}\n{ans2}")


def solve(target, parts, operators):
    def rec(i, partial):
        if partial > target:
            return 0

        if i == len(parts):
            return target if partial == target else 0

        for op in operators:
            if res := rec(i + 1, OPS[op](partial, parts[i])):
                return res

        return 0

    return rec(1, parts[0])


parsed = list(map(parse, get_input(7).splitlines()))
solve_all(parsed)
