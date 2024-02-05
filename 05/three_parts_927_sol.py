class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        """ solution 참고했음; time 37 / space 85 """

        count_ones = sum(arr)
        
        if count_ones % 3 != 0:
            # 1의 개수가 3의 배수가 아니면 실패
            return [-1, -1]
        elif count_ones == 0:
            # 1이 없으면 성공
            return [0, len(arr)-1]
        
        
        k = count_ones // 3     # 각 part에 들어 있어야 하는 1의 개수

        # 0k+1번째, 1k+1번째, 2k+1번째 1의 위치를 찾음
        c = 0
        i = 0
        parts = [-1, -1, -1]

        for t in range(3):
            while c < t * k + 1:
                if arr[i] == 1:
                    c += 1
                i += 1
            parts[t] = i

        # 거기서 출발해서 세 부분이 동일한지 비교
        while parts[2] < len(arr) and len({arr[i] for i in parts}) == 1:
            parts = list(map(lambda x: x+1, parts))

        if parts[2] == len(arr):
            return [parts[0]-1, parts[1]]
        else:
            return [-1, -1]


def make_test_case(s: str) -> list[int]:
    return list(map(int, list(s)))

if __name__ == "__main__":
    test_cases = [
        [1,0,1,0,1],
        # [1,1,0,1,1],
        # [1,1,0,0,1],
        # make_test_case("001100001111"),
        [0, 0, 0, 0, 0],
        # [1, 0, 1, 1, 0],

        # [1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0],
        # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        #                                                                                                                                                                                                                                                                                                                                                                                  1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
    
    for arr in test_cases:
        answer = Solution().threeEqualParts(arr)
        print(arr, answer)