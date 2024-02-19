import math


class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        """
        time 52 / space 69
        """

        if threshold == 0:
            return [True] * len(queries)
        
        uf = UnionFind(n, threshold)
        answer = [
            uf.find(src-1) == uf.find(trg-1)
            for src, trg in queries
        ]
        return answer


class UnionFind:
    def __init__(self, n: int, threshold: int):
        self.parent = [i for i in range(n)]

        # # 초기화 (테케 58ms) -> 이렇게 했을 때는 TLE
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if math.gcd(i+1, j+1) > threshold:
        #             self.union(i, j)

        # hint 따라 초기화 (테케 55ms)
        for k in range(threshold + 1, n // 2 + 1):
            for t in range(1, n // k + 1):
                self.union(k - 1, k * t - 1)

    def find(self, v: int) -> int:
        """ 최상단 root를 찾아줌 """
        p = self.parent[v]
        if v == p:
            return v
        else:
            f = self.parent[v] = self.find(p)   # optimized (path compression)
            return f
        
    def union(self, u: int, v: int):
        """ 두 vertex가 속한 집합을 합침 """
        x = self.find(u)
        y = self.find(v)

        self.parent[x] = y


if __name__ == "__main__":
    n = 6
    th = 2
    queries = [[1,4],[2,5],[3,6]]

    # n = 6
    # th = 0
    # queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
    
    answer = Solution().areConnected(n, th, queries)
    print("answer:", answer)
