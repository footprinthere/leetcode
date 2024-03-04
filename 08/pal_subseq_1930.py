class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """time 38 / space 96"""

        result = set()  # ("a", "c") -> "a c a"
        visited = set()

        for i, ch in enumerate(s):
            if ch in visited:
                # 이미 본 적 있으면 skip
                continue

            j = s.rfind(ch)  # 뒤에서부터 동일한 글자 찾음

            # 그 사이에 있는 모든 글자를 가운데 글자로 쓸 수 있음
            for m in s[i + 1 : j]:
                result.add((ch, m))

            visited.add(ch)

        return len(result)


if __name__ == "__main__":
    s = "aabca"
    # (a)abc(a)

    answer = Solution().countPalindromicSubsequence(s)
    print(f"{answer = }")
