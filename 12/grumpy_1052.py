class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        """
        Sliding Window
        time 87 / space 91 (with big variance)
        """

        satisfied = 0  # grumpy 하지 않은 날의 합
        added = 0  # 기회를 써서 추가로 얻을 수 있는 합
        # 굳이 변수 두 개 따로 둘 필요 없음

        for i, c in enumerate(customers[:minutes]):
            if grumpy[i]:
                added += c
            else:
                satisfied += c

        max_added = added

        for i, c in enumerate(customers[minutes:], start=minutes):
            if grumpy[i]:
                added += c
            else:
                satisfied += c

            if grumpy[i - minutes]:
                added -= customers[i - minutes]
            max_added = max(max_added, added)

        return satisfied + max_added


if __name__ == "__main__":
    # fmt: off
    customers = [1,0,1,2,1,1,7,5]
    grumpy =    [0,1,0,1,0,1,0,1]
    minutes = 3     # 16

    customers = [1]
    grumpy = [0]
    minutes = 1     # 1

    customers = [4,10,10]
    grumpy =    [1, 1, 0]
    minutes = 2     # 24
    # fmt: on

    answer = Solution().maxSatisfied(customers, grumpy, minutes)
    print(f"{answer = }")
