class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """ time 17 / space 97 """
        
        answer = 0

        max_num = max(max(nums), k)
        mask = 1
        shift = 0

        while mask <= max_num:      # 모든 자릿수를 다 본 후 종료
            parity_sum = sum((n & mask) >> shift for n in nums)
            if (parity_sum & 1) != ((k & mask) >> shift):
                # 1이 홀수 개인데 0이 나와야 하거나 그 반대이면 operation 필요
                answer += 1

            # shift
            mask <<= 1
            shift += 1

        return answer
    

if __name__ == "__main__":
    nums = [2, 1, 3, 4]
    k = 1

    nums = [3,5,1,1]
    k = 19

    answer = Solution().minOperations(nums, k)
    print(answer)
