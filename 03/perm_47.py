from typing import Optional
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """ time 79% / space 13% """

        N = len(nums)
        perms = permutations(nums, N)

        return list(map(list, set(perms)))

    def withoutLib(self, nums: list[int]) -> list[list[int]]:
        """ time 23% / space 5% """

        perms = []
        p(nums, 0, perms)

        return list(map(list, set(perms)))


def p(nums: list[int], start: int, result: list[tuple[int, ...]]):
    if start == len(nums) - 1:
        result.append(tuple(nums))

    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]     # swap
        p(nums, start + 1, result)
        nums[start], nums[i] = nums[i], nums[start]     # restore



if __name__ == "__main__":
    nums = [1, 1, 2]
    answer = Solution().withoutLib(nums)

    print(answer)
