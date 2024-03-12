class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        """time 74 / space 93"""

        kmp = KMP(source=nums1, pattern=nums2)

        max_len = 0
        for _ in range(len(nums2)):
            if len(kmp.pattern) <= max_len:
                break  # further matches are redundant

            matched = kmp.match()
            max_len = max(max_len, matched)

            kmp.slice_pattern()

        return max_len


class KMP:
    def __init__(self, source: list[int], pattern: list[int]):
        self.source = source
        self.pattern = pattern

    def _build_pi(self) -> list[int]:
        pi = [0] * len(self.pattern)

        j = 0  # end of prefix
        for i in range(1, len(self.pattern)):
            while j > 0 and self.pattern[i] != self.pattern[j]:
                j = pi[j - 1]

            if self.pattern[i] == self.pattern[j]:
                j += 1
                pi[i] = j

        return pi

    def match(self) -> int:
        """
        max_t (pattern[0...t] is included in source)
        """

        max_len = 0

        pi = self._build_pi()
        s, p = 0, 0

        while s < len(self.source) and p < len(self.pattern):
            if self.pattern[p] == self.source[s]:
                s += 1
                p += 1
                max_len = max(max_len, p)  # length of agreed part
            elif p > 0:
                p = pi[p - 1]
            else:
                s += 1

        return max_len

    def slice_pattern(self):
        self.pattern = self.pattern[1:]


def naive(nums1: list[int], nums2: list[int]) -> int:
    """O(N^3) :: TLE 41 / 53"""

    max_len = 0

    for p1 in range(len(nums1)):
        for p2 in range(len(nums2)):
            slice1 = nums1[p1:]
            slice2 = nums2[p2:]

            for i in range(min(len(slice1), len(slice2))):
                if slice1[i] != slice2[i]:
                    break
            else:
                i += 1

            if i > max_len:
                max_len = i
                print(f"{p1 = }, {p2 = }, {i = }")
                print(slice1[:i])
                print(slice2[:i])

    return max_len


if __name__ == "__main__":
    # fmt: off
    # nums1 = [1, 2, 3, 2, 1]
    # nums2 = [3, 2, 1, 4, 7]

    # nums1 = [0, 0, 0, 0, 1]
    # nums2 = [1, 0, 0, 0, 0]

    # nums1 = [1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0]
    # nums2 = [1,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0]

    nums1 = [0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1]
    nums2 = [1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0]

    answer = Solution().findLength(nums1, nums2)
    print(f"{answer = }")
    # fmt: on
