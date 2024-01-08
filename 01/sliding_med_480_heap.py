import heapq


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        """ time limit exceeded """

        answer = []
        heap = MedianHeap()

        for num in nums[:k]:
            heap.push(num)
        answer.append(heap.peek())

        idx = k     # 새로 추가할 수의 index
        while idx < len(nums):
            heap.replace(old=nums[idx-k], new=nums[idx])
            answer.append(heap.peek())

            idx += 1

        return answer


class MedianHeap:
    def __init__(self):
        self.left = []      # max heap (multiplied by -1)
        self.right = []     # min heap

    def peek(self) -> float:
        if len(self.left) == len(self.right):
            return (-1 * self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -1 * self.left[0]
        else:
            return self.right[0]
        
    def push(self, num: int):
        self._add(num)
        self._balance()
        
    def replace(self, old: int, new: int):
        # remove
        if -1 * old in self.left:
            self.left.remove(-1 * old)
            heapq.heapify(self.left)
        elif old in self.right:
            self.right.remove(old)
            heapq.heapify(self.right)
        else:
            raise ValueError(f"value not in heap: {old}")
        
        self._add(new)
        self._balance()

    def _add(self, num: int):
        if len(self.right) == 0 or num < self.right[0]:
            heapq.heappush(self.left, -1 * num)
        else:
            heapq.heappush(self.right, num)
        
    def _balance(self):
        diff = len(self.left) - len(self.right)
        while not (-1 <= diff <= 1):
            if diff > 0:
                # left에 더 많음
                num = -1 * heapq.heappop(self.left)
                heapq.heappush(self.right, num)
                diff -= 2
            else:
                # right에 더 많음
                num = heapq.heappop(self.right)
                heapq.heappush(self.left, -1 * num)
                diff += 2

    # # for debugging
    # def __str__(self) -> str:
    #     return f"{self.left}, {self.right}"


if __name__ == "__main__":
    # nums = [1,3,-1,-3,5,3,6,7]
    # k = 3

    nums = [1,2,3,4,2,3,1,4,2]
    k = 4

    answer = Solution().medianSlidingWindow(nums, k)
    print(answer)
