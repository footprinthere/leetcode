# https://www.acmicpc.net/problem/16236

from typing import Generator
from sys import stdin
from collections import defaultdict, deque


def main():
    N = int(stdin.readline().strip())
    board = [[int(t) for t in stdin.readline().split()] for _ in range(N)]
    simulator = Simulator(board)
    
    print(simulator.solve())


Point = tuple[int, int]


class Simulator:
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.N = len(board)

        self.curr_pos = (-1, -1)
        self.curr_size = 2
        self.gauge = 0
        self.time = 0

        for x in range(self.N):
            for y in range(self.N):
                k = self.board[x][y]
                if k == 9:
                    self.curr_pos = (x, y)
                    self.board[x][y] = 0

    def solve(self) -> int:
        while (target := self._find_target()) is not None:
            (tx, ty), dist = target
            self.time += dist
            self._update_gauge()

            self.curr_pos = (tx, ty)
            self.board[tx][ty] = -1  # mark eaten

        return self.time

    def _find_target(self) -> tuple[Point, int] | None:
        """Finds the nearest edible fish"""
        dist = 1
        q = deque([self.curr_pos])  # BFS
        visited = {self.curr_pos}

        while True:
            q_next = deque()
            candidates: list[Point] = []

            while q:
                qx, qy = q.popleft()
                for (ax, ay), k in self._around(qx, qy):
                    if (ax, ay) in visited:
                        continue
                    else:
                        visited.add((ax, ay))

                    if 0 < k < self.curr_size:
                        candidates.append((ax, ay))
                    else:
                        q_next.append((ax, ay))

            if candidates:
                return min(candidates), dist
            if not q_next:
                return None  # not found

            dist += 1
            q = q_next

    def _around(self, x: int, y: int) -> Generator[tuple[Point, int], None, None]:
        """Generates neighboring available positions"""
        for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):  # U L R D
            nx, ny = x + dx, y + dy
            if not (0 <= nx < self.N and 0 <= ny < self.N):
                continue
            k = self.board[nx][ny]
            if k <= self.curr_size:  # including eaten (-1)
                yield (nx, ny), k

    def _update_gauge(self):
        """Updates the size of the shark"""
        self.gauge += 1
        if self.gauge == self.curr_size:
            self.curr_size += 1
            self.gauge = 0


if __name__ == "__main__":
    main()
