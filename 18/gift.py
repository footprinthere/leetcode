# https://www.acmicpc.net/problem/23757

from sys import stdin
import heapq


def main():
    _ = stdin.readline()
    supplies = list(int(t) for t in stdin.readline().split())
    demands = list(int(t) for t in stdin.readline().split())

    supplies = [-1 * s for s in supplies]  # max heap
    heapq.heapify(supplies)

    for d in demands:
        top = -1 * heapq.heappop(supplies)
        if d > top:
            print("0")
            return
        if (remain := top - d) >= 0:
            heapq.heappush(supplies, -1 * remain)

    print("1")


if __name__ == "__main__":
    main()
