DEAD = 0
LIVE = 1
DEAD_TO_LIVE = 2
LIVE_TO_DEAD = 3

AROUND = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """time 21 / space 57"""

        R, C = len(board), len(board[0])

        def _count_around(x: int, y: int) -> int:
            count = 0
            for dx, dy in AROUND:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < R and 0 <= ny < C):
                    continue
                if board[nx][ny] in (LIVE, LIVE_TO_DEAD):
                    count += 1
            return count

        for x in range(R):
            for y in range(C):
                state = board[x][y]
                count = _count_around(x, y)

                if state == LIVE and not (2 <= count <= 3):
                    board[x][y] = LIVE_TO_DEAD  # over/under-population
                elif state == DEAD and count == 3:
                    board[x][y] = DEAD_TO_LIVE  # revive

        for x in range(R):
            for y in range(C):
                state = board[x][y]
                if state == LIVE_TO_DEAD:
                    board[x][y] = DEAD
                elif state == DEAD_TO_LIVE:
                    board[x][y] = LIVE


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    board = [[1, 1], [1, 0]]

    Solution().gameOfLife(board)
    print(*board, sep="\n")
