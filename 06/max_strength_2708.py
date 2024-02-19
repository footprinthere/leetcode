class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        """ time 65 / space 63 """

        # 곱이 양수가 나오게 하려면 음수를 짝수 개 골라야 함
        # 양수/음수 분리
        pos, neg = [], []
        for n in nums:
            if n > 0:
                pos.append(n)
            elif n < 0:
                neg.append(n)

        # 양수가 없고 음수가 없거나 하나뿐이면 -- 이렇게 처리하는 거 좀 지저분한가?
        if len(pos) == 0:
            if len(neg) == 0:
                return 0
            elif len(neg) == 1:
                if 0 in nums:
                    return 0
                else:
                    return neg[0]

        # 양수는 다 골라야 함
        prod = 1
        for n in pos:
            prod *= n

        # 음수는 절댓값 큰 것부터 짝수 개만 골라야 함
        neg.sort(reverse=True)
        while len(neg) >= 2:
            prod *= neg.pop()
            prod *= neg.pop()

        return prod
