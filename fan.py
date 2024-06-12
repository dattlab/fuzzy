import matplotlib.pyplot as plt

from utils import *


class FLcontroller:
    def __init__(self, target_temp: float = 22) -> None:
        self.target_temp = target_temp
        self.negative_pts = (Point(), Point(11, 1), Point(22))
        self.zero_pts = (Point(11), Point(22, 1), Point(33))
        self.positive_pts = (Point(22), Point(33, 1), Point(44))

    def get_negative_mf(self) -> float:
        ...

    def get_zero_mf(self) -> float:
        ...

    def get_positive_mf(self) -> float:
        ...


def main() -> None:
    y = []  # temp
    x = []  # time
    cmd = 22
    temp = 50
    error = cmd - temp

    y.append(temp); x.append(0)
    for i in range(1, 101):
        y.append()

    return 0


if __name__ == "__main__":
    main()
