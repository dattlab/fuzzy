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
        return trim_mf(self.temp, *self.cool_pts)

    def get_warm_mf(self) -> float:
        return trim_mf(self.temp, *self.warm_pts)

    def get_hot_mf(self) -> float:
        return trap_mf(self.temp, *self.hot_pts)

    def display_memvals(self) -> None:
        print(f"""
        Freezing Val.: {self.get_freezing_mf()}
        Cool Val.: {self.get_cool_mf()}
        Warm Val.: {self.get_warm_mf()}
        Hot Val.: {self.get_hot_mf()}""")


class CloudCover:
    def __init__(self, input_cover: float) -> None:
        self.cover = input_cover
        self.sunny_pts = (Point(), Point(), Point(20, 1), Point(40))
        self.partly_cloudy_pts = (Point(20), Point(50, 1), Point(80))
        self.overcast_pts = (Point(60), Point(80, 1), Point(), Point())

    def get_sunny_mf(self) -> float:
        return trap_mf(self.cover, *self.sunny_pts)

    def get_partly_cloudy_mf(self) -> float:
        return trim_mf(self.cover, *self.partly_cloudy_pts)

    def get_overcast_mf(self) -> float:
        return trap_mf(self.cover, *self.overcast_pts)

    def display_memvals(self) -> float:
        print(f"""
        Sunny Val.: {self.get_sunny_mf()}
        Partly Cloudy Val.: {self.get_partly_cloudy_mf()}
        Overcast Val.: {self.get_overcast_mf()}""")


class Speed:
    def __init__(self, temp: Temperature, cover: CloudCover) -> None:
        self.temp = temp
        self.cover = cover

    def get_fast_val(self) -> float:
        return min(self.cover.get_sunny_mf(), self.temp.get_warm_mf())

    def get_slow_val(self) -> float:
        return min(self.cover.get_partly_cloudy_mf(), self.temp.get_cool_mf())

    def display_memvals(self) -> float:
        print(f"""
        Fast Val.: {self.get_fast_val()}
        Slow Val.: {self.get_slow_val()}""")


def main() -> None:
    temp = Temperature(float(input("Temperature: ")))
    cover = CloudCover(float(input("Cloud Cover: ")))
    speed = Speed(temp, cover)

    temp.display_memvals()
    cover.display_memvals()
    speed.display_memvals()


if __name__ == "__main__":
    main()

