"""
[IDEA]
* 교체를 통해 아무 substring도 palindrome이 될 수 있기 때문에, 본질적으로 모든 가능성을 검토해야 함
    -> backtracking?
"""

from itertools import combinations
from functools import lru_cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """TLE 27 / 32"""

        min_changes = 1000

        @lru_cache(maxsize=None)
        def _check_pal(start: int, end: int) -> int:
            n_changes = 0
            i, j = start, end - 1
            while i < j:
                if s[i] != s[j]:
                    n_changes += 1
                i += 1
                j -= 1
            return n_changes

        if k == 1:
            return _check_pal(0, len(s))

        for comb in combinations(range(1, len(s)), k - 1):
            # [0:comb[0]], [comb[0]:comb[1]], ..., [comb[k-2]:len(s)]
            n_changes = 0

            n_changes += _check_pal(0, comb[0])
            if n_changes > min_changes:
                continue

            for i in range(k - 2):
                n_changes += _check_pal(comb[i], comb[i + 1])
                if n_changes > min_changes:
                    continue

            if k >= 2:
                n_changes += _check_pal(comb[k - 2], len(s))

            if n_changes < min_changes:
                min_changes = n_changes

        return min_changes


if __name__ == "__main__":
    test_cases = [
        # ("abc", 2),
        # ("aabbc", 3),
        # ("leetcode", 8),
        ("oiwwhqjkb", 1),
    ]

    for t in test_cases:
        print(">>>", t)
        answer = Solution().palindromePartition(*t)
        print(f"\t{answer = }")
