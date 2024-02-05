# 진행 방향
FORWARD = 0
BACKWARD = 1
BLOCKED = -1

# 타일 종류
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# tile_type = TILE_TYPE[tile][dir]
TILE_TYPE: list[dict[int, int]] = [
    None,
    {FORWARD: RIGHT, BACKWARD: LEFT},   # 1: 우
    {FORWARD: DOWN, BACKWARD: UP},      # 2: 하
    {FORWARD: DOWN, BACKWARD: LEFT},    # 3: 우하
    {FORWARD: DOWN, BACKWARD: RIGHT},   # 4: 좌하
    {FORWARD: LEFT, BACKWARD: UP},      # 5: 하좌
    {FORWARD: RIGHT, BACKWARD: UP},     # 6: 하우
]
# move = MOVE[tile_type]
MOVE: dict[int, tuple[int, int]] = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1),
}
# dir = NEXT_DIR[tile_type][tile]
NEXT_DIR: dict[int, list[int]] = {
    UP: [None, BLOCKED, BACKWARD, BACKWARD, BACKWARD, BLOCKED, BLOCKED],
    DOWN: [None, BLOCKED, FORWARD, BLOCKED, BLOCKED, FORWARD, FORWARD],
    LEFT: [None, BACKWARD, BLOCKED, BLOCKED, FORWARD, BLOCKED, BACKWARD],
    RIGHT: [None, FORWARD, BLOCKED, FORWARD, BLOCKED, BACKWARD, BLOCKED],
}
 

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        """ TLE 79/80 """

        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0])
        
        # 첫 번째 칸
        tile_type = grid[0][0]

        if tile_type in (1, 2, 3, 6):
            return self.start(FORWARD)
        elif tile_type == 4:
            return self.start(FORWARD) or self.start(BACKWARD)
        else:
            return False
            
    def start(self, dir: int) -> bool:

        been = [[False] * self.C for _ in range(self.R)]    # 이미 가본 칸에 true 표시

        x, y = 0, 0
        next_tile = self.grid[x][y]
        been[x][y] = True

        while True:
            if x == self.R - 1 and y == self.C - 1:
                # 도착
                return True
            
            tile = next_tile
            tile_type = TILE_TYPE[tile][dir]

            move = MOVE[tile_type]
            x += move[0]
            y += move[1]

            print(f"tile {tile}, tile type {tile_type}, move {move}")

            print(f"x {x} y {y} / dir {dir}")

            if not ((0 <= x < self.R) and (0 <= y < self.C)):
                # 범위 초과
                return False
            
            next_tile = self.grid[x][y]
            if been[x][y]:
                # loop
                return False
            dir = NEXT_DIR[tile_type][next_tile]
            been[x][y] = True

            print(f"\ttile {next_tile}, dir {dir}")

            if dir == BLOCKED:
                # 진행 불가
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
    