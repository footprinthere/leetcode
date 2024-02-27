class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """TLE 120 / 123"""

        # Trivial cases
        if len(s) <= 1:
            return s

        # Init
        i = 0
        j = len(s) - 1

        left = ch_to_n(s[i])
        right = ch_to_n(s[j])
        end = j

        """
        {aa}cec{aa}a
        
        """

        # left, right: substring의 hash value
        # left에서는 가장 오른쪽에 있는 ch가 가장 낮은 자릿수, right에서는 반대

        while j > 0:
            # print(f"left (i={i}) vs right (j={j}, end={end})")
            # print(f"left (i={i}) {s[:i+1]} vs right (j={j}, end={end}) {s[j:end+1]}")

            if left == right and i >= j:
                # palindrom 발견
                break
            elif left == right and s[i + 1] == s[j - 1]:
                # 이미 일치하고 다음 char도 같으면, 다음 char 추가
                i += 1
                j -= 1
                left = left * HASH_BASE + ch_to_n(s[i])
                right = right * HASH_BASE + ch_to_n(s[j])
            else:
                # right의 맨 끝 char 제거하고 다음 char 추가
                right = right - ch_to_n(s[end]) * (HASH_BASE**i)
                end -= 1
                j -= 1
                right = right * HASH_BASE + ch_to_n(s[j])

        # j=0에 도달했는데 일치하지 않으면 길이를 줄여야 함
        while end > 0 and left != right:
            # print(f"--left (i={i}) vs right (j={j}, end={end})")
            # print(f"-- left (i={i}) {s[:i+1]} vs right (j={j}, end={end}) {s[j:end+1]}")

            left = (left - ch_to_n(s[i])) // HASH_BASE
            right = right - ch_to_n(s[end]) * (HASH_BASE**i)
            i -= 1
            end -= 1

        # Now [0, end] is the longest palindrom substring
        return "".join(reversed(s[end + 1 :])) + s


HASH_BASE = 27


def ch_to_n(ch: str) -> int:
    return ord(ch) - ord("a")


if __name__ == "__main__":
    # s = "aacecaaa"
    # s = "abcd"
    # s = "cacacacba"
    # s = "aaaaacdaaaaa"
    s = "a" * 20000 + "cd" + "a" * 20000
    # s = "aab"
    # s = "ababbbabbaba"

    answer = Solution().shortestPalindrome(s)
    print(answer)

    from collections import Counter

    print(Counter(answer))
    print(len(s), len(answer))
