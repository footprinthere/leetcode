# Solution에서 아이디어 얻었음

from collections import Counter


class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        """TLE 98 / 101"""

        # Count characters in target and stickers
        target_counter = Counter(target)
        target_combi: list[int] = []
        ch_idx_map: dict[str, int] = {}

        for i, (ch, count) in enumerate(target_counter.items()):
            target_combi.append(count)
            ch_idx_map[ch] = i
        _print(f"{target_combi = }, {ch_idx_map = }")

        sticker_combi_list = []
        for sticker in stickers:
            combi = [0] * len(target_combi)
            for ch in sticker:
                if ch in ch_idx_map:
                    # Only count characters in target
                    combi[ch_idx_map[ch]] += 1
            _print(f"{sticker = }, {combi = }")
            sticker_combi_list.append(combi)

        # Back-tracking
        stack = [(0, 0, [t for t in target_combi])]
        # (지금 볼 문자의 index, 지금까지 쓴 sticker 수, 지금까지 남은 count)
        answer = INIT = 100

        while stack:
            ch_idx, n_stickers, curr_combi = stack.pop()
            _print(f"{ch_idx = }, {n_stickers = }, {curr_combi = }")

            if all(c <= 0 for c in curr_combi):
                answer = min(answer, n_stickers)
                continue  # 성공
            elif ch_idx >= len(target_combi):
                continue  # 모든 문자 봤으나 실패
            elif n_stickers >= answer:
                continue  # 이미 더 좋은 답 있음
            elif curr_combi[ch_idx] <= 0:
                stack.append((ch_idx + 1, n_stickers, curr_combi))
                continue  # 더 필요 없는 문자

            for sticker_combi in sticker_combi_list:
                if sticker_combi[ch_idx] == 0:
                    continue  # 필요한 문자 갖고 있지 않음
                new_combi = [c - s for c, s in zip(curr_combi, sticker_combi)]
                stack.append((ch_idx, n_stickers + 1, new_combi))

        if answer == INIT:
            return -1
        else:
            return answer


def _print(*args, **kwargs):
    print(*args, **kwargs)
    pass


if __name__ == "__main__":
    # stickers = ["with", "example", "science"]
    # target = "thehat"

    # stickers = ["notice", "possible"]
    # target = "basicbasic"

    # stickers = ["these", "guess", "about", "garden", "him"]
    # target = "atomher"

    stickers = ["fly", "me", "charge", "mind", "bottom"]
    target = "centorder"

    answer = Solution().minStickers(stickers, target)
    print(f"{answer = }")
