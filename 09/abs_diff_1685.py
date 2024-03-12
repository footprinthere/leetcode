class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        """time 98 / space 11"""

        L = len(nums)
        answer = [0] * L

        unseen = sum(nums)
        seen = 0
        mul = 1 - L

        for i, n in enumerate(nums):
            unseen -= n
            answer[i] = mul * n + unseen - seen
            # -> answer[i] = (2 * i + 1 - L) * n + unseen - seen
            mul += 2
            seen += n

        return answer


if __name__ == "__main__":
    nums = [2, 3, 5]
    nums = [1, 4, 6, 8, 10]

    answer = Solution().getSumAbsoluteDifferences(nums)
    print(f"{answer = }")
