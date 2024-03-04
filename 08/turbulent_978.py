class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        """time 84 / space 86"""

        max_val = 1
        prev = [1, 1]  # dp table의 한 row

        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                prev = [1, 1]
                continue
            elif arr[i - 1] > arr[i]:
                val = prev[1] + 1
                curr = [val, 1]
            else:
                val = prev[0] + 1
                curr = [1, val]

            prev = curr
            max_val = max(val, max_val)

        return max_val

    def simple(self, arr: list[int]) -> int:
        """time 24 / space 12"""

        L = len(arr)
        dp = [[1, 1] for _ in range(L)]
        # dp[i] -> arr[i]로 끝나는 최장 subarray의 길이
        #          dp[i][0] : arr[i-1] > arr[i] (방금 감소)
        #          dp[i][1] : arr[i-1] < arr[i] (방금 증가)

        for i in range(1, L):
            if arr[i - 1] > arr[i]:
                dp[i][0] = dp[i - 1][1] + 1
            elif arr[i - 1] < arr[i]:
                dp[i][1] = dp[i - 1][0] + 1

        return max(max(r) for r in dp)


if __name__ == "__main__":
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]

    answer = Solution().maxTurbulenceSize(arr)
    print(f"{answer = }")
