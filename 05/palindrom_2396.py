from collections import deque


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        """ time 63% / space 58% """
        for b in range(2, n-2 + 1):
            converted = convert_base(n, b)
            if not is_palindrom(converted):
                return False
            
        return True


def convert_base(n: int, base: int) -> list[int]:
    numbers = deque()

    while n >= base:
        n, r = divmod(base, n)
        numbers.appendleft(r)
    numbers.appendleft(n)

    return numbers


def is_palindrom(numbers: list[int]) -> bool:
    start, end = 0, len(numbers) - 1

    while start <= end:
        if numbers[start] != numbers[end]:
            return False
        start += 1
        end -= 1

    return True
