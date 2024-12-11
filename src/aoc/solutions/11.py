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

    s = str(n)
    if len(s) % 2 == 0:
        first, second = int(s[: len(s) // 2]), int(s[len(s) // 2 :])
        return solve(first, left - 1) + solve(second, left - 1)

    return solve(n * 2024, left - 1)


nums = list(map(int, get_input(11).split()))
solve_all(nums)
