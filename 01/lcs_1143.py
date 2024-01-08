def solution1(text1: str, text2: str) -> int:
    """ WRONG """
    N, M = len(text1), len(text2)
    table = [[0]*M for _ in range(N)]

    # Fill in first row and column
    count = 0
    for i in range(N):
        if text1[i] == text2[0]:
            count += 1
        table[i][0] = count
    
    count = 0
    for j in range(M):
        if text1[0] == text2[j]:
            count += 1
        table[0][j] = count

    # Fill in the rest
    for i in range(1, N):
        for j in range(1, M):
            if text1[i] == text2[j]:
                table[i][j] = max(table[i-1][j], table[i][j-1], table[i-1][j-1] + 1)
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1], table[i-1][j-1])

    print(*table, sep='\n')
    
    return table[-1][-1]


def solution2(text1: str, text2: str) -> int:
    N, M = len(text1), len(text2)
    table = [[0]*(M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            if text1[i-1] == text2[j-1]:
                table[i][j] = max(table[i-1][j], table[i][j-1], table[i-1][j-1] + 1)
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1], table[i-1][j-1])

    print(*table, sep='\n')
    
    return table[-1][-1]


if __name__ == "__main__":
    print(solution2("aaaaaa", "aaa"))
