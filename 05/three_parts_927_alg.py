from typing import Optional
import math


class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        """ time 5 / space 79 """

        num = eval_bin(arr)
        
        third = 0
        shift = -1
        j = len(arr)
        valid_length = 0    # 앞에 붙는 0을 제외한 유효 길이

        while j >= 2:
            # next
            shift += 1
            j -= 1

            # 마지막 자리 합산 후 제거
            digit = num & 1
            if digit == 1:
                valid_length = len(arr) - j
            third += digit << shift
            num >>= 1

            # third = 0이라면 전부 0이어야 함
            if third == 0:
                if num == 0:
                    return [0, j]
                else:
                    continue
            
            # (num - third) = third * Q + R 에서
            # Q = 2^k 이고 R=0 이어야 함
            q, r = divmod(num - third, third)
            if (
                r == 0                              # 나누어떨어져야 함
                and q > 0                           # 몫이 0이면 안 됨
                and (log_q := log(q)) is not None   # Q = 2^k
                and log_q >= valid_length           # 동일한 배열이 다른 위쪽 자리수에서 나타나야 함
            ):
                return [j - int(log_q) - 1, j]
        
        # 실패
        return [-1, -1]

def eval_bin(arr: list[int]) -> int:
    """ binary array의 값 평가 """
    output = 0
    shift = 0
    for digit in reversed(arr):
        output += digit << shift
        shift += 1
    
    return output


def log(num: int) -> Optional[int]:
    """
    num = 2^k이면 k 반환, 그렇지 않으면 None 반환
    math.log2()를 그냥 사용하면 precision 문제가 있음
    """
    output = math.log2(num)
    truc = int(output)
    if output == truc and num == (1 << truc):
        return truc
    else:
        return None


def make_test_case(s: str) -> list[int]:
    return list(map(int, list(s)))

if __name__ == "__main__":
    test_cases = [
        # [1,0,1,0,1],
        # [1,1,0,1,1],
        [1,1,0,0,1],
        # make_test_case("001100001111"),
        # [0, 0, 0, 0, 0],
        # [1, 0, 1, 1, 0],

        [1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                                                                                                                                                                                                                                                                                                                                                                         1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
    
    for arr in test_cases:
        answer = Solution().threeEqualParts(arr)
        print(arr, answer)
