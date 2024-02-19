from math import gcd


class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        """ time 94 / space 58 """

        answer = []
        for denom in range(1, n + 1):
            for nom in range(1, denom):
                if gcd(nom, denom) == 1:
                    answer.append(f"{nom}/{denom}")

        return answer

    def with_set(self, n: int) -> list[int]:
        """
        Solution 보니 이렇게 푼 사람이 있더라
        91 / 51
        """

        answer = []
        visited = set()

        for denom in range(1, n + 1):
            for nom in range(1, denom):
                q = nom / denom
                if q not in visited:
                    visited.add(q)
                    answer.append(f"{nom}/{denom}")

        return answer


if __name__ == "__main__":
    answer = Solution().simplifiedFractions(3)
    print(answer)
