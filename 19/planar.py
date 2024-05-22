# https://www.acmicpc.net/problem/1917

from sys import stdin
from dataclasses import dataclass
from enum import Enum


SIX = 6


def main():
    for _ in range(3):
        figure: list[list[int]] = []
        for __ in range(SIX):
            figure.append([int(t) for t in stdin.readline().split()])

        solve(figure)


def solve(figure: list[list[int]]):
    cube = Cube()

    x, y = find_first_one(figure)
    stack = [((x, y), cube.get_default_state())]
    visited = {(x, y)}
    cube.covered[0] = True

    def _is_valid_one(_x: int, _y: int) -> bool:
        # In range & Not visited
        return (
            (0 <= _x < SIX and 0 <= _y < SIX)
            and figure[_x][_y] == 1
            and (_x, _y) not in visited
        )

    # DFS
    while stack:
        (x, y), cube_state = stack.pop()

        for dx, dy, dir in (
            (-1, 0, Dir.UP),
            (0, -1, Dir.LEFT),
            (1, 0, Dir.DOWN),
            (0, 1, Dir.RIGHT),
        ):
            nx = x + dx
            ny = y + dy
            if not _is_valid_one(nx, ny):
                continue

            rotated = cube_state.rotated(dir)
            if not rotated.cover_front():
                print("no")  # already covered
                return

            stack.append(((nx, ny), rotated))
            visited.add((nx, ny))

    if all(cube.covered):
        print("yes")
    else:
        print("no")


def find_first_one(figure: list[list[int]]) -> tuple[int, int]:
    for i, row in enumerate(figure):
        for j, n in enumerate(row):
            if n == 1:
                return (i, j)
    raise ValueError("No 1 found")


@dataclass(frozen=True)
class Face:
    num: int
    links: list["Face"]  # counter-clockwise
    link_nums: list[int]


class Cube:

    faces: list[Face] = [Face(n, [], []) for n in range(SIX)]
    _class_initialized = False

    def __init__(self):
        if not Cube._class_initialized:
            #   4
            # 0 1 2 3
            #   5
            Cube._link_faces(0, [4, 3, 5, 1])  # counter-clockwise
            Cube._link_faces(1, [4, 0, 5, 2])
            Cube._link_faces(2, [4, 1, 5, 3])
            Cube._link_faces(3, [4, 2, 5, 0])
            Cube._link_faces(4, [2, 3, 0, 1])
            Cube._link_faces(5, [0, 3, 2, 1])
            Cube._class_initialized = True

        self.covered = [False] * SIX

    def get_default_state(self) -> "CubeState":
        return CubeState(cube=self)

    @classmethod
    def _link_faces(cls, idx: int, link_nums: list[int]):
        cls.faces[idx].links[:] = [cls.faces[i] for i in link_nums]
        cls.faces[idx].link_nums[:] = link_nums


class Dir(int, Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


class CubeState:
    """cube의 어느 면을 어떤 방향으로 보고 있는지를 표현"""

    def __init__(self, cube: Cube):
        self._cube = cube
        self._front_num = 0  # [0, 6)
        self._upside_edge = 0  # [0, 4)

    def rotated(self, dir: Dir) -> "CubeState":
        copy = self._copy()

        # 회전 후 새로운 앞면 결정
        link_idx = (dir + copy._upside_edge) % 4
        new_front = Cube.faces[copy._front_num].links[link_idx]

        # 기존의 앞면과 어떻게 연결되어 있는지 보고 upside edge 결정
        new_link_idx = new_front.link_nums.index(copy._front_num)
        copy._upside_edge = (new_link_idx - (dir + 2)) % 4

        copy._front_num = new_front.num
        return copy

    def cover_front(self) -> bool:
        if self._cube.covered[self._front_num]:
            return False  # already covered
        else:
            self._cube.covered[self._front_num] = True
            return True

    def _copy(self) -> "CubeState":
        new = CubeState(self._cube)
        new._front_num = self._front_num
        new._upside_edge = self._upside_edge
        return new


if __name__ == "__main__":
    main()
