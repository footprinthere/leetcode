class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """ time 83% / space 5% """

        # 길이가 홀수이면 불가능
        if len(s) % 2 != 0:
            return False
        
        unlocked, left = [], []

        for i, (ch, l) in enumerate(zip(s, locked)):
            # unlocked이거나 '('이면 stack에 추가
            if l == "0":
                unlocked.append(i)
                continue
            elif ch == "(":
                left.append(i)
                continue

            # locked ')'일 때
            # stack 안에 '('나 unlocked가 있으면 함께 제거 가능
            # 없으면 실패
            if left:
                left.pop()
            elif unlocked:
                unlocked.pop()
            else:
                return False
            
        # 이제 unlocked로 left를 전부 상쇄할 수 있으면 성공
        i_unlocked, i_left = 0, 0
        while True:
            if i_left >= len(left):
                # 전부 상쇄됨
                return True
            elif i_unlocked >= len(unlocked):
                # 더 이상 unlocked가 남아 있지 않음
                return False
            
            if unlocked[i_unlocked] > left[i_left]:
                # left보다 뒤에 unlocked가 있으면 상쇄 가능
                i_left += 1

            i_unlocked += 1


if __name__ == "__main__":
    # s = "))()))"
    # locked = "010100"

    # s = ")("
    # locked = "00"

    s =      "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
    locked = "100011110110011011010111100111011101111110000101001101001111"

    for i, (ch, l) in enumerate(zip(s, locked)):
        print(f"{'0' if l == '0' else ch} ", end="")
        if i % 10 == 9:
            print()

    answer = Solution().canBeValid(s, locked)
    print(answer)
