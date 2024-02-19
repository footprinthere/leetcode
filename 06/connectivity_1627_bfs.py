import math
from collections import deque


class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        """
        connectivity를 query 하나마다 일일이 검사
        O(V^2 + (V+E)*Q)  (Q = len(queries))
        TLE 48 / 67
        """
        
        # 그래프 초기화
        graph = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i):
                graph[i][j] = graph[j][i]   # symmetric (undirected)

            for j in range(i+1, n):
                # gcd가 threshold보다 크면 connected
                graph[i][j] = (math.gcd(i+1, j+1) > threshold)

        answer = [is_conntected(graph, src-1, trg-1) for src, trg in queries]
        return answer


def is_conntected(graph: list[list[bool]], src: int, trg: int) -> bool:
    """ BFS를 통해 두 node가 연결되어 있는지 검사 """

    queue = deque([src])
    visited = set()

    while queue:
        # print("q:", queue)

        v = queue.popleft()
        if v == trg:
            return True
        
        # v는 src와 연결되어 있으므로 그 결과를 기억
        graph[src][v] = graph[v][src] = True
        visited.add(v)

        # print("visited:", visited)
        # print("adj:", graph[v])

        for u in range(len(graph)):
            if graph[u][v] and u not in visited:
                queue.append(u)

    return False


if __name__ == "__main__":
    # n = 6
    # th = 2
    # queries = [[1,4],[2,5],[3,6]]

    n = 6
    th = 0
    queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
    
    answer = Solution().areConnected(n, th, queries)
    print("answer:", answer)
