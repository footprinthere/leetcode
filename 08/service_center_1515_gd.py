from typing import Optional
from itertools import count

import numpy as np


class Solution:
    def getMinDistSum(self, positions: list[list[int]]) -> float:
        """TLE"""

        # Trivial cases
        if len(positions) == 1:
            return 0.0
        elif len(positions) == 2:
            p1, p2 = np.array(positions[0]), np.array(positions[1])
            return np.linalg.norm(p1 - p2)

        # Initialize with mean values
        sx, sy = 0, 0
        for pos in positions:
            sx += pos[0]
            sy += pos[1]
        center_init = np.array([sx, sy]) / len(positions)
        # print(f"{center_init = }")

        LR = 0.001
        model = DistanceModel(
            positions=positions,
            center_init=center_init,
            lr=LR,
            threshold=1e-6 / LR,
        )
        # print(f"{LR = } / threshold = {1e-7 / LR}")

        result = model.train()
        # print(f"{result = }")

        return model.loss()


class DistanceModel:
    def __init__(
        self,
        positions: list[list[int]],
        center_init,
        lr: float,
        threshold: float,
    ):
        self.positions = [np.array(pos) for pos in positions]
        self.center = center_init

        self.lr = lr
        self.threshold = threshold
        self.eps = 1e-7

    def loss(self) -> float:
        # center: (2,)
        output = 0.0
        for pos in self.positions:
            output += np.linalg.norm(self.center - pos)
        return output

    def train(self, max_steps: Optional[int] = None) -> bool:
        if max_steps is None:
            it = count()
        else:
            it = range(max_steps)

        for t in it:
            grad = self.step()
            # print(f"{t = } / {grad = }")
            if np.max(np.abs(grad)) < self.threshold:
                return True
        return False

    def step(self):
        """Performs a step of gradient descent"""
        grad = self.grad(self.center)
        self.center -= self.lr * grad
        return grad

    def grad(self, center):
        # center: (2,)
        output = 0.0
        for pos in self.positions:
            output += (center - pos) / (np.linalg.norm(center - pos) + self.eps)
        return output


if __name__ == "__main__":
    # positions = [[0, 1], [1, 0], [1, 2], [2, 1]]
    # positions = [[1, 1], [0, 0], [2, 0]]
    positions = [
        [44, 23],
        [18, 45],
        [6, 73],
        [0, 76],
        [10, 50],
        [30, 7],
        [92, 59],
        [44, 59],
        [79, 45],
        [69, 37],
        [66, 63],
        [10, 78],
        [88, 80],
        [44, 87],
    ]

    answer = Solution().getMinDistSum(positions)
    print(f"{answer = }")
