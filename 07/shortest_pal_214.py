class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """ TLE 120 / 123 """
        
        # 첫 번째 char와 일치하는 것을 뒤에서부터 찾음 (lazy)
        candidates = (
            j for j in reversed(range(1, len(s)))
            if s[j] == s[0]
        )

        for end in candidates:
            i, j = 0, end
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1

            # FIXME: palindrom을 깨는 char가 가운데쪽에 있으면 매번 불필요하게 양끝에서 가운데까지 이르느라 오래 걸림

            # palindrom found
            if i >= j:
                break
        
        else:
            # palindrom not found
            end = 0

        # Now [0, end] is the longtest palindrom substring
        return "".join(reversed(s[end+1:])) + s
    

if __name__ == "__main__":
    s = "aacecaaa"
    # s = "abcd"
    # s = "cacacacba"
    s = "a" * 20000 + "cd" + "a" * 20000

    answer = Solution().shortestPalindrome(s)
    print(answer)

    from collections import Counter
    print(Counter(answer))
