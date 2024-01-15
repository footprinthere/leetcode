class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        pool: list[tuple[int, int]] = []    # (num, rank)

        for i in range(len(nums)):
            for j, num in enumerate(nums[i]):
                k = i + j
                tri = k * (k + 1) // 2  # 1 + 2 + ... + (i+j)
                
                rank = tri + j
                pool.append((num, rank))

        pool.sort(key=lambda pair: pair[1])
        return [pair[0] for pair in pool]
    

if __name__ == "__main__":
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    # nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    # nums = [[1,2,3,4,5,6]]

    answer = Solution().findDiagonalOrder(nums)

    print(answer)


"""
list에 append 하고 마지막에 sort 하면
* n개를 append -> O(n)
* sort -> O(n logn)

heap을 쓰면
* n개를 append -> O(n logn)
    * list에 append한 후 한번에 heapify 하면 -> O(n)
* sort -> O(n logn)

동일.
"""
