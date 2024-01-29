class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        WRONG
        한번 scan 후 stack 내에서 이웃한 것들끼리 match 시도

        stack 내에서의 match를 linear 하게 할 수 없음 (이웃한 것들끼리만 보면 안 됨)
        """
        
        stack = []
        # list of (i, ch)

        # scan
        for i, ch in enumerate(s):
            if len(stack) > 0 and stack[-1][1] == "(" and ch == ")":
                stack.pop()
            else:
                stack.append((i, ch))
        
        # remove matchable items
        t = 0
        while t < len(stack):
            if locked[stack[t][0]] == "1":
                # 수정 불가능
                t += 1

            elif stack[t][1] == "(" and t > 0 and (locked[stack[t-1][0]] == "0" or stack[t-1][1] == "("):
                # 수정 가능한 (가 있고 직전에 ( 또는 수정 가능한 것이 있으면 match
                stack.pop(t-1)
                stack.pop(t-1)
            elif stack[t][1] == ")" and t < len(stack) - 1 and (locked[stack[t+1][0]] == "0" or stack[t+1][1] == ")"):
                # 수정 가능한 )가 있고 직후에 ) 또는 수정 가능한 것이 있으면 match
                stack.pop(t)
                stack.pop(t)
            else:
                t += 1

        print(stack)

        return len(stack) == 0


if __name__ == "__main__":
    # s = "))()))"
    # locked = "010100"

    s = ")("
    locked = "00"

    answer = Solution().canBeValid(s, locked)
    print(answer)
