"""
각 line의 수들을 queue에 넣어 하나씩 pop 하는 방식
53번째 test case에서 시간초과
"""

from collections import deque


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        queues = [deque(line) for line in nums]
        start = 0                   # 몇 번째 줄부터 시작할지
        increasing = True           # start가 증가하고 있는지의 여부
        left = sum(map(len, nums))  # 아직 순회하지 않은 칸의 개수
        answer = []

        while left:
            for i in reversed(range(0, start + 1)):
                if len(queues[i]) == 0:
                    continue
                answer.append(queues[i].popleft())
                left -= 1

            if increasing:
                # 초기에는 시작 위치를 한 줄씩 아래로 이동
                start += 1
                if start >= len(queues) - 1:
                    start = len(queues) - 1
                    increasing = False
            else:
                # 이후에는 소진될 때마다 한 줄씩 위로 이동
                while start >= 0 and len(queues[start]) == 0:
                    start -= 1

        return answer
    

if __name__ == "__main__":
    # nums = [[1,2,3],[4,5,6],[7,8,9]]
    # nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    nums = [[1,2,3,4,5,6]]

    answer = Solution().findDiagonalOrder(nums)

    print(answer)
