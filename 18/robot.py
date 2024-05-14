# https://www.acmicpc.net/problem/2174

from sys import stdin
from typing import Generator


def main():
    W, H = map(int, stdin.readline().split())
    simulator = Simulator(W, H)

    n_robots, n_commands = map(int, stdin.readline().split())
    for _ in range(n_robots):
        simulator.add_robot(stdin.readline().strip())

    for _ in range(n_commands):
        ok = simulator.run_command(stdin.readline().strip())
        if not ok:
            print(simulator.result_message)
            return

    print("OK")


Point = tuple[int, int]


class Simulator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.robots: list[Robot] = [0]  # 1-indexed
        self.position_map: dict[Point, int] = {}
        # {position : robot index}
        self.result_message = ""

    def add_robot(self, info: str) -> None:
        robot = Robot(number=len(self.robots), info=info)
        self.position_map[robot.pos] = robot.number
        self.robots.append(robot)

    def run_command(self, command: str) -> bool:
        target, op, repeat = command.split()
        robot = self.robots[int(target)]
        if op == "F":
            return self._handle_move(robot, int(repeat))

        if op == "L":
            robot.rotate(Robot.LEFT, int(repeat))
        else:
            robot.rotate(Robot.RIGHT, int(repeat))
        return True

    def _handle_move(self, robot: "Robot", repeat: int) -> bool:
        old_pos = robot.pos
        trace = robot.move(repeat)

        for t in trace:
            if (other := self.position_map.get(t)) is not None:
                self.result_message = f"Robot {robot.number} crashes into robot {other}"
                return False
        nx, ny = robot.pos
        if not ((1 <= nx <= self.width) and (1 <= ny <= self.height)):
            self.result_message = f"Robot {robot.number} crashes into the wall"
            return False

        self.position_map.pop(old_pos)
        self.position_map[robot.pos] = robot.number
        return True


class Robot:
    N = 0
    E = 1
    S = 2
    W = 3
    STR_DIR_MAP = {"N": N, "E": E, "S": S, "W": W}
    DIR_DELTA_MAP = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    LEFT = -1
    RIGHT = 1

    def __init__(self, number: int, info: str):
        self.number = number

        x, y, d = info.split()
        self._x = int(x)
        self._y = int(y)
        self._dir = Robot.STR_DIR_MAP[d]

    @property
    def pos(self) -> Point:
        return (self._x, self._y)

    def rotate(self, to: int, repeat: int) -> None:
        self._dir = (self._dir + to * repeat) % 4

    def move(self, repeat: int) -> Generator[Point, None, None]:
        x, y = self._x, self._y

        d = Robot.DIR_DELTA_MAP[self._dir]
        self._x += d[0] * repeat
        self._y += d[1] * repeat

        # returns trace
        return (((x := x + d[0]), (y := y + d[1])) for _ in range(repeat))


if __name__ == "__main__":
    main()
