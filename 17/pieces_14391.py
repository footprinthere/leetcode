# https://www.acmicpc.net/problem/14391

from sys import stdin


def main():
    N, _ = [int(tok) for tok in stdin.readline().split()]
    board: list[list[int]] = []
    for _ in range(N):
        board.append([int(e) for e in stdin.readline().strip()])

    solver = Solver(board)
    answer = solver.solve()
    print(answer)


Point = tuple[int, int]
Step = tuple[Point, set[Point], int]
# (next position, visited, total)


class Solver:
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.R = len(board)
        self.C = len(board[0])

    def solve(self) -> int:
        stack: list[Step] = [((0, 0), set(), 0)]
        max_value = 0

        # DFS
        while stack:
            s = stack.pop()
            next_steps = self.step(s)
            if len(next_steps) > 0:
                stack.extend(next_steps)
            else:
                _, _, value = s
                max_value = max(max_value, value)

        return max_value

    def step(self, s: Step) -> list[Step]:
        pos, visited, total = s
        x, y = self.find_next_pos(pos, visited)
        if x == -1:
            return []  # terminated

        output: list[Step] = []

        visited.add((x, y))
        v = self.board[x][y]
        output.append(((x, y), visited, total + v))

        # Down
        nx = x + 1
        new_visited: set[Point] = set()
        value = v
        while nx < self.R and (nx, y) not in visited:
            new_visited.add((nx, y))
            value = value * 10 + self.board[nx][y]
            output.append(((x, y), visited | new_visited, total + value))
            nx += 1

        # Right
        ny = y + 1
        new_visited: set[Point] = set()
        value = v
        while ny < self.C and (x, ny) not in visited:
            new_visited.add((x, ny))
            value = value * 10 + self.board[x][ny]
            output.append(((x, ny), visited | new_visited, total + value))
            ny += 1

        return output

    def find_next_pos(self, start: Point, visited: set[Point]) -> Point:
        """Finds the position to visit next."""

        x, y = start
        while (x, y) in visited:
            if y == self.C - 1:
                if x == self.R - 1:
                    return (-1, -1)
                else:
                    x += 1
                    y = 0
            else:
                y += 1

        return (x, y)


if __name__ == "__main__":
    main()
