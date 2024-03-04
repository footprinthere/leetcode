from collections import Counter
import math


class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        """TLE 40 / 101"""

        # Count characters in target and stickers
        target_counter = Counter(target)
        target_combi = []
        ch_idx_map = {}
        for i, (ch, count) in enumerate(target_counter.items()):
            target_combi.append(count)
            ch_idx_map[ch] = i
        _print(f"{ch_idx_map = }")

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
        # (지금 볼 스티커의 index, 지금까지 쓴 sticker 수, 지금까지 남은 count)
        answer = INIT = 100

        while stack:
            idx, n_stickers, curr_combi = stack.pop()
            # _print(f"{idx = }, {n_stickers = }, {curr_combi = }")
            if all(c == 0 for c in curr_combi):
                answer = min(answer, n_stickers)
                continue
            if idx >= len(sticker_combi_list):
                continue  # already checked all stickers
            if n_stickers >= answer:
                continue  # already found a better solution

            stack.append((idx + 1, n_stickers, curr_combi))  # not using this sticker
            sticker_combi = sticker_combi_list[idx]
            _print(f"\t{sticker_combi = }")

            demand = max_demand(curr_combi, sticker_combi)
            _print(f"\t{demand = }")
            subtracted = curr_combi
            for n in range(1, demand + 1):
                subtracted = [
                    c - s if c > s else 0 for c, s in zip(subtracted, sticker_combi)
                ]
                stack.append((idx + 1, n_stickers + n, subtracted))

        if answer == INIT:
            return -1
        else:
            return answer


def max_demand(target: list[int], sticker: list[int]) -> int:
    """target의 count를 채우기 위해 sticker가 최대 몇 개 필요한지 계산"""

    output = 0
    for t, s in zip(target, sticker):
        if t == 0 or s == 0:
            continue
        output = max(output, math.ceil(t / s))

    return output


def _print(*args, **kwargs):
    print(*args, **kwargs)
    pass


if __name__ == "__main__":
    stickers = ["with", "example", "science"]
    target = "thehat"

    # stickers = ["notice", "possible"]
    # target = "basicbasic"

    stickers = ["these", "guess", "about", "garden", "him"]
    target = "atomher"

    stickers = ["fly", "me", "charge", "mind", "bottom"]
    target = "centorder"

    answer = Solution().minStickers(stickers, target)
    print(f"{answer = }")
