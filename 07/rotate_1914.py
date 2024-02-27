from typing import Generator


class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """time 8 / space 50"""

        n_rows = len(grid)
        n_cols = len(grid[0])
        n_layers = min(n_rows, n_cols) // 2

        result = [[0] * n_cols for _ in range(n_rows)]

        for layer in range(n_layers):
            start = (layer, layer)

            length = 2 * (n_rows + n_cols) - 4 - 8 * layer
            n_steps = k % length

            for x, y in cycle(start, layer, n_rows, n_cols):
                nx, ny = forward((x, y), n_steps, layer, n_rows, n_cols)
                result[nx][ny] = grid[x][y]

        return result


def forward(
    start: tuple[int, int],
    n_steps: int,
    layer: int,
    n_rows: int,
    n_cols: int,
) -> tuple[int, int]:
    """`cycle`로부터 `n_steps+1`번 generate"""

    gen = cycle(start, layer, n_rows, n_cols, infinite=True)
    for _ in range(n_steps + 1):
        x, y = next(gen)
    return x, y


def cycle(
    start: tuple[int, int],
    layer: int,
    n_rows: int,
    n_cols: int,
    infinite: bool = False,
) -> Generator[tuple[int, int], None, None]:
    """start 출발해 한 바퀴. infinite=True이면 무한반복."""

    x, y = start

    while True:
        yield x, y

        if y == layer:  # 왼쪽 col
            if x == n_rows - layer - 1:
                y += 1
            else:
                x += 1
        elif y == n_cols - layer - 1:  # 오른쪽 col
            if x == layer:
                y -= 1
            else:
                x -= 1
        elif x == layer:  # 위쪽 row
            y -= 1
        else:  # 아래쪽 row
            y += 1

        if not infinite and (x, y) == start:
            break


if __name__ == "__main__":
    grid = [[40, 10], [30, 20]]
    k = 1

    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    k = 2

    answer = Solution().rotateGrid(grid, k)
    print(*answer, sep="\n")
