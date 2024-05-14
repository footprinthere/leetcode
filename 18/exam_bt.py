# https://www.acmicpc.net/problem/19949

# FIXME: wrong answer

from sys import stdin


def main():
    answers = [int(tok) for tok in stdin.readline().split()]
    N = len(answers)

    stack: list[tuple[int, int, int, int, list[int]]] = [(0, 0, 0, 0, [])]
    # (볼 문제 번호, 직전 문제 답, 연속 같은 답 개수, 점수)
    count = 0

    while stack:
        idx, prev_choice, consec, score, acc = stack.pop()

        if idx == N:
            if score >= 5:
                count += 1  # success
                # print(acc)
            continue

        for choice in range(1, 5 + 1):
            if choice == prev_choice:
                if consec >= 2:
                    continue
                next_consec = consec + 1
            else:
                next_consec = consec

            next_score = score + 1 if choice == answers[idx] else score
            stack.append((idx + 1, choice, next_consec, next_score, acc + [choice]))

    print(count)


if __name__ == "__main__":
    main()
