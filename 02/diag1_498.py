from typing import Generator


class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        answer = [
            mat[x][y] for x, y in diag_coordinates(len(mat), len(mat[0]))
        ]
         
        return answer


def diag_coordinates(m: int, n: int) -> Generator[tuple[int, int], None, None]:
    x, y = 0, 0
    up = True

    while True:
        yield x, y

        if x == m-1 and y == n-1:
            break
        
        # up -> down 전환
        if y == n-1 and up:
            up = False
            x += 1
        elif x == 0 and up:
            up = False
            y += 1
        # down -> up 전환
        elif x == m-1 and not up:
            up = True
            y += 1
        elif y == 0 and not up:
            up = True
            x += 1
        # up 진행
        elif up:
            x -= 1
            y += 1
        # down 진행
        else:
            x += 1
            y -= 1


if __name__ == "__main__":
    mat = [[1,2],[3,4]]
    answer = Solution().findDiagonalOrder(mat)

    print(answer)
