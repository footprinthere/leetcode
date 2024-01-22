class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        """ time 98% / space 5% """

        boundaries = set()
        # list of (m, i) - i 위치에서 min이 m으로 갱신됨
        
        # 왼쪽 순회하며 min 갱신되는 지점 기록
        m = nums[k]
        for i in reversed(range(0, k)):
            if nums[i] < m:
                boundaries.add((m, i))
                m = nums[i]
        boundaries.add((m, -1))
        
        # 오른쪽 순회하며 min 갱신되는 지점 기록
        m = nums[k]
        for i in range(k+1, len(nums)):
            if nums[i] < m:
                boundaries.add((m, i))
                m = nums[i]
        boundaries.add((m, len(nums)))

        # 갱신 위치를 m이 큰 것부터 하나씩 검토
        start = k
        end = k
        max_score = nums[k]

        for m, i in sorted(list(boundaries), reverse=True):
            # 왼쪽이면 start, 오른쪽이면 end 업데이트
            if i < k:
                start = i + 1
            else:
                end = i - 1

            # score 계산
            score = m * (end - start + 1)
            if score > max_score:
                max_score = score

        return max_score
    

if __name__ == "__main__":
    # nums = [1,4,3,7,4,5]
    # k = 3

    nums = [5,5,4,5,4,1,1,1]
    k = 0

    answer = Solution().maximumScore(nums, k)
    print(answer)
