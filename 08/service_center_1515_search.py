# Solutions 참고했음

import math


class Solution:
    def getMinDistSum(self, positions: list[list[int]]) -> float:
        """time 43 / space 65"""

        # Trivial cases
        L = len(positions)
        if L == 1:
            return 0.0
        elif L == 2:
            return dist(positions[0], positions[1])

        # Initialize with mean values
        sum_x, sum_y = 0, 0
        for pos in positions:
            sum_x += pos[0]
            sum_y += pos[1]
        cx = sum_x / L
        cy = sum_y / L

        answer = loss((cx, cy), positions)
        step_size = 50

        while step_size > 1e-7:
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                # 상하좌우를 탐색하고, 더 좋은 지점이 없으면 step_size를 좁힘
                _x = cx + step_size * dx
                _y = cy + step_size * dy

                l = loss((_x, _y), positions)
                if l < answer:
                    answer = l
                    cx, cy = _x, _y
                    break

            else:
                # No better positions found
                step_size /= 2

        return answer


def loss(center, positions: list[int]) -> float:
    return sum(dist(center, pos) for pos in positions)


def dist(p1: list[int], p2: list[int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


if __name__ == "__main__":
    # positions = [[0, 1], [1, 0], [1, 2], [2, 1]]
    positions = [[1, 1], [0, 0], [2, 0]]

    answer = Solution().getMinDistSum(positions)
    print(f"{answer = }")
