# https://www.acmicpc.net/problem/25328

from sys import stdin
from itertools import combinations


def main():
    x = stdin.readline().strip()
    y = stdin.readline().strip()
    z = stdin.readline().strip()
    k = int(stdin.readline().strip())

    x_combi = list(combinations(x, k))
    y_combi = list(combinations(y, k))
    z_combi = list(combinations(z, k))

    pool = x_combi + y_combi + z_combi

    seen = set()  # seen once
    answers = set()  # seen twice or more

    for combi in pool:
        if combi not in seen:
            seen.add(combi)
        else:
            answers.add(combi)

    if len(answers) == 0:
        print(-1)
        return

    for answer in sorted(list(answers)):
        print("".join(answer))


if __name__ == "__main__":
    main()
