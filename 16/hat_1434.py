from typing import Generator
from functools import lru_cache


class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        """time 6 / space 61"""

        N = len(hats)
        MAX_HAT = max(max(h) for h in hats)

        @lru_cache(maxsize=None)
        def _dp(people_mask: BitMask.BitMask, curr_hat: int) -> int:
            """
            people_mask: 각 사람들이 모자를 할당받았는지의 여부
            curr_hat: 지금 씌우려는 모자의 번호
            """

            if curr_hat > MAX_HAT:
                if BitMask.all(people_mask, length=N):
                    return 1
                else:
                    return 0

            output = _dp(people_mask, curr_hat + 1)

            for p_idx, (p_hats, is_allocated) in enumerate(
                zip(hats, BitMask.iter(people_mask, length=N))
            ):
                if is_allocated or curr_hat not in p_hats:
                    continue
                output += _dp(BitMask.set(people_mask, p_idx), curr_hat + 1)

            return output

        return _dp(BitMask.EMPTY_MASK, 1) % (10**9 + 7)


class BitMask:
    BitMask = int
    EMPTY_MASK: BitMask = 0

    @staticmethod
    def iter(bit_mask: BitMask, length: int) -> Generator[BitMask, None, None]:
        for _ in range(length):
            yield bit_mask & 1
            bit_mask >>= 1

    @staticmethod
    def all(bit_mask: BitMask, length: int) -> bool:
        return bit_mask == 2**length - 1

    @staticmethod
    def set(bit_mask: BitMask, idx: int) -> BitMask:
        return bit_mask | (1 << idx)


if __name__ == "__main__":
    hats = [[3, 5, 1], [3, 5]]
    hats = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

    answer = Solution().numberWays(hats)
    print(f"{answer = }")
