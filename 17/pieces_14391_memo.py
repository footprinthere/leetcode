# https://www.acmicpc.net/problem/14391

from functools import lru_cache
from sys import stdin


Board = list[list[int]]
Point = tuple[int, int]
BitMask = int


def main():
    N, _ = [int(tok) for tok in stdin.readline().split()]
    board: Board = []
    for _ in range(N):
        board.append([int(e) for e in stdin.readline().strip()])

    solver = Solver(board)
    answer = solver.solve()
    print(answer)


class Solver:
    def __init__(self, board: Board):
        self.board = board
        self.R = len(board)
        self.C = len(board[0])
        self.FULL_MASK = (1 << (self.R * self.C)) - 1

    @lru_cache(maxsize=None)
    def solve(self, mask: BitMask = 0) -> int:
        if mask == self.FULL_MASK:
            return 0  # terminated

        x, y = self.find_next_pos(mask)
        mask = self.bm_set(mask, x, y)
        v = self.board[x][y]
        output = v + self.solve(mask)

        # Down
        nx = x + 1
        new_mask = mask
        value = v
        while nx < self.R and not self.bm_get(mask, nx, y):
            new_mask = self.bm_set(new_mask, nx, y)
            value = value * 10 + self.board[nx][y]
            output = max(output, value + self.solve(new_mask))
            nx += 1

        # Right
        ny = y + 1
        new_mask = mask
        value = v
        while ny < self.C and not self.bm_get(mask, x, ny):
            new_mask = self.bm_set(new_mask, x, ny)
            value = value * 10 + self.board[x][ny]
            output = max(output, value + self.solve(new_mask))
            ny += 1

        return output

    def find_next_pos(self, mask: BitMask) -> Point:
        for idx in range(self.R * self.C):
            if not Solver._bm_get(mask, idx):
                return (idx // self.C, idx % self.C)

        raise ValueError("No available position found")

    def bm_set(self, mask: BitMask, x: int, y: int) -> BitMask:
        return mask | (1 << self._pos_to_idx(x, y))

    def bm_get(self, mask: BitMask, x: int, y: int) -> bool:
        return Solver._bm_get(mask, self._pos_to_idx(x, y))

    def _pos_to_idx(self, x: int, y: int) -> int:
        return x * self.C + y

    @staticmethod
    def _bm_get(mask: BitMask, idx: int) -> bool:
        return bool((mask >> idx) & 1)


if __name__ == "__main__":
    main()
