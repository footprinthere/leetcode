class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:

        L = len(word)
        idx = k
        count = 1

        while idx < len(word):
            if word[: L - idx] == word[idx:]:
                break
            idx += k
            count += 1

        return count


if __name__ == "__main__":
    word = "abacaba"
    k = 3
    k = 4

    answer = Solution().minimumTimeToInitialState(word, k)
    print(f"{answer = }")
