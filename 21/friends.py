# https://www.acmicpc.net/problem/1058

from sys import stdin
from collections import defaultdict
from functools import reduce


def main():
    N = int(stdin.readline())
    table: list[list[bool]] = []
    for _ in range(N):
        row = list(map(lambda ch: ch == "Y", list(stdin.readline().strip())))
        table.append(row)

    friends = defaultdict(set)
    for i in range(N):
        for j in range(N):
            if table[i][j]:
                friends[i].add(j)

    two_friends = {}
    for i in range(N):
        two_friends[i] = friends[i] | reduce(
            lambda x, y: x | y,
            (friends[j] for j in friends[i]),
            set(),
        ) - {i}
    # 내 친구 + 내 모든 친구들의 친구 - 나 자신

    answer = max(len(two_friends[i]) for i in range(N))
    print(answer)


if __name__ == "__main__":
    main()
