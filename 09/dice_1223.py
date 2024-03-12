from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        """time 14 / space 5"""

        @lru_cache(maxsize=None)
        def _dp(length: int, last: int, consec: int) -> int:
            if length == n:
                return 1

            output = 0
            for d in range(6):
                if d == last:
                    if consec < rollMax[d]:
                        output += _dp(length + 1, d, consec + 1)
                else:
                    output += _dp(length + 1, d, 1)
            return output

        return _dp(0, -1, 0) % int(1e9 + 7)

    def climb_up(self, n: int, rollMax: list[int]) -> int:
        """
        Solution 참고했음
        time 69 / space 55
        """

        dp = [[0] * 7 for _ in range(n + 1)]
        # dp[i][j=0...5]: 길이 i이면서 j로 끝나는 것의 개수
        # dp[i][6] = sum(sum[i][j] for j in 0...5)

        # Initialize
        dp[0][6] = 1  # 길이 0인 것은 총 1개
        for j in range(6):
            dp[1][j] = 1  # 길이 1인 것은 각각 1개씩
        dp[1][6] = 6  # 총 6개

        # DP
        for i in range(2, n + 1):
            for j in range(6):
                # 예를 들어 rollMax[j] = 2라면, XXXXj의 개수는
                #   XXX(not j) + XX(not j)
                # 와 같아짐

                for k in range(1, min(rollMax[j], i) + 1):
                    dp[i][j] += dp[i - k][6] - dp[i - k][j]

            dp[i][6] = sum(dp[i][0:6])

        return dp[-1][6] % int(1e9 + 7)


if __name__ == "__main__":
    n = 2
    rollMax = [1, 1, 2, 2, 2, 3]  # 34

    # n = 2
    # rollMax = [1, 1, 1, 1, 1, 1]  # 30

    n = 6
    rollMax = [6, 6, 2, 2, 2, 1]

    answer = Solution().dieSimulator(n, rollMax)
    print(f"{answer = }")
