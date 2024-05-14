# https://www.acmicpc.net/problem/19949

# FIXME: WRONG ANSWER

from sys import stdin


def main():
    answers = [int(tok) - 1 for tok in stdin.readline().split()]
    N = len(answers)

    dp = [[[0] * 6 for _ in range(N + 1)] for __ in range(N)]
    # N x (N+1) x 6
    # dp[n][s][c] : n번 답으로 c를 고르면서 1...n번 누적 s점을 얻는 경우의 수
    # dp[n][s][-1] = sum_c(0...4) dp[n][s][c]

    def _compute(no: int, score: int, choice: int) -> int:
        is_correct = answers[no] == choice
        if no == 0:
            if (is_correct and score == 1) or (not is_correct and score == 0):
                return 1
            else:
                return 0

        # 이제 n >= 1
        # 1. n-1번에 choice와 다른 답을 쓰거나
        # 2. n-1번에는 같은 답을 쓰고 n-2번에는 다른 답을 쓰면 됨
        #     -> n-1번에 같은 답 쓴 경우 중 n-2번에도 같은 답 쓴 경우 빼기

        target_score = score - 1 if is_correct else score
        if target_score < 0:
            return 0
        output = dp[no - 1][target_score][-1]
        if no == 1:
            return output

        if choice == answers[no - 1]:
            target_score -= 1
            if target_score < 0:
                return output
        output -= dp[no - 2][target_score][choice]
        return output

    for n in range(N):
        for s in range(N + 1):
            total = 0

            for c in range(5):
                v = _compute(n, s, c)
                dp[n][s][c] = v
                total += v

            dp[n][s][-1] = total

    answer = sum(dp[-1][s][-1] for s in range(5, N + 1))  # 5점 이상
    print(answer)


if __name__ == "__main__":
    main()
