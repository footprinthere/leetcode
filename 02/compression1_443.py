class Solution:
    def compress(self, chars: list[str]) -> int:
        """ in-place로 압축하고 그 길이 반환 """

        read_idx, write_idx = 0, 0
        prev_char = ""
        count = 0
        
        while read_idx < len(chars):
            new_char = chars[read_idx]
            if new_char == prev_char:
                # 반복되는 문자 출현
                count += 1
                read_idx += 1
                continue

            # 다른 문자 출현
            # 1. 이전 문자의 count 기록
            if count > 1:
                count_str = list(str(count))
                chars[write_idx : write_idx + len(count_str)] = count_str
                write_idx += len(count_str)

            # 2. 새로운 문자 기록
            chars[write_idx] = new_char
            write_idx += 1
            prev_char = new_char
            count = 1

            read_idx += 1

        # 마지막에 count 기록
        if count > 1:
            count_str = list(str(count))
            chars[write_idx : write_idx + len(count_str)] = count_str
            write_idx += len(count_str)

        return write_idx


if __name__ == "__main__":
    chars = list("aabbbcccc")
    answer = Solution().compress(chars)

    print(answer)
    print(chars[:answer])
