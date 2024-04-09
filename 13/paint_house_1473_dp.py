from functools import lru_cache


class Solution:
    def minCost(
        self,
        houses: list[int],
        cost_table: list[list[int]],
        n_houses: int,
        n_colors: int,
        target: int,
    ) -> int:
        """time 85 / space 58"""

        LIMIT = 10000000

        @lru_cache(maxsize=None)
        def _dp(idx: int, color: int, n_neighbors: int) -> int:
            """
            house[idx] = color로 칠하면서
            house[: idx+1]를 n_neighbors개 그룹으로 나누는 최소 비용
            """

            if idx < 0:
                return 0  # padding
            if idx + 1 < n_neighbors:
                return LIMIT  # impossible

            if houses[idx] > 0:
                if houses[idx] != color:
                    return LIMIT  # impossible
                else:
                    add_cost = 0  # already painted
            else:
                add_cost = cost_table[idx][color - 1]

            min_cost = _dp(idx - 1, color, n_neighbors)  # 직전 칸과 같은 색으로
            if n_neighbors == 1:
                return min_cost + add_cost

            for c in range(1, n_colors + 1):
                if c == color:
                    continue
                cost = _dp(idx - 1, c, n_neighbors - 1)  # 직전 칸과 다른 색으로
                min_cost = min(cost, min_cost)

            return min_cost + add_cost

        min_cost = min(
            _dp(idx=n_houses - 1, color=c, n_neighbors=target)
            for c in range(1, n_colors + 1)
        )
        if min_cost < LIMIT:
            return min_cost
        else:
            return -1


if __name__ == "__main__":
    # fmt: off
    houses = [0,0,0,0,0]; cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]; m = 5; n = 2; target = 3 #9
    houses = [0,2,1,2,0]; cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]; m = 5; n = 2; target = 3 #11

    houses = [2,2,1]; cost = [[1,1],[3,4],[4,2]]; m=3; n=2; target=2 #0
    houses = [3,1,2,3]; cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]; m=4; n=3; target=3 #-1

    houses = [0,0,0,1]; cost = [[1,5],[4,1],[1,3],[4,4]]; m=4; n=2; target=4 #12
    # fmt: on

    answer = Solution().minCost(houses, cost, m, n, target)
    print(f"{answer = }")
