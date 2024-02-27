from functools import lru_cache


MOD = int(1e9 + 7)


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        """
        memoization 기반 DP
        time 10 / space 87
        """

        low = str(int(low) - 1)
        low_list = [int(d) for d in low]
        high_list = [int(d) for d in high]

        low_count = count(low_list)
        high_count = count(high_list)
        # print("count:", high_count, low_count)

        return (high_count - low_count) % MOD


def count(x: list[int]) -> int:
    x = tuple(x)  # [4, 5, 6, 7]
    output = 0

    # 첫 자리 0
    output += dp(x, length=1, last=-1, less=True)
    # 첫 자리 0 < ... < x[0]
    for d in range(1, x[0]):
        output += dp(x, length=1, last=d, less=True)
    # 첫 자리 x[0]
    if x[0] > 0:
        output += dp(x, length=1, last=x[0], less=False)

    dp.cache_clear()
    return output


@lru_cache(maxsize=None)
def dp(
    x: tuple[int, ...],
    length: int,
    last: int,
    less: bool,
) -> int:
    """
    [1, x] 범위 내의 stepping number 수 계산
    length: 현재까지 build 한 수의 길이
    last: 현재까지 build 한 수의 맨 끝 자리 숫자
        -1이면 leading zero만 있다는 의미
    less: 현재까지 build 한 수가 x보다 작은지의 여부
    """

    if length == len(x):
        # print(f"x={x}, length={length}, last={last}, less={less} -> done (1)")
        return 1

    output = 0

    if last == -1:
        output += dp(x, length + 1, last=-1, less=True)  # 0 하나 더
        for d in range(1, 10):
            output += dp(x, length + 1, last=d, less=True)

        return output % MOD

    for d in (last - 1, last + 1):
        if not (0 <= d < 10):
            continue
        if not less and d > x[length]:
            # 바로 전까지 tie였다가 여기서 초과
            continue
        output += dp(x, length + 1, last=d, less=less or d < x[length])
        output %= MOD

    # print(f"x={x}, length={length}, last={last}, less={less} -> {output}")

    return output


if __name__ == "__main__":
    low, high = "1", "11"
    # low, high = "90", "101"
    # low, high = "2", "40"

    answer = Solution().countSteppingNumbers(low, high)
    print("answer:", answer)
