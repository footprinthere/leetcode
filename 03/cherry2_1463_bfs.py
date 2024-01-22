from collections import deque
from itertools import product


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        """ 10/59에서 시간 초과 """
        
        # BFS
        # 두 robot의 움직임이 서로 독립적이지 않으므로 함께 다뤄야 함
        queue = deque([(
            (0, 0),
            (0, len(grid[0]) - 1),
            grid[0][0] + grid[0][-1],
        )])

        def _forward(pos: tuple[int, int]) -> list[tuple[int, int]]:
            # (1,-1) (1,0) (1,1)
            return [
                (pos[0] + 1, pos[1] + c) for c in (-1, 0, 1)
                if 0 <= pos[1] + c < len(grid[0])
            ]

        while queue and queue[0][0][0] < len(grid) - 1:
            pos1, pos2, score = queue.popleft()

            for next1, next2 in product(_forward(pos1), _forward(pos2)):
                if next1 == next2:
                    next_score = score + grid[next1[0]][next1[1]]
                else:
                    next_score = score + grid[next1[0]][next1[1]] + grid[next2[0]][next2[1]]
                queue.append((next1, next2, next_score))

        # 이제 마지막 row에 도달했음
        return max(x[2] for x in queue)
    

if __name__ == "__main__":
    # grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]

    grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]

    answer = Solution().cherryPickup(grid)
    print(answer)
