from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """ time 79 / space 96 """
        
        s_counter = Counter(s)
        t_counter = Counter(t)

        answer = 0

        for ch, t_count in t_counter.items():
            s_count = s_counter[ch]     # ch not in s이면 0
            
            # 문자 ch가 s에보다 t에 몇 개 더 많이 들어 있는지 계산
            #   -> 그만큼을 부족한 다른 문자로 바꾸면 됨
            if t_count > s_count:
                answer += (t_count - s_count)
        
        return answer
    

if __name__ == "__main__":
    s = "aba"
    t = "bab"

    s = 'leetcode'
    t = 'practice'

    answer = Solution().minSteps(s, t)
    print(answer)
