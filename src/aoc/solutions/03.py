from aoc.utilities.fetch import get_input
import re


def check_len(a, b):
    return (1 <= len(a) <= 3) and (1 <= len(b) <= 3)


def solve_first(data):
    pattern = r"mul\((\d+),\s*(\d+)\)"

    ans = 0
    for mul in re.findall(pattern, data):
        a, b = mul
        if not check_len(a, b):
            continue
        ans += int(a) * int(b)

    print(ans)


def solve_second(data):
    pattern = r"(mul|do|don\'t)\((\d+,\d+|)\)"

    ans = 0
    enabled = True
    for match in re.findall(pattern, data):
        op, args = match

        if op != "mul":
            enabled = op == "do"
            continue

        a, b = args.split(",")
        if not enabled or not check_len(a, b):
            continue

        ans += int(a) * int(b)

    print(ans)


data = get_input(3)

solve_first(data)
solve_second(data)
