"""
KMP 설명
https://yiyj1030.tistory.com/495
https://bowbowbow.tistory.com/6

[IDEA]
KMP는 string match 알고리즘의 일종.
string match를 naive 하게 하려면
    - 일치하면 길이를 하나씩 늘리고
    - 일치하지 않으면 한 칸 미루고
하면서 계속 비교하면 됨.
그런데 이때 한 칸씩만 미루면 불필요한 비교를 계속하게 됨.
그래서 어차피 일치할 리가 없는 부분은 건너뛰면서 비교를 하기 위해 pi 배열 필요.

pi[i] = s[0 : i+1]의 prefix와 postfix가 서로 일치하게 되는 최대의 길이
        arg max_j { s[0 : j] == s[... : i+1] }

이 문제에서는 KMP 자체를 쓰지는 않지만, pi 배열의 아이디어를 차용함.
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """time 54 / space 14"""

        orig = s + "#" + "".join(reversed(s))
        # "ABAB" -> "{ABA}B#B{ABA}"
        # 이제 이 문자열 전체의 pi 값은 index 0에서 시작하는 최대의 palindrom substring의 길이가 됨

        pi = [0] * len(orig)

        j = 0  # prefix의 끝을 가리킴
        for i in range(1, len(orig)):

            while j > 0 and orig[i] != orig[j]:
                # char 일치하지 않으면 j를 앞당겨 prefix의 길이를 줄여야 함.
                # 이때 orig[: j] == orig[... : i]가 보장되므로,
                # P := pi[j-1]라 하면 orig[: P] == orig[... : i] 성립.
                # 따라서 j = P로 둠으로써 prefix의 길이를 줄여 다시 비교해나가야 함.
                j = pi[j - 1]

            if orig[i] == orig[j]:
                j += 1
                pi[i] = j  # prefix의 길이를 pi 값으로 사용

        # 이제 pi[-1]이 longest palindrom substring의 길이임
        l = pi[-1]
        return "".join(reversed(s[l:])) + s


if __name__ == "__main__":
    # s = "aacecaaa"
    # s = "abcd"
    s = "cacacacba"
    # s = "aaaaacdaaaaa"
    # s = "a" * 20000 + "cd" + "a" * 20000
    # s = "aab"
    # s = "ababbbabbaba"

    answer = Solution().shortestPalindrome(s)
    print(answer)

    from collections import Counter

    print(Counter(answer))
    print(len(s), len(answer))
