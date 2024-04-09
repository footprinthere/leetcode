class Solution:
    def minCost(
        self,
        houses: list[int],
        cost: list[list[int]],
        n_houses: int,
        n_colors: int,
        target: int,
    ) -> int:
        """TLE 9 / 62"""

        min_cost = float("inf")

        count = count_neighbors(houses)
        next_idx = find_zero_idx(houses)
        if next_idx < 0:
            # no houses to paint
            if count == target:
                return 0
            else:
                return -1
        stack = [(houses, next_idx, count, 0)]

        while stack:
            curr, idx, count, curr_cost = stack.pop()

            next_idx = find_zero_idx(curr, start=idx + 1)
            left = (
                find_nonzero_item(curr, start=idx - 1, reverse=True) if idx > 0 else 0
            )
            right = find_nonzero_item(curr, start=idx + 1) if idx < n_houses - 1 else 0

            for c in range(1, n_colors + 1):
                # Compare color with neighboring houses
                next_count = count
                if left != c and c != right:
                    if left == right:
                        if left > 0:
                            next_count += 2  # (A, _, A) -> (A, B, A)
                        else:
                            next_count += 1  # (0, _, 0) -> (0, B, 0)
                    else:
                        next_count += 1  # (A, _, C) -> (A, B, C)
                if next_count > target:
                    continue

                # Check current cost
                next_cost = curr_cost + cost[idx][c - 1]
                if next_cost >= min_cost:
                    continue

                if next_idx >= n_houses or next_idx == -1:
                    # Painting completed
                    if next_count == target and next_cost < min_cost:
                        min_cost = next_cost
                    continue

                copy = [e for e in curr]
                copy[idx] = c
                stack.append((copy, next_idx, next_count, next_cost))

        return min_cost if min_cost < float("inf") else -1


def find_zero_idx(arr: list[int], start: int = 0) -> int:
    """Finds the first zero starting from `start`"""

    for i, n in enumerate(arr[start:], start=start):
        if n == 0:
            return i
    return -1


def find_nonzero_item(arr: list[int], start: int = 0, reverse: bool = False) -> int:
    step = 1 if not reverse else -1
    i = start
    while 0 <= i < len(arr):
        if (n := arr[i]) > 0:
            return n
        i += step
    return 0


def count_neighbors(houses: list[int]) -> int:
    if len(houses) == 1:
        return 1 if houses[0] > 0 else 0

    count = 0
    prev = -1

    for c in houses:
        if c > 0 and c != prev:
            count += 1
            prev = c
    return count


if __name__ == "__main__":
    # fmt: off
    houses = [0,0,0,0,0]; cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]; m = 5; n = 2; target = 3 #9
    houses = [0,2,1,2,0]; cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]; m = 5; n = 2; target = 3 #11

    houses = [2,2,1]; cost = [[1,1],[3,4],[4,2]]; m=3; n=2; target=2 #0
    houses = [3,1,2,3]; cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]; m=4; n=3; target=3 #-1
    # fmt: on

    answer = Solution().minCost(houses, cost, m, n, target)
    print(f"{answer = }")
