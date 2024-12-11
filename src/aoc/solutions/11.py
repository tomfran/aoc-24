from aoc.utilities.fetch import get_input
from aoc.utilities.decorators import solution
from functools import cache


@solution
def solve_all(nums):
    print(sum(map(lambda x: solve(x, 25), nums)))
    print(sum(map(lambda x: solve(x, 75), nums)))


@cache
def solve(n, left):
    if left == 0:
        return 1

    if n == 0:
        return solve(1, left - 1)

    if len(str(n)) % 2 == 0:
        s = str(n)
        first = solve(int(s[: len(s) // 2]), left - 1)
        second = solve(int(s[len(s) // 2 :]), left - 1)
        return first + second

    return solve(n * 2024, left - 1)


nums = list(map(int, get_input(11).split()))
solve_all(nums)
