class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        """time 97 / space 15"""

        if x > y:
            x, y = y, x  # now x <= y
        A = x - 1
        B = y - x + 1
        C = n - y
        # 1 - ... - x - ... - y - ... - n
        # (  A   ) (     B     ) (  C   )

        answer = [0] * n

        def _add(result: list[int], mul: int = 1):
            for i in range(min(n, len(result))):
                answer[i] += result[i] * mul

        # A 또는 C 내부에서
        # 이때는 x와 y도 포함해서 셈
        _add(decreasing(start=A))  # A
        _add(decreasing(start=C))  # C

        # B 내부에서
        temp = decreasing(start=B - 1)
        _add(fold_half(temp, threshold=B))

        # A와 B 간에, 또는 C와 B 간에
        # x 또는 y에서 B 안의 다른 점에 이르는 거리
        temp = fold_half([1] * (B - 1), threshold=B)
        for _ in range(min(A, C)):
            temp = [0] + temp
            _add(temp, mul=2)
        for _ in range(abs(A - C)):
            temp = [0] + temp
            _add(temp)

        # A와 C 간에
        bridge = 3 if x != y else 2
        for a in range(A):
            for c in range(C):
                # d = (A-1 - a) + bridge + (C-1 - c)
                answer[A + C - a - c + bridge - 3] += 1

        return [2 * k for k in answer]


def decreasing(start: int) -> list[int]:
    return [k for k in reversed(range(1, start + 1))]


def fold_half(arr: list[int], threshold: int) -> list[int]:
    """threshold의 절반보다 멀면 뒤로 돌아가는 게 더 빠름"""

    result = [0] * len(arr)
    for i in range(len(arr)):
        if i > threshold:
            break

        if i + 1 > threshold // 2:
            j = threshold - i - 2
        else:
            j = i
        result[j] += arr[i]

    return result


if __name__ == "__main__":

    # n, x, y = 3, 1, 3
    # n, x, y = 5, 2, 4
    n, x, y = 4, 1, 1

    # n, x, y = 5, 1, 5  # [10, 10, 0, 0, 0]
    # n, x, y = 3, 3, 1  # [6, 0, 0]
    n, x, y = 3, 2, 2  # [4, 2, 0]

    # n, x, y = 7, 2, 6

    answer = Solution().countOfPairs(n, x, y)
    print(f"{answer = }, {sum(answer) = }")
