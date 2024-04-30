from copy import deepcopy


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """time 90 / space 93"""

        R, C = len(board), len(board[0])
        AROUND = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        copy = deepcopy(board)

        def _count_around(x: int, y: int) -> int:
            count = 0
            for dx, dy in AROUND:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < R and 0 <= ny < C):
                    continue
                if copy[nx][ny]:
                    count += 1
            return count

        for x in range(R):
            for y in range(C):
                count = _count_around(x, y)
                if not (2 <= count <= 3):
                    board[x][y] = 0  # die
                elif count == 3:
                    board[x][y] = 1  # live on or revive


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    board = [[1, 1], [1, 0]]

    Solution().gameOfLife(board)
    print(*board, sep="\n")
