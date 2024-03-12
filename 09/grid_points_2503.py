from functools import lru_cache


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        """time 98 / space 73"""

        M, N = len(grid), len(grid[0])
        answer = [0] * len(queries)

        # Sort queries to handle the smallest query first
        # Remove trivial queries in the meantime
        sorted_queries = [(q, idx) for idx, q in enumerate(queries) if grid[0][0] < q]
        if len(sorted_queries) == 0:
            return answer
        sorted_queries.sort()

        score = 0
        stacks = [set() for _ in range(len(queries))]
        stacks[sorted_queries[0][1]].add((0, 0))

        visited = [[False] * N for _ in range(M)]
        visited[0][0] = True

        @lru_cache(maxsize=None)
        def _search_query(v: int) -> int:
            """Finds a proper query using binary search, and returns its index"""

            if v >= sorted_queries[-1][0]:
                return -1

            start, end = 0, len(sorted_queries) - 1
            while start < end:
                mid = (start + end) // 2
                if v < sorted_queries[mid][0]:
                    end = mid
                else:
                    start = mid + 1
            return sorted_queries[start][1]

        for q, q_idx in sorted_queries:
            stack = list(stacks[q_idx])
            score += len(stack)

            while stack:
                x, y = stack.pop()

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx = x + dx
                    ny = y + dy
                    if not (0 <= nx < M and 0 <= ny < N) or visited[nx][ny]:
                        continue

                    val = grid[nx][ny]
                    if val >= q:
                        # Cannot reach by now
                        proper_idx = _search_query(val)
                        if proper_idx > -1:
                            visited[nx][ny] = True
                            stacks[proper_idx].add((nx, ny))
                        continue

                    score += 1
                    visited[nx][ny] = True
                    stack.append((nx, ny))

            answer[q_idx] = score

        return answer

    def cumulate_linear(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        """TLE 20 / 21"""

        M, N = len(grid), len(grid[0])
        answer = [0] * len(queries)

        # Sort queries to handle the smallest query first
        # Remove trivial queries in the meantime
        sorted_queries = [(q, idx) for idx, q in enumerate(queries) if grid[0][0] < q]
        sorted_queries.sort()

        score = 0
        visited = [[False] * N for _ in range(M)]
        neighbors = {(0, 0)}
        # Some positions in `neighbor` will be selected to construct a stack in the next iteration

        for q, idx in sorted_queries:

            stack = []
            removed = set()
            for nx, ny in neighbors:
                if grid[nx][ny] < q:
                    score += 1
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    removed.add((nx, ny))
            neighbors = neighbors - removed

            if len(stack) == 0:
                # Cannot reach any neighbors -> Skip to the next query
                answer[idx] = score
                continue

            while stack:
                x, y = stack.pop()

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx = x + dx
                    ny = y + dy
                    if not (0 <= nx < M and 0 <= ny < N) or visited[nx][ny]:
                        continue
                    if grid[nx][ny] >= q:
                        # Cannot reach now, but maybe can in the next iteration
                        neighbors.add((nx, ny))
                        continue

                    score += 1
                    visited[nx][ny] = True
                    stack.append((nx, ny))

            answer[idx] = score

        return answer


def print_grid(grid, visited):
    """For debugging purpose"""

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j]:
                print(f"\033[31m{grid[i][j] :>9}\033[37m", end="")
            else:
                print(f"{grid[i][j] :>9}", end="")
        print()
    print()


if __name__ == "__main__":
    # fmt: off
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]   # [5,8,1]

    grid = [[5,2,1],[1,1,2]]
    queries = [3]   # [0]

    grid = [[123491,95183,131119,576084,779700,886039,564610],[835246,594630,752204,976312,431928,916878,37773],[602559,675,8018,72760,560850,132858,416126],[787316,77587,784798,797907,769783,143785,378185],[362862,754648,212843,813454,552332,10700,266493],[970387,690405,956929,172955,952240,156111,403784],[916537,511212,795823,716447,470772,943050,542971],[449416,742776,952272,447280,190229,354861,256967],[682983,738563,29191,379588,802026,480129,88803],[200621,935415,758897,430413,947532,642396,281230],[11009,169593,224388,165812,668820,197039,370824],[69652,613219,858695,278982,688142,592221,573682],[169510,983952,45500,536012,460040,22352,30370],[80353,162875,946697,861329,680011,716224,528454],[752578,92518,914849,76979,957241,215103,428977],[882979,485485,371229,191577,428367,22769,668112]]
    queries = [581002,174698]   # [4,3]

    answer = Solution().maxPoints(grid, queries)
    print(f"{answer = }")
    # fmt: on
