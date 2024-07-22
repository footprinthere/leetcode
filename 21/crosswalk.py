# https://www.acmicpc.net/problem/24042

from sys import stdin
from collections import defaultdict
import math
import heapq as hq


def main():
    N, M = (int(t) for t in stdin.readline().split())
    graph = Graph(n_nodes=N, cycle=M)

    for i in range(M):
        a, b = (int(t) for t in stdin.readline().split())
        graph.add_edge(a, b, i + 1)  # 1-indexed

    print(graph.dijkstra(start=1, end=N))


class Graph:
    def __init__(self, n_nodes: int, cycle: int):
        self.graph = defaultdict(list)
        self.n_nodes = n_nodes
        self.cycle = cycle

    def add_edge(self, a: int, b: int, idx: int):
        self.graph[a].append((b, idx))
        self.graph[b].append((a, idx))

    def dijkstra(self, start: int, end: int) -> int:
        dist = [float("inf")] * (self.n_nodes + 1)  # 1-indexed
        dist[start] = 0
        visited = {start}
        heap = []

        for v, d in self.graph[start]:
            dist[v] = d
            hq.heappush(heap, (d, v))

        while heap:
            min_dist, min_node = hq.heappop(heap)
            if min_node == end:
                return min_dist
            if min_node in visited:
                continue
            visited.add(min_node)

            for v, d in self.graph[min_node]:
                if v in visited:
                    continue
                x = math.ceil((min_dist - d) / self.cycle)
                d_adj = d + self.cycle * x
                if d_adj < dist[v]:
                    dist[v] = d_adj
                    hq.heappush(heap, (d_adj, v))

        raise RuntimeError("End node is not reachable")


if __name__ == "__main__":
    main()
