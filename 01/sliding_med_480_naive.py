def solution(nums: list[int], k: int) -> list[float]:
    """ time limit exceeded """

    if k % 2 == 0:
        med_func = lambda s: (s[k//2 - 1] + s[k//2]) / 2
    else:
        med_func = lambda s: s[k//2]

    answer = []
    
    start = 0
    while (end := start + k) <= len(nums):
        s = sorted(nums[start : end])
        answer.append(med_func(s))

        start += 1

    return answer


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    answer = solution(nums, k)
    print(answer)
