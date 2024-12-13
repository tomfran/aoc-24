from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution
import re


def parse(data):
    return list(map(parse_game, data.split("\n\n")))


def parse_game(s):
    pattern = r"[XY][+=](\d+),?\s?[XY][+=](\d+)"
    matches = re.findall(pattern, s)

    return [(int(x), int(y)) for x, y in matches]


@solution
def solve_all(games):
    ans1, ans2 = 0, 0

    for a, b, p in games:
        first, second = (
            solve(*a, *b, *p),
            solve(*a, *b, p[0] + 10000000000000, p[1] + 10000000000000),
        )

        ans1 += first if first != float("inf") else 0
        ans2 += second if second != float("inf") else 0

    print(f"{ans1}\n{ans2}")


def solve(ax, ay, bx, by, px, py):
    a_num = py * bx - px * by
    a_den = ay * bx - ax * by

    if a_num % a_den != 0:
        return float("inf")

    A = a_num / a_den

    b_num = px - ax * A
    b_den = bx

    if b_num % b_den != 0:
        return float("inf")

    B = b_num / b_den

    return int(3 * A + B)


data = get_input(13)

games = parse(data)
solve_all(games)
