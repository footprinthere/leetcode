LARGE_INT = 1000


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """time 98 / space 72"""

        check_pal_memo = [[-1] * len(s) for _ in range(len(s))]

        def _check_pal(start: int, end: int) -> int:
            """[start : end+1]가 palindrome이 되려면 몇 글자를 바꿔야 하나?"""
            if (memo := check_pal_memo[start][end]) > -1:
                return memo

            n_changes = 0
            i, j = start, end
            while i < j:
                if s[i] != s[j]:
                    n_changes += 1
                i += 1
                j -= 1

            check_pal_memo[start][end] = n_changes
            return n_changes

        dp_memo = [[LARGE_INT] * (k + 1) for _ in range(len(s))]

        def _dp(end: int, n_parts: int) -> int:
            """end로 끝나는 prefix를 n_parts개 구획으로 나눌 때"""

            if end + 1 < n_parts:
                # 글자 수보다 구획 수가 많아 불가능
                return LARGE_INT
            elif (memo := dp_memo[end][n_parts]) < LARGE_INT:
                return memo

            if n_parts == 1:
                # 구획이 1개
                n_changes = _check_pal(0, end)
                dp_memo[end][n_parts] = n_changes
                return n_changes
            elif n_parts == end + 1:
                # 글자 수와 구획 수가 동일 -> 한 글자씩 하면 됨
                dp_memo[end][n_parts] = 0
                return 0

            min_changes = LARGE_INT
            for i in range(max(n_parts - 2, 0), end):
                # s[ : i+1]을 (n_parts - 1)개로 나누고, s[i+1 : end]를 하나로 삼음
                n_changes = _dp(i, n_parts - 1) + _check_pal(i + 1, end)
                if n_changes < min_changes:
                    min_changes = n_changes

            dp_memo[end][n_parts] = min_changes
            return min_changes

        return _dp(len(s) - 1, k)


if __name__ == "__main__":
    test_cases = [
        ("abc", 2),
        ("aabbc", 3),
        ("leetcode", 8),
        ("oiwwhqjkb", 1),
    ]

    for t in test_cases:
        print(">>>", t)
        answer = Solution().palindromePartition(*t)
        print(f"\t{answer = }")
