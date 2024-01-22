from typing import Generator


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        """
        3차원 dp 배열을 만드는 셈
        dp[i][j][k] -> robot 1은 [i, j], robot 2는 [i, k]에서 출발할 때 얻을 수 있는 최대 점수
        i = N-1 ... 0으로 역순으로 채우고, 한 row를 채울 때마다 바로 다음 row만 필요하므로 2개 row만 보관

        time 58% / space 92%
        """
        
        M, N = len(grid), len(grid[0])
        self.M, self.N = M, N

        next = [[0] * N for _ in range(N)]  # (N, N)
        curr = [[0] * N for _ in range(N)]

        for i in reversed(range(1, M)):

            for j in range(N):
                for k in range(j, N):
                    if j == k:
                        # 두 로봇이 같은 칸에 있을 때
                        curr[j][k] = grid[i][j]
                    else:
                        curr[j][k] = grid[i][j] + grid[i][k]
                    
                    # 바로 다음 row 중 도달할 수 있는 칸들의 최댓값
                    curr[j][k] += max(next[x][y] for x, y in self._forward((j, k)))

            # 대칭이므로 하삼각 부분은 따로 계산하지 않고 복사
            for j in range(1, N):
                for k in range(j):
                    curr[j][k] = curr[k][j]

            # 이전 row로 이동
            next, curr = curr, next

        # 첫 번째 row에서는 위치가 고정되어 있음
        answer = grid[0][0] + grid[0][N-1] + max(
            next[x][y] for x, y in self._forward((0, N-1))
        )

        return answer


    def _forward(self, pos: tuple[int, int]) -> Generator[tuple[int, int], None, None]:
        return (
            (pos[0] + x, pos[1] + y)
            for x, y in (
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 0), (0, 1),
                (1, -1), (1, 0), (1, 1),
            )
            if 0 <= pos[0] + x < self.N and 0 <= pos[1] + y < self.N
        )


if __name__ == "__main__":
    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]

    # grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]

    # grid = [[4,1,5,7,1],[6,0,4,6,4],[0,9,6,3,5]]

    answer = Solution().cherryPickup(grid)
    print(answer)
