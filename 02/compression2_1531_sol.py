""" Solution 참고했음 """

import math

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)
        dp = [[float('inf')] * (k+1) for _ in range(N+1)]

        dp[0][0] = 0

        for i in range(1, N+1):
            for j in range(0, k+1):
                count, deleted = 0, 0
                # count: 현재 보고 있는 target character와 똑같은 것의 수
                # deleted: target과 다른, 그래서 지워야 하는 것의 수
                
                # i번째 char를 지우지 않는 경우
                #   -> 직전에 있는 다른 char들을 최대한 지워 merge 도모
                for t in reversed(range(1, i+1)):
                    if s[i-1] == s[t-1]:
                        count += 1
                    else:
                        deleted += 1

                    if j >= deleted:
                        dp[i][j] = min(
                            dp[i][j],
                            dp[t-1][j - deleted] + 1 + (int(math.log10(count)) + 1 if count > 1 else 0)
                        )

                # i번째 char를 지우는 경우
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])

        return dp[-1][-1]


if __name__ == "__main__":
    s = "abc"
    k = 2
    answer = Solution().getLengthOfOptimalCompression(s, k)

    print(answer)
