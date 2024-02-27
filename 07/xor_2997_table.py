class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """ time 5 / space 6 """
        
        nums_bin = [convert_bin(n) for n in nums]
        k_bin = convert_bin(k)

        print("numsbin")
        print(*nums_bin, sep="\n")

        # zero padding
        max_len = max(max(len(b) for b in nums_bin), len(k_bin))
        for i in range(len(nums_bin)):
            nums_bin[i] = [0] * (max_len - len(nums_bin[i])) + nums_bin[i]
        k_bin = [0] * (max_len - len(k_bin)) + k_bin

        print("pad")
        print(*nums_bin, sep="\n")

        # transpose
        nums_bin_t = list(zip(*nums_bin))

        print("transpose")
        print(*nums_bin_t, sep="\n")

        answer = 0
        for col, k_digit in zip(nums_bin_t, k_bin):
            # 1이 홀수 개인데 0이 나와야 하거나 그 반대이면 operation 필요
            print(f"col {col} (par {sum(col) & 1}) vs k {k_digit}")
            if sum(col) & 1 != k_digit:
                answer += 1

        return answer


def convert_bin(n: list) -> list[int]:
    """
    정수를 bit 배열로 변환
    e.g. 6 -> [1, 1, 0]
    """

    result = []

    while n > 0:
        result.insert(0, n & 1)
        n >>= 1

    return result


if __name__ == "__main__":
    nums = [2, 1, 3, 4]
    k = 1

    nums = [3,5,1,1]
    k = 19

    answer = Solution().minOperations(nums, k)
    print(answer)
