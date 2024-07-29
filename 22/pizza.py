# https://www.acmicpc.net/problem/14607

from sys import stdin
import math
from functools import lru_cache


def main():
    N = int(stdin.readline().strip())
    print(split(N))


@lru_cache(maxsize=None)
def split(n: int) -> int:
    if n == 1:
        return 0

    a, b = math.ceil(n / 2), math.floor(n / 2)
    return a * b + split(a) + split(b)


if __name__ == "__main__":
    main()
