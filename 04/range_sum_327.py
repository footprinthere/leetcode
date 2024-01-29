import heapq


class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        """
        60/67에서 시간초과
        N^2 logN ?
        -> heap을 씀으로써 오히려 나빠진 듯
        """
        
        # 누적 합 계산
        c = 0
        cum = []
        for n in nums:
            c += n
            cum.append(c)

        answer = 0

        # 각 위치를 끝으로 하는 range 개수 세기
        cum_heap = []
        for c in cum:
            # 1개짜리 range
            if lower <= c <= upper:
                answer += 1
            
            answer += count_between(cum_heap, c - upper, c - lower)
            heapq.heappush(cum_heap, c)

        return answer


def count_between(heap: list[int], lower: int, upper: int) -> int:
    # print(f"count heap {heap} - [{lower}, {upper}]")

    copy = [n for n in heap]

    count = 0
    while copy and copy[0] <= upper:
        n = heapq.heappop(copy)
        # print(f"popped {n}")
        if n >= lower:
            count += 1
    
    return count


if __name__ == "__main__":
    nums = [-2,5,-1]
    lower = -2
    upper = 2

    answer = Solution().countRangeSum(nums, lower, upper)
    print(answer)
