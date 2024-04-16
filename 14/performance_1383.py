import heapq


class Solution:
    def maxPerformance(
        self, n: int, speed: list[int], efficiency: list[int], k: int
    ) -> int:
        """TLE 54/55 -- O(NlogN + N*K)"""

        pool = sorted([(e, s) for e, s in zip(efficiency, speed)], reverse=True)

        # [t][i] -> pool[: i+1][1] (speed) 중에서 t개의 합의 최댓값
        # 메모리 절약 위해 직전 row만 보관
        prev = [0] * n
        answer = 0

        for t in range(1, k + 1):
            curr = [0] * n

            for i in range(t - 1, n):
                curr[i] = max(curr[i - 1], prev[i - 1] + pool[i][1])

                performance = pool[i][0] * curr[i]
                answer = max(answer, performance)

            prev = curr

        return answer % (10**9 + 7)

    def with_heap(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        """TLE 54/55 -- O(NlogN * K)"""
        pool = sorted([(e, s) for e, s in zip(efficiency, speed)], reverse=True)
        answer = 0

        for i in range(n):
            speed_heap = [-1 * s for _, s in pool[: i + 1]]
            heapq.heapify(speed_heap)

            total = -1 * sum(heapq.heappop(speed_heap) for _ in range(min(i + 1, k)))
            answer = max(answer, pool[i][0] * total)

        return answer % (10**9 + 7)

    def from_solution(
        self, n: int, speed: list[int], efficiency: list[int], k: int
    ) -> int:
        """time 54 / space 75 -- O(N(logN + logK))"""

        sum_speed = 0
        speed_heap = []  # 현재 합산되어 있는 speed들
        answer = 0

        for e, s in sorted([(e, s) for e, s in zip(efficiency, speed)], reverse=True):
            sum_speed += s
            heapq.heappush(speed_heap, s)

            if len(speed_heap) > k:
                # k개 초과 시 가장 작은 것을 버림
                sum_speed -= heapq.heappop(speed_heap)

            answer = max(answer, e * sum_speed)

        return answer % (10**9 + 7)


if __name__ == "__main__":
    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 2  # 60

    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 3  # 68

    n = 3
    speed = [2, 8, 2]
    efficiency = [2, 7, 1]
    k = 2  # 56

    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 2  # 60

    answer = Solution().from_solution(n, speed, efficiency, k)
    print(f"{answer = }")
