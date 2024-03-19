class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        """time 10 / space 15"""

        if x > y:
            x, y = y, x  # now x <= y

        # Initialize table
        floyd = [[1000] * n for _ in range(n)]
        for i in range(n - 1):
            floyd[i][i + 1] = 1
        floyd[x - 1][y - 1] = 1

        def _get(_i: int, _j: int) -> int:
            if _i > _j:
                _i, _j = _j, _i
            return floyd[_i][_j]

        # Run Floyd's algorithm
        for k in range(n):
            for i in range(n):
                for j in range(i + 1, n):
                    floyd[i][j] = min(floyd[i][j], _get(i, k) + _get(k, j))

        answer = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                answer[floyd[i][j] - 1] += 2

        return answer


if __name__ == "__main__":
    # n, x, y = 3, 1, 3
    n, x, y = 5, 2, 4
    # n, x, y = 4, 1, 1

    # n, x, y = 5, 1, 5  # [10, 10, 0, 0, 0]
    n, x, y = 3, 3, 1  # [6, 0, 0]

    answer = Solution().countOfPairs(n, x, y)
    print(f"{answer = }")
