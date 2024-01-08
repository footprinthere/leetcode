"""
median heap을 사용하되, remove 할 때 매번 search 해서 제거하는 대신
기록만 해두고 이후 제거된 값이 맨 앞에 왔을 때 제거
"""

import heapq
from collections import defaultdict


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        answer = []
        heap = MedianHeap(nums[:k])
        answer.append(heap.peek())

        idx = k     # 새로 추가할 수의 index
        while idx < len(nums):
            heap.replace(old=nums[idx-k], new=nums[idx])
            answer.append(heap.peek())

            idx += 1

        return answer


class MedianHeap:
    def __init__(self, nums: list[int]):
        self.left = []      # max heap (multiplied by -1)
        self.right = []     # min heap

        for num in nums:
            heapq.heappush(self.left, -1 * num)
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
            if len(self.left) < len(self.right):
                heapq.heappush(self.left, -1 * heapq.heappop(self.right))
        # 실행 후 len(left) >= len(right), 차이 최대 1
        
        self.size = len(nums)
        self.remove_counter = defaultdict(int)

    def peek(self) -> float:
        if self.size % 2 == 1:
            # 홀수라면 len(left) > len(right)
            return -1 * self.left[0]
        else:
            return (-1 * self.left[0] + self.right[0]) / 2
        
    def replace(self, old: int, new: int):
        balance = 0     # 각 turn에서 (left 순유입 - right 순유입)

        # add
        med = self.peek()
        if new <= med:  # size가 홀수라면 median은 항상 left에 있음
            heapq.heappush(self.left, -1 * new)
            balance = 1
        else:
            heapq.heappush(self.right, new)
            balance = -1

        # mark as removed
        self.remove_counter[old] += 1
        if old <= med:
            balance -= 1
        else:
            balance += 1

        # rebalance (이때 balance = -2 or 0 or 2)
        if balance < 0:
            heapq.heappush(self.left, -1 * heapq.heappop(self.right))
        elif balance > 0:
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))

        # remove
        while self.left and self.remove_counter[-1 * self.left[0]] > 0:
            self.remove_counter[-1 * self.left[0]] -= 1
            heapq.heappop(self.left)
        while self.right and self.remove_counter[self.right[0]] > 0:
            self.remove_counter[self.right[0]] -= 1
            heapq.heappop(self.right)


if __name__ == "__main__":
    # nums = [1,3,-1,-3,5,3,6,7]
    # k = 3

    nums = [1,2,3,4,2,3,1,4,2]
    k = 3

    answer = Solution().medianSlidingWindow(nums, k)
    print(answer)
