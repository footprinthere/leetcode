import heapq


class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        """
        Solution 참고
        time 63% / space 87%
        """
        
        end_heap = [-1]
        # heap의 각 item은 각 group에 속한 interval들의 end의 최댓값에 해당함

        for start, end in sorted(intervals):
            if start > end_heap[0]:
                # 현재 start보다 작은 end를 가진 group이 있으면 병합
                heapq.heappop(end_heap)
            heapq.heappush(end_heap, end)

        return len(end_heap)


if __name__ == "__main__":
    # intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

    # intervals = [[441459,446342],[801308,840640],[871890,963447],[228525,336985],[807945,946787],[479815,507766],[693292,944029],[751962,821744]]

    intervals = [[159431,428743],[614908,651142],[431031,806494]]

    answer = Solution().minGroups(intervals)
    print(answer)
