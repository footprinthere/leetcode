class Solution:

    def constructDistancedSequence(self, n: int) -> list[int]:
        """ time 33 / space 56 """
        
        if n == 1:
            return [1]
        
        stack = []  # DFS

        L = 2*n - 1
        seq = [0] * L
        seq[0] = n
        seq[n] = n
        stack.append((1, seq))
        # (다음으로 채워야 할 index, 지금까지 채운 결과)

        while stack:
            idx, seq = stack.pop()

            for num in range(1, n+1):
                if num in seq:
                    continue    # 이미 사용한 수

                if num == 1:
                    copy = [e for e in seq]
                    copy[idx] = 1
                elif idx + num >= L or seq[idx + num] > 0:
                    continue    # 두 번째 자리를 채울 수 없음
                else:
                    copy = [e for e in seq]
                    copy[idx] = num
                    copy[idx + num] = num

                if 0 not in copy:
                    return copy     # 완성

                stack.append((find_empty(copy, idx), copy))

        raise RuntimeError()    # should not reach here


def find_empty(arr: list[int], start: int) -> int:
    """ start 위치부터 시작해 최초로 0이 등장하는 지점을 찾음 """
    idx = start
    while idx < len(arr):
        if arr[idx] == 0:
            break
        idx += 1

    return idx


if __name__ == "__main__":
    
    answer = Solution().constructDistancedSequence(10)
    print(answer)
