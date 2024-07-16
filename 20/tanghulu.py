# https://www.acmicpc.net/problem/30804

from sys import stdin


def main():
    N = int(stdin.readline().strip())
    fruits = [int(t) for t in stdin.readline().split()]

    groups = []
    count = 1
    for n in range(1, N):
        if fruits[n - 1] == fruits[n]:
            count += 1
        else:
            groups.append((count, fruits[n - 1]))
            count = 1
    groups.append((count, fruits[-1]))

    max_count = 0
    for i in range(len(groups)):
        seen = set()
        count = 0
        for c, f in groups[i:]:
            seen.add(f)
            if len(seen) > 2:
                max_count = max(max_count, count)
                break
            count += c
        else:
            max_count = max(max_count, count)

    print(max_count)


if __name__ == "__main__":
    main()
