# https://www.acmicpc.net/problem/5214

from sys import stdin
from collections import defaultdict, deque

# tube를 node로 취급


def main():
    n_stations, _, n_tubes = (int(t) for t in stdin.readline().split())
    graph = Graph()
    for i in range(1, n_tubes + 1):
        graph.add_connection(i, [int(t) for t in stdin.readline().split()])

    print(graph.bfs(start=1, end=n_stations))


class Graph:
    def __init__(self):
        self.graph: defaultdict[int, list[int]] = defaultdict(list)
        # Tubes are represented with negative indices

    def add_connection(self, idx: int, nodes: list[int]):
        # station -> tube
        for v in nodes:
            self.graph[v].append(-1 * idx)
        # tube -> station
        self.graph[-1 * idx] = nodes

    def bfs(self, start: int, end: int) -> int:
        # Special case
        if start == end:
            return 1

        queue = deque([(start, 0)])
        reserved = {start}

        while queue:
            u, d = queue.popleft()

            for v in self.graph[u]:
                if v == end:
                    assert d % 2 == 1
                    return (d + 1) // 2 + 1
                if v in reserved:
                    continue

                reserved.add(v)
                queue.append((v, d + 1))

        return -1  # not reachable


if __name__ == "__main__":
    main()
