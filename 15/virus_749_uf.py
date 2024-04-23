from collections import deque


class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:

        simulator = Simulator(board=isInfected)
        total_walls = 0

        while (n_walls := simulator.step()) is not None:
            total_walls += n_walls

        return total_walls


Region = set[tuple[int, int]]
# 한 번 확산했을 때 감염될 칸들의 좌표만 보관하면 충분함
# block 처리된 region은 empty set으로 표현


class Simulator:
    def __init__(self, board: list[list[int]]):
        self.n_rows = len(board)
        self.n_cols = len(board[0])
        self.n_infected = 0

        # for union-find (-1 for uninfected)
        self.parents = [-1] * (self.n_rows * self.n_cols)
        self.regions: dict[int, Region] = {}

        for x in range(self.n_rows):
            for y in range(self.n_cols):
                if board[x][y] and self.parents[self._key_of(x, y)] == -1:
                    self.add_point(x, y, board)

    def add_point(self, x: int, y: int, board: list[list[int]]) -> None:
        """Adds a new region starting at (x, y)"""

        key = self._key_of(x, y)

        queue = deque([(x, y)])
        visited = {(x, y)}
        size = 0
        region: Region = set()

        while queue:
            qx, qy = queue.popleft()
            size += 1
            self.parents[self._key_of(qx, qy)] = key

            for ap in self._around(qx, qy):
                if ap in visited:
                    continue

                if board[ap[0]][ap[1]]:
                    queue.append(ap)
                    visited.add(ap)
                else:
                    region.add(ap)

        self.n_infected += size
        self.regions[key] = region

    def step(self) -> int | None:
        """
        Blocks the region with the largest impact, and diffuse all other regions
        Returns:
            - how many walls are installed
            - `None` when there are no more regions to block or all cells are infected
        """

        max_key = -1
        max_impact = 0
        keys_to_diffuse = []

        for key, region in self.regions.items():
            if not region:
                continue  # blocked
            if len(region) > max_impact:
                keys_to_diffuse.append(max_key)
                max_key = key
                max_impact = len(region)
            else:
                keys_to_diffuse.append(key)

        if max_key == -1:
            return None  # No regions to block
        n_walls = self.block(max_key)

        # Diffuse
        pairs_to_merge = set()
        for key in keys_to_diffuse[1:]:  # keys_to_diffuse[0] is -1
            pairs_to_merge |= self.diffuse(key)

        # Merge
        for p in pairs_to_merge:
            self._union(*p)

        if self.n_infected >= self.n_rows * self.n_cols:
            # All cells are infected
            # If the program reaches here, this means no regions diffused -- keys_to_diffuse[1:] was empty
            return None
        else:
            return n_walls

    def block(self, root_key: int) -> int:
        """Blocks a region and calculates how many walls are installed"""

        region = self.regions[root_key]
        n_walls = 0

        for x, y in region:
            if self.parents[self._key_of(x, y)] > -1:
                continue  # already infected (this can happen after merger)

            for ax, ay in self._around(x, y):
                if self._parent_of(self._key_of(ax, ay)) == root_key:
                    n_walls += 1

        region.clear()  # block
        return n_walls

    def diffuse(self, root_key: int) -> set[tuple[int, int]]:
        """Diffuse a region and returns pairs of keys that need to be merged"""

        region = self.regions[root_key]
        new_region: Region = set()
        pairs_to_merge = set()

        for x, y in region:
            key = self._key_of(x, y)
            if self.parents[key] > -1:
                continue  # already infected (this can happen after merger)

            # Infect next cells
            self.parents[self._key_of(x, y)] = root_key
            self.n_infected += 1

            # Refill
            for ax, ay in self._around(x, y):
                if (ax, ay) in region:
                    continue
                if (p := self._parent_of(self._key_of(ax, ay))) is None:
                    new_region.add((ax, ay))  # uninfected
                elif p != root_key and self.regions[p]:
                    # touched another unblocked region
                    pairs_to_merge.add((root_key, p))

        self.regions[root_key] = new_region
        return pairs_to_merge

    def _around(self, x: int, y: int):
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < self.n_rows and 0 <= ny < self.n_cols:
                yield (nx, ny)

    def _key_of(self, x: int, y: int) -> int:
        """Generates key used for union-find"""
        return x * self.n_cols + y

    def _parent_of(self, key: int) -> int | None:
        p = self.parents[key]
        if p == -1:
            return None  # not infected
        elif p == key:
            return key
        else:
            self.parents[key] = p = self._parent_of(p)
            return p

    def _union(self, key1: int, key2: int) -> None:
        """Merges 1 into 2"""
        parent1 = self._parent_of(key1)
        parent2 = self._parent_of(key2)
        if parent1 == parent2:
            return  # already merged

        self.parents[parent1] = parent2
        self.regions[parent2] |= self.regions[parent1]
        del self.regions[parent1]


if __name__ == "__main__":
    # fmt: off
    isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
    # 10
    isInfected = [[1,1,1],[1,0,1],[1,1,1]]
    # 4
    isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
    # 13

    isInfected = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    # fmt: on

    answer = Solution().containVirus(isInfected)
    print(f"{answer = }")
