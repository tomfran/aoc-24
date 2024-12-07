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


def solve(target, parts, operators):
    def rec(i, partial):
        if i == len(parts):
            return partial == target

        for op in operators:
            if rec(i + 1, OPS[op](partial, parts[i])):
                return True

        return False

    return rec(1, parts[0])


@solution
def solve_all(parsed):
    ans1, ans2 = 0, 0

    for target, parts in parsed:
        ans1 += target if solve(target, parts, "*+") else 0
        ans2 += target if solve(target, parts, "*+|") else 0

    print(f"{ans1}\n{ans2}")


parsed = list(map(parse, get_input(7).splitlines()))
solve_all(parsed)
