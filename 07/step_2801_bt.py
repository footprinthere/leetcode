class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        """
        Partially uses DP
        TLE 2402
        """

        low = str(int(low) - 1)
        low_list = list(map(int, low))
        high_list = list(map(int, high))

        low_len = len(low_list)
        high_len = len(high_list)

        if low_len < high_len:
            row_sums = make_dp_table(max_len=high_len - 1)
            # print("row_sums:", row_sums)
            count = row_sums[high_len - 2]
            if low_len > 1:
                count -= row_sums[low_len - 2]
        else:
            count = 0

        count += count_same_digits(high_list) - count_same_digits(low_list)
        return count

    def back_tracking(self, low: str, high: str) -> int:
        """
        Back tracking
        TLE 2402 / 2523
        """

        low_list = list(map(int, low))  # "123" -> [1, 2, 3]
        high_list = list(map(int, high))

        max_len = len(high_list)
        low_list = [0] * (max_len - len(low_list)) + low_list  # zero-padded

        stack = [[i] for i in range(10)]  # [0, ...] ~ [9]
        count = 0

        while stack:
            arr = stack.pop()

            arr_len = len(arr)
            if not (low_list[:arr_len] <= arr <= high_list[:arr_len]):
                # out of range
                continue
            if len(arr) == max_len:
                # success
                count += 1
                continue

            # Add next digit
            last = arr[-1]
            if last == 0:
                if all(d == 0 for d in arr):
                    # only leading zeros
                    for i in range(10):
                        stack.append(arr + [i])
                else:
                    stack.append(arr + [1])
            elif last == 9:
                stack.append(arr + [8])
            else:
                stack.append(arr + [last - 1])
                stack.append(arr + [last + 1])

        return count


def make_dp_table(max_len: int) -> list[int]:
    """
    Makes table of shape (max_len, 10).
    table[i][j] = # of stepping numbers with i+1 digits, ending with j

    Returns list of "prefix sums" of sum of each row.
    """

    table = [[1] * 10 for _ in range(max_len)]
    table[0][0] = 0
    # table[0][0] = 0 / table[0][...] = 1

    for i in range(1, max_len):
        table[i][0] = table[i - 1][1]
        table[i][9] = table[i - 1][8]
        for j in range(1, 9):
            table[i][j] = table[i - 1][j - 1] + table[i - 1][j + 1]

    # print("table")
    # print(*table, sep="\n")

    row_sums = [sum(table[i]) for i in range(max_len)]
    for i in range(1, max_len):
        row_sums[i] = row_sums[i] + row_sums[i - 1]

    return row_sums


def count_same_digits(x: list[int]) -> int:
    """
    Counts stepping numbers no larger than x,
    with as many digits as x.
    Uses back-tracking.
    """

    stack = [[i] for i in range(1, 10)]  # [1] ~ [9]
    count = 0

    while stack:
        arr = stack.pop()
        arr_len = len(arr)

        if not (arr <= x[:arr_len]):
            # out of range
            continue
        if len(arr) == len(x):
            # success
            count += 1
            continue

        # Add next digit
        last = arr[-1]
        if last == 0:
            stack.append(arr + [1])
        elif last == 9:
            stack.append(arr + [8])
        else:
            stack.append(arr + [last - 1])
            stack.append(arr + [last + 1])

    # print(f"count {x} -> {count}")
    return count


if __name__ == "__main__":
    low, high = "1", "11"
    # low, high = "90", "101"

    answer = Solution().countSteppingNumbers(low, high)
    print("answer:", answer)
