import matplotlib.pyplot as plt

from utils import *


class Temperature:
    def __init__(self, input_temp: float) -> None:
        self.temp = input_temp
        self.freezing_pts = (Point(), Point(), Point(30, 1), Point(50))
        self.cool_pts = (Point(30), Point(50, 1), Point(70))
        self.warm_pts = (Point(50), Point(70, 1), Point(90))
        self.hot_pts = (Point(70), Point(90, 1), Point(), Point())

    def get_freezing_mf(self) -> float:
        return trap_mf(self.temp, *self.freezing_pts)

    def get_cool_mf(self) -> float:
        return tri_mf(self.temp, *self.cool_pts)

    def get_warm_mf(self) -> float:
        return tri_mf(self.temp, *self.warm_pts)

    def get_hot_mf(self) -> float:
        return trap_mf(self.temp, *self.hot_pts)

    def __str__(self) -> str:
        return f"""
        Freezing: {self.get_freezing_mf()}
        Cool: {self.get_cool_mf()}
        Warm: {self.get_warm_mf()}
        Hot: {self.get_hot_mf()}"""


class CloudCover:
    def __init__(self, input_cover: float) -> None:
        self.cover = input_cover
        self.sunny_pts = (Point(), Point(), Point(20, 1), Point(40))
        self.partly_cloudy_pts = (Point(20), Point(50, 1), Point(80))
        self.overcast_pts = (Point(60), Point(80, 1), Point(), Point())

    def get_sunny_mf(self) -> float:
        return trap_mf(self.cover, *self.sunny_pts)

    def get_partly_cloudy_mf(self) -> float:
        return tri_mf(self.cover, *self.partly_cloudy_pts)

    def get_overcast_mf(self) -> float:
        return trap_mf(self.cover, *self.overcast_pts)

    def __str__(self) -> str:
        return f"""
        Sunny: {self.get_sunny_mf()}
        Partly Cloudy: {self.get_partly_cloudy_mf()}
        Overcast: {self.get_overcast_mf()}"""


class Speed:
    def __init__(self, temp: Temperature, cover: CloudCover) -> None:
        self.temp = temp
        self.cover = cover
        self.get_speed()

    def get_fast_val(self) -> float:
        return min(self.cover.get_sunny_mf(), self.temp.get_warm_mf())

    def get_slow_val(self) -> float:
        return min(self.cover.get_partly_cloudy_mf(), self.temp.get_cool_mf())
    
    def get_speed(self) -> None:
        slow_val = self.get_slow_val()
        fast_val = self.get_fast_val()

        if slow_val > fast_val:
            p1 = Point(25, 1); p2 = Point(75)
        else:
            p1 = Point(25); p2 = Point(75, 1)
        self.breakpoint_slow = (slow_val - intercept(p1, p2)) / slope(p1, p2)
        self.breakpoint_fast = (fast_val - intercept(p1, p2)) / slope(p1, p2)

        self.xs = [x for x in range(1, 101)]
        self.ys = []
        for x in self.xs:
            if x < self.breakpoint_slow:
                self.ys.append(slow_val)
            elif x >= self.breakpoint_slow and x < self.breakpoint_fast:
                self.ys.append(slope(p1, p2) * x + intercept(p1, p2))
            elif x >= self.breakpoint_fast:
                self.ys.append(fast_val)

        self.speed = ((slow_val*25) + (fast_val*75))/(slow_val + fast_val)

    def __str__(self) -> str:
        return f"""
        FINAL SPEED: {self.speed}
        Fast: {self.get_fast_val()}
        Slow: {self.get_slow_val()}
        Slow Breakpoint: {self.breakpoint_slow}
        Fast Breakpoint: {self.breakpoint_fast}"""

    def plot_speed(self) -> None:
        plt.title("Speed Graph")
        plt.plot(self.xs, self.ys)
        plt.show()


def main() -> None:
    temp = Temperature(float(input("Temperature: ")))
    cover = CloudCover(float(input("Cloud Cover: ")))
    speed = Speed(temp, cover)

    print(temp)
    print(cover)
    print(speed)

    speed.plot_speed()


if __name__ == "__main__":
    main()
