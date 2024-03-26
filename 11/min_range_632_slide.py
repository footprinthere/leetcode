from collections import deque


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        """time 5 / space 12"""

        K = len(nums)
        # if K == 1:
        #     # Trivial case
        #     return [nums[0][0], nums[0][0]]

        pool = []
        for idx, sublist in enumerate(nums):
            for n in sublist:
                pool.append((n, idx))
        pool.sort()

        min_a, min_b = -100000, 100000

        start, end = 0, K - 1
        while end < len(pool):

            # 커버된 list의 index들
            indices = deque([pool[i][1] for i in range(start, end)])
            covered = set(indices)

            # K개 모두 커버될 때까지 end를 뒤로 밀기
            while end < len(pool) and len(covered) < K:
                idx = pool[end][1]
                indices.append(idx)
                covered.add(pool[end][1])
                end += 1
            if len(covered) < K:
                break

            # 이제 [start : end]가 K개를 모두 커버함
            # 앞에서부터 불필요한 것 제거해 구간 줄이기
            while True:
                head = indices.popleft()
                if head not in indices:
                    break  # 제거 불가능
                start += 1

            a, b = pool[start][0], pool[end - 1][0]
            if (b - a) < (min_b - min_a) or ((b - a) == (min_b - min_a) and a < min_a):
                min_a, min_b = a, b

            start += 1

        return [min_a, min_b]


if __name__ == "__main__":
    # fmt: off
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]  # [20, 24]
    # nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]  # [1, 1]
    # nums = [[1, 3, 5, 6]]   # [1, 1]
    # nums = [[3, 4, 6, 8], [2, 4, 7, 9]]     # [4, 4]
    nums = [[1,4,7,10,13],[2,5,8,11,13],[3,6,9,12]] # [12, 13]
    # fmt: on

    answer = Solution().smallestRange(nums)
    print(f"{answer = }")
