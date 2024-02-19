import math


class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        """
        모든 node 간의 연결을 확인해야 하므로 Floyd 알고리즘 사용 -- O(V^3)
        TLE 44 / 67
        """
        
        floyd = Floyd(n, threshold)
        floyd.run()

        print(*floyd.table, sep="\n")

        answer = [floyd.get(i-1, j-1) for i, j in queries]
        return answer


class Floyd:
    def __init__(self, n: int, threshold: int):
        self.n = n
        self.table = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    self.table[i][j] = True
                else:
                    # gcd가 threshold보다 크면 connected
                    self.table[i][j] = (math.gcd(i+1, j+1) > threshold)

    def run(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(i, self.n):
                    self.table[i][j] = self.table[i][j] or (self.get(i, k) and self.get(k, j))


    def get(self, i: int, j: int) -> bool:
        if i <= j:
            return self.table[i][j]
        else:
            return self.table[j][i]


if __name__ == "__main__":
    n = 6
    th = 2
    queries = [[1,4],[2,5],[3,6]]
    
    answer = Solution().areConnected(n, th, queries)
    print("answer:", answer)
