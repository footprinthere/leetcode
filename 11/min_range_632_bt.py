class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        """TLE 86 / 90"""

        K = len(nums)
        if K == 1:
            # Trivial case
            return [nums[0][0], nums[0][0]]

        pool = []
        for idx, sublist in enumerate(nums):
            for n in sublist:
                pool.append((n, idx))
        P = len(pool)
        pool.sort()

        memo = [[None] * P for _ in range(P)]

        def _get_coverage(s: int, e: int) -> list[bool]:
            """각 집단의 수가 포함되었는지 여부를 나타내는 길이 K의 list 반환"""

            if (m := memo[s][e]) is not None:
                return m

            if e - s + 1 <= K:
                # Base case
                result = [False] * K
                for i in range(s, e + 1):
                    result[pool[i][1]] = True
            else:
                # Recursion
                result = _get_coverage(s, e - 1)
                result[pool[e][1]] = True

            memo[s][e] = result
            return result

        min_range = (-100000, 100000)

        for size in range(K, P + 1):
            start = 0
            while (end := start + size - 1) < P:
                curr_range = (pool[start][0], pool[end][0])
                if compare_range(curr_range, min_range) and all(
                    _get_coverage(start, end)
                ):
                    min_range = curr_range
                start += 1

        return list(min_range)


def compare_range(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    """r1이 r2보다 작으면 True 반환"""

    a, b = r1
    c, d = r2
    if (b - a) < (d - c):
        return True
    elif (b - a) == (d - c) and a < c:
        return True
    else:
        return False


if __name__ == "__main__":
    # fmt: off
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]  # [20, 24]
    # nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]  # [1, 1]
    # nums = [[1, 3, 5, 6]]   # [1, 1]
    # nums = [[3, 4, 6, 8], [2, 4, 7, 9]]     # [4, 4]
    # fmt: on

    answer = Solution().smallestRange(nums)
    print(f"{answer = }")


"""
[IDEA]
* (start, end, included) 가지고 탐색
    - included = [False] * len(nums)로 초기화한 후 포함되는 것이 생기면 True로 표시
    - 모두 True가 되면 종료
* start, end는 수 대신 pool 내의 index로 충분할 것

* 초기에 start=0...len(pool)-3 반복하며 stack에 넣고 시작해야 하나?
* 전혀 가능성 없는 값을 아예 탐색하지 않으려면 어떻게 해야 할까?
"""
