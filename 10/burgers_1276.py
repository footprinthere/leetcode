class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        """time 96 / space 33"""

        if tomatoSlices % 2 != 0:
            return []

        n_jumbo = (tomatoSlices // 2) - cheeseSlices
        if n_jumbo < 0 or n_jumbo > cheeseSlices:
            return []

        return [n_jumbo, cheeseSlices - n_jumbo]


if __name__ == "__main__":
    test_cases = [
        (16, 7),
        (17, 4),
        (4, 17),
    ]

    for t in test_cases:
        print(t)
        answer = Solution().numOfBurgers(*t)
        print(f"{answer = }")
