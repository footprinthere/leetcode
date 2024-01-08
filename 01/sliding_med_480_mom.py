"""
median of medians 알고리즘 사용
"""


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        """med queue보다 더 빨리 time limit exceeded """
        
        answer = []
        queue = []

        for num in nums[:k]:
            queue.append(num)
        answer.append(find_median(queue))

        idx = k
        while idx < len(nums):
            queue.pop(0)
            queue.append(nums[idx])
            answer.append(find_median(queue))

            idx += 1

        return answer
    

def find_median(arr: list[int]) -> float:
    if len(arr) % 2 == 1:
        return linear_select(arr, len(arr) // 2)
    else:
        # TODO: 개선 가능할 듯
        return (
            linear_select(arr, len(arr) // 2 - 1)
            + linear_select(arr, len(arr) // 2)
        ) / 2


def linear_select(arr: list[int], rank: int) -> int:

    # Base case
    if len(arr) <= 5:
        return sorted(arr)[rank]
    
    # Find medians of each parts
    def _m(_a: list[int]) -> int:
        return sorted(_a)[len(_a) // 2]
    
    medians = [
        _m(arr[start : start + 5])
        for start in range(0, len(arr), 5)
    ]

    # Recursive call to find the median of medians
    mom = linear_select(medians, len(medians) // 2)

    # Partition, using mom as pivot
    left, right = [], []
    is_pivot_skipped = False
    for item in arr:
        if not is_pivot_skipped and item == mom:
            is_pivot_skipped = True
        elif item < mom:
            left.append(item)
        else:
            right.append(item)

    # print(f"=== rank {rank}")
    # print(sorted(left), mom, sorted(right))

    # Recursion
    if rank < len(left):
        # print("selected left")
        return linear_select(left, rank)
    elif rank == len(left):
        # print("selected pivot")
        return mom
    else:
        # print(f"selected right -- {rank - len(left) - 1}, len(left)={len(left)}")
        return linear_select(right, rank - len(left) - 1)
    

if __name__ == "__main__":
    # nums = [1,3,-1,-3,5,3,6,7]
    # k = 3

    # nums = [1,2,3,4,2,3,1,4,2]
    # k = 4

    nums = [5,2,2,7,3,7,9,0,2,3]
    k = 9

    answer = Solution().medianSlidingWindow(nums, k)
    print(answer)
