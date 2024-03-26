class Solution:
    def minOperationsMaxProfit(
        self, customers: list[int], boardingCost: int, runningCost: int
    ) -> int:
        """time 95 / space 11"""

        if (boardingCost << 2) < runningCost:
            # 한 번 돌리고 4명 태워도 손해
            return -1

        n_customers = 0  # 현재 대기중인 손님 수
        curr_profit = 0
        max_profit = 0
        max_rotations = -1

        for r, n in enumerate(customers, start=1):
            n_customers += n

            n_board = min(n_customers, 4)
            n_customers -= n_board

            curr_profit += n_board * boardingCost - runningCost
            if curr_profit > max_profit:
                max_profit = curr_profit
                max_rotations = r

        if n_customers <= 0:
            return max_rotations

        # 남은 사람들 처리
        # 먼저 4명씩 태우기
        n_full, n_remain = divmod(n_customers, 4)
        curr_profit += (n_full << 2) * boardingCost - n_full * runningCost
        if curr_profit > max_profit:
            max_profit = curr_profit
            max_rotations = len(customers) + n_full

        # 남은 사람들 태우기
        curr_profit += n_remain * boardingCost - runningCost
        if curr_profit > max_profit:
            max_rotations = len(customers) + n_full + 1

        return max_rotations


if __name__ == "__main__":
    test_cases = [
        ([8, 3], 5, 8),  # 3
        ([10, 9, 6], 6, 4),  # 7
        ([3, 4, 0, 5, 1], 1, 92),  # -1
        ([10, 10, 1, 0, 0], 4, 4),  # 5
        ([10, 10, 6, 4, 7], 3, 8),  # 9
    ]

    for c, b, r in test_cases:
        print(">>>", c, b, r)
        answer = Solution().minOperationsMaxProfit(c, b, r)
        print(f"{answer = }")
