import bisect


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        """time 91 / space 14"""

        # Collect fibonacci numbers smaller than k
        fibs = [1, 1]
        while (f := fibs[-2] + fibs[-1]) <= k:
            fibs.append(f)

        end = len(fibs) - 1
        target = k
        count = 0

        while target > 0:
            # Greedy; end = arg max_i {fibs[i] <= target}
            end = bisect.bisect_right(fibs, target, hi=end + 1) - 1

            target -= fibs[end]
            count += 1

        return count


if __name__ == "__main__":
    k = 7
    k = 19

    answer = Solution().findMinFibonacciNumbers(k)
    print(f"{answer = }")
