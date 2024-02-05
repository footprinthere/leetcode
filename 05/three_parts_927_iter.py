class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        """ TLE 110 / 121 """
        
        self.init_arr(arr)

        j = len(arr) - 1

        for j in reversed(range(2, len(arr))):
            # j-1번째와 마지막 값이 같아야 함
            if arr[j - 1] != arr[-1]:
                continue

            # 두 번째 [...j-1]과, 세 번째 [j : -1]가 일치하는지 확인
            min_length = Solution.truncated_length(arr[j:])     # 먼저 세 번째에서 0을 떼어내고
            max_i = j - min_length - 1                          # 그 길이만큼 두 번째를 잡음

            if max_i < 0:
                break
            if not self.are_equivalent((max_i + 1, j), (j, len(arr))):
                continue

            # 이제 i를 잡아야 함
            # 먼저 max_i 기준으로 비교 한 번
            if arr[max_i] == arr[-1] and self.are_equivalent((0, max_i + 1), (j, len(arr))):
                # 성공
                return [max_i, j]

            # i를 하나씩 줄이면서 비교
            for i in reversed(range(max_i)):
                # 만약 1이 새로 추가된다면, 두 번째의 값이 바뀌어버리므로 더 볼 필요 없음
                if arr[i+1] == 1:
                    break
                # i번째와 마지막 값이 같아야 함
                if arr[i] != arr[-1]:
                    continue

                # 값 비교
                if not self.are_equivalent((0, i+1), (j, len(arr))):
                    continue

                # 성공
                return [i, j]
        
        # 실패
        return [-1, -1]
    
    def init_arr(self, arr: list[int]):
        self.arr = arr
        self.length = len(arr)

        # arr을 2진수로 평가
        self.num = arr[-1]  
        shift = 0
        for digit in reversed(arr[:-1]):
            shift += 1
            self.num += digit << shift

    def are_equivalent(self, p1: tuple[int, int], p2: tuple[int, int]) -> bool:
        """ num을 binary로 표현했을 때 구간 p1와 p2가 동일한지 검사 """
        n1 = self.slice_bin(self.length - p1[1], self.length - p1[0])
        n2 = self.slice_bin(self.length - p2[1], self.length - p2[0])
        return n1 == n2

    def slice_bin(self, lower: int, upper: int) -> int:
        """ num을 binary로 표현한 후 2^start(inc) ~ 2^end(exc) 부분만 eval """
        output = self.num & ((1 << upper) - 1)
        output >>= lower
        return output
    
    @staticmethod
    def truncated_length(arr: list[int]) -> int:
        """
        앞쪽에 붙어 있는 0들을 제거하고 남는 길이 반환
        전부 0이어도 1을 반환
        """
        for i, n in enumerate(arr):
            if n > 0:
                return len(arr) - i
        return 1
    

def make_test_case(s: str) -> list[int]:
    return list(map(int, list(s)))


if __name__ == "__main__":
    # arr = [1,0,1,0,1]
    # arr = [1,1,0,1,1]
    # arr = [1,1,0,0,1]
    # arr = make_test_case("001100001111")
    arr = [0, 0, 0, 0, 0]

    answer = Solution().threeEqualParts(arr)
    print(arr, answer)
