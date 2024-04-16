class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """time 56 / space 17"""

        l1 = sorted(list(s1))
        l2 = sorted(list(s2))

        cmp = 0

        for ch1, ch2 in zip(l1, l2):
            curr = compare(ch1, ch2)
            if curr == 0:
                continue
            if cmp == 0:
                cmp = curr
                continue

            if curr != cmp:
                return False

        return True


def compare(ch1: str, ch2: str) -> int:
    if ch1 > ch2:
        return 1
    elif ch1 < ch2:
        return -1
    else:
        return 0


if __name__ == "__main__":
    s1 = "leetcodee"
    s2 = "interview"

    answer = Solution().checkIfCanBreak(s1, s1)
    print(f"{answer = }")
