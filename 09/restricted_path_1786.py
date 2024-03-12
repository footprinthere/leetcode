import heapq
from collections import defaultdict
from functools import lru_cache


class Solution:
    def countRestrictedPaths(self, n: int, edges: list[list[int]]) -> int:
        """time 43 / space 7"""

        graph = Graph(n, edges)
        graph.dijkstra()
        return graph.count_restricted() % int(1e9 + 7)


class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.graph = defaultdict(list)  # matrix 형태로 했을 때 memory limit exceeded
        self.dist = [-1] + [float("inf")] * (n - 1) + [0]

        for u, v, weight in edges:
            self.graph[u].append((v, weight))
            self.graph[v].append((u, weight))

    def dijkstra(self):
        """Run algorithm with Vertex n as starting point"""

        heap = [(0, self.n)]  # (distance, vertex)
        visited = set()

        while len(visited) < self.n:
            # Select the closest vertex
            while (closest := heapq.heappop(heap)[1]) in visited:
                ...

            visited.add(closest)
            for v, weight in self.graph[closest]:
                if (new_dist := self.dist[closest] + weight) < self.dist[v]:
                    self.dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

    def count_restricted(self) -> int:
        """Use DFS to count restricted paths"""

        # Visited vertices are never visited again
        # since distances have to be monotonically decreasing
        @lru_cache(maxsize=None)
        def _dfs(u: int) -> int:
            if u == self.n:
                return 1

            output = 0
            for v, _ in self.graph[u]:
                if self.dist[u] > self.dist[v]:
                    output += _dfs(v)

            return output

        return _dfs(1)
