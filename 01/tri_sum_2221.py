def solution(nums: list[int]) -> int:
    N = len(nums) - 1
    if N <= 0:
        return nums[0]
    
    sum = 0
    for i, n in enumerate(nums):
        sum += choose(N, i) * n
    
    print(sum)
    return sum % 10
    

def choose(n, r):
    p, q = 1, 1
    for j in range(n-r+1, n+1):
        p *= j
    for i in range(2, r+1):
        q *= i
    
    assert p % q == 0
    return p // q


if __name__ == "__main__":
    solution([1, 2, 3, 4, 5])
