# https://www.acmicpc.net/problem/1002
# reference: https://acstory.tistory.com/236 (두 원의 위치관계)

from sys import stdin
import math


def main():
    T = int(stdin.readline())  # n of test cases
    for _ in range(T):
        inputs = tuple(map(int, stdin.readline().strip().split()))
        print(solve(inputs))


def solve(inputs: tuple[int, ...]) -> int:
    """두 원의 교점의 개수 구하기"""

    assert len(inputs) == 6
    x1, y1, r1, x2, y2, r2 = inputs

    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    sum = r1 + r2
    diff = abs(r1 - r2)

    if dist < diff:
        return 0  # 한 원이 다른 원 안에 있음
    elif dist == diff:
        if dist == 0:
            return -1  # 같은 원
        else:
            return 1  # 내접
    elif dist < sum:
        return 2
    elif dist == sum:
        return 1  # 외접
    else:
        return 0


def test():
    test_cases = [
        (0, 0, 1, 0, 0, 1),  # -1
        (0, 0, 1, 0, 0, 3),  # 0
        (0, 0, 4, 1, 1, 5),  # 2
        (0, 0, 10, 1, 1, 2),  # 0
        (0, 0, 10, 5, 0, 5),  # 1 (내접)
    ]
    for inputs in test_cases:
        print(solve(inputs))


if __name__ == "__main__":
    main()
