class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        """time 98 / space 49"""

        # Encode nums using the given rule
        source: list[int] = []
        for k in range(1, len(nums)):
            if nums[k] > nums[k - 1]:
                source.append(1)
            elif nums[k] == nums[k - 1]:
                source.append(0)
            else:
                source.append(-1)

        S = len(source)
        P = len(pattern)

        # Run KMP algorithm
        # Construct pi array
        pi = [0] * P
        i, j = 1, 0
        while i < P and j < P:
            if pattern[i] == pattern[j]:
                j += 1
                pi[i] = j
                i += 1
            elif j == 0:
                i += 1
            else:
                j = pi[j - 1]

        # Match
        count = 0
        s, p = 0, 0
        while s < S and p < P:
            if source[s] == pattern[p]:
                s += 1
                if p == P - 1:
                    count += 1  # matched
                    p = pi[p]  # skip identical part
                else:
                    p += 1  # proceed
            elif p == 0:
                s += 1  # give up
            else:
                p = pi[p - 1]

        return count


if __name__ == "__main__":
    # fmt: off
    nums = [1,2,3,4,5,6]
    pattern = [1,1]

    nums = [1,4,4,1,3,5,5,3]
    pattern = [1,0,-1]
    # fmt: on

    answer = Solution().countMatchingSubarrays(nums, pattern)
    print(f"{answer = }")
