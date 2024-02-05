from collections import deque


class Solution:
    count = 0

    def constructDistancedSequence(self, n: int) -> list[int]:
        answer = self.dfs(n)
        print("pop count:", Solution.count)
        return answer
    
    def dfs(self, n: int) -> list[int]:
        """
        n부터 거꾸로 채우되, DFS 사용하고 이미 찾은 정답보다 작은 건 바로 폐기
        """

        if n == 1:
            return [1]

        largest = [0]
        stack = []

        # n 채우기
        L = 2*n - 1
        seq = [0] * L
        seq[0] = n
        seq[n] = n
        stack.append((n-1, seq))

        while stack:
            num, seq = stack.pop()
            print(num, seq)
            Solution.count += 1

            # 끝
            if num == 1:
                Solution.fill_one(seq)
                largest = seq
                continue

            # 채우기
            for i in reversed(range(L - num)):
                if not (seq[i] == 0 and seq[i + num] == 0):
                    continue

                copy = [e for e in seq]
                copy[i] = num
                copy[i + num] = num
                if copy > largest:
                    stack.append((num-1, copy))

            num -= 1

        return largest

    def naive(self, n: int) -> list[int]:
        """ Memory Limit Exceeded 9/20 """
        
        largest = [0]
        queue: deque[tuple[int, list[int]]] = deque()
        # (마지막으로 채운 수, 지금까지 채운 결과)

        # 1 처리
        L = 2 * n - 1
        for i in range(L):
            seq = [0] * L
            seq[i] = 1
            queue.append((1, seq))

        while queue:
            num, seq = queue.popleft()
            Solution.count += 1

            # 끝
            if num == n:
                if largest < seq:
                    largest = seq
                continue

            # 채우기
            num += 1
            for i in range(L - num):
                if seq[i] == 0 and seq[i + num] == 0:
                    copy = [e for e in seq]
                    copy[i] = num
                    copy[i + num] = num
                    queue.append((num, copy))

        return largest

    def reverse(self, n: int) -> list[int]:
        """
        n부터 거꾸로 채우기
        TLE 12/20
        """

        largest = [0]
        queue: deque[tuple[int, list[int]]] = deque()

        # n 채우기 (항상 0번째 & n번째)
        L = 2*n - 1
        seq = [0] * L
        seq[0] = n
        seq[n] = n
        queue.append((n-1, seq))
        # (다음으로 채울 수, 지금까지 채운 결과)

        while queue:
            num, seq = queue.popleft()
            Solution.count += 1

            # 끝
            if num == 1:
                Solution.fill_one(seq)
                if largest < seq:
                    largest = seq
                continue

            # 채우기
            for i in range(L - num):
                if not (seq[i] == 0 and seq[i + num] == 0):
                    continue
                copy = [e for e in seq]
                copy[i] = num
                copy[i + num] = num
                queue.append((num-1, copy))

            num -= 1

        return largest
                

    @staticmethod
    def fill_one(seq: list[int]):
        for i, n in enumerate(seq):
            if n == 0:
                seq[i] = 1
                return


if __name__ == "__main__":
    
    answer = Solution().constructDistancedSequence(7)
    print(answer)
