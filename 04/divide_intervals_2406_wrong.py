class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        """ WRONG """
        
        intervals.sort()
        overlapped = [False] + [
            are_overlapped(intervals[i-1], intervals[i])
            for i in range(1, len(intervals))
        ]
        # overlapped[i]: intervals[i-1]와 intervals[i]가 서로 겹치면 True

        print(intervals)
        print(overlapped)

        # 서로 이웃하는 True의 최대 개수 구하기
        n = 1
        max_n = 1
        
        for b in overlapped:
            if b:
                n += 1
            else:
                max_n = max(max_n, n)
                n = 1
        max_n = max(max_n, n)

        return max_n


def are_overlapped(a: list[int], b: list[int]) -> bool:
    return a[0] <= b[1] and b[0] <= a[1]


if __name__ == "__main__":
    # intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

    intervals = [[441459,446342],[801308,840640],[871890,963447],[228525,336985],[807945,946787],[479815,507766],[693292,944029],[751962,821744]]

    # intervals = [[159431,428743],[614908,651142],[431031,806494]]

    answer = Solution().minGroups(intervals)
    print(answer)
