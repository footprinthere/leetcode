from collections import deque


TILES = [
    None,
    ((0, 1), (0, -1)),
    ((1, 0), (-1, 0)),
    ((1, 0), (0, -1)),
    ((1, 0), (0, 1)),
    ((-1, 0), (0, -1)),
    ((-1, 0), (0, 1)),
]

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        """
        Solution 참고했음
        time 89 / space 76
        """

        R = len(grid)
        C = len(grid[0])
        
        queue = deque([(0, 0)])
        visited = {(0, 0)}

        while queue:
            x, y = queue.popleft()
            if x == R-1 and y == C-1:
                # 도착
                return True
            
            for dx, dy in TILES[grid[x][y]]:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < R and 0 <= ny < C             # 범위 안에 들고
                    and (nx, ny) not in visited             # 아직 가본 적 없고
                    and (-dx, -dy) in TILES[grid[nx][ny]]   # 길이 통하면 <- 이게 핵심 아이디어!
                ):
                    queue.append((nx, ny))
                    visited.add((nx, ny))

        return False
            

if __name__ == "__main__":
    # grid = [[2,4,3],[6,5,2]]
    # grid = [[1,2,1],[1,2,1]]
    # grid = [[1,1,2]]
    # grid = [[4,1],[6,1]]
    # grid = [[1]]
    # grid = [[4,3,3],[6,5,2]]    # loop
    grid = [[4,1,3],[6,1,2]]

    answer = Solution().hasValidPath(grid)
    print(answer)
    