# https://www.acmicpc.net/problem/5212

from sys import stdin


def main():
    R, C = [int(tok) for tok in stdin.readline().split()]
    board: list[list[str]] = []
    for _ in range(R):
        board.append(list(stdin.readline().strip()))

    # Diffusion
    def _is_surrounded(x: int, y: int) -> bool:
        count = 0
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            if (
                not (0 <= (nx := x + dx) < R and 0 <= (ny := y + dy) < C)
                or board[nx][ny] == "."
            ):
                count += 1
                if count >= 3:
                    return True
        return False

    new_board = [["."] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] == ".":
                continue
            if not _is_surrounded(x, y):
                new_board[x][y] = "X"

    # Trim
    trim_row(new_board)
    transpose = list(zip(*new_board))
    trim_row(transpose)
    answer = list(zip(*transpose))

    for row in answer:
        print("".join(row))


def trim_row(board: list[list[str]]) -> None:
    while len(board) > 0 and all(e == "." for e in board[0]):
        del board[0]
    while len(board) > 0 and all(e == "." for e in board[-1]):
        del board[-1]


if __name__ == "__main__":
    main()
