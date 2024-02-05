class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """ time 92 / space 45 """
        self.dividers = sorted((a, b, c))
        return self.search(target=n, start=1, end=int(2e9))

    def search(self, target: int, start: int, end: int) -> int:
        """
        binary search 이용해 [start, end] 사이에서 target을 찾음
        여기서는 target-1에서 target에서 최초로 바뀌는 지점을 찾아야 함 -> 중단 없이 끝까지 가야 함
        """
        # found
        if start == end:
            return start
        
        # divide
        pivot = (start + end) // 2
        if self.count_below(pivot) >= target:
            return self.search(target, start, pivot)
        else:
            return self.search(target, pivot + 1, end)
    
    def count_below(self, k: int) -> int:
        """ k 이하의 수 중 ugly number가 몇 개인지 셈 (inclusion-exclusion) """
        count = 0

        # 1개
        for d in self.dividers:
            count += k // d
        
        # 2개
        count -= k // lcm2(self.dividers[0], self.dividers[1])
        count -= k // lcm2(self.dividers[1], self.dividers[2])
        count -= k // lcm2(self.dividers[0], self.dividers[2])

        # 3개
        count += k // lcm3(*self.dividers)

        return count


def gcd(a: int, b: int) -> int:
    """
    Euclidean algorithm
    항상 a <= b임을 보장해야 함
    """
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm2(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


def lcm3(a: int, b: int, c: int) -> int:
    l = lcm2(b, c)
    if a > l:
        a, l = l, a
    return lcm2(a, l)
    

if __name__ == "__main__":
    # n, a, b, c = 4, 2, 3, 4
    n, a, b, c = 5, 2, 3, 3

    answer = Solution().nthUglyNumber(n, a, b, c)
    print(answer)
