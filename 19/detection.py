# https://www.acmicpc.net/problem/21938

from sys import stdin


def main():
    N, M = [int(t) for t in stdin.readline().split()]
    input_image: list[list[int]] = []
    for _ in range(N):
        input_image.append([int(t) for t in stdin.readline().split()])
    T = int(stdin.readline().strip())

    image: list[list[bool]] = []
    for row in input_image:
        averaged: list[bool] = []
        for i in range(0, len(row), 3):
            averaged.append((row[i] + row[i + 1] + row[i + 2]) / 3 >= T)
        image.append(averaged)

    n_objects = 0
    visited = [[False] * M for _ in range(N)]

    def _dfs(x: int, y: int) -> None:
        stack = [(x, y)]
        visited[x][y] = True

        while stack:
            sx, sy = stack.pop()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx = sx + dx
                ny = sy + dy
                if (
                    not (0 <= nx < N and 0 <= ny < M)
                    or not image[nx][ny]
                    or visited[nx][ny]
                ):
                    continue

                stack.append((nx, ny))
                visited[nx][ny] = True

    for x in range(N):
        for y in range(M):
            if image[x][y] and not visited[x][y]:
                _dfs(x, y)
                n_objects += 1

    print(n_objects)


if __name__ == "__main__":
    main()
