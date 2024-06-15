# pyright: reportArgumentType=false
# pyright: reportGeneralTypeIssues=false

import matplotlib.pyplot as plt
import random

CMD = 22
INIT_TEMP = 61


def change_temp(
        curr_temp: float,
        error: float,
        error_dot: float
) -> float:
    c = random.randint(-5, -1)
    h = random.randint(1, 5)

    if error_dot < 0:
        if error < 0: return curr_temp + c, "C"
        if error == 0 or error > 0: return curr_temp + h, "H"
    if error_dot == 0:
        if error < 0: return curr_temp + c, "C"
        if error == 0: return curr_temp, "NC"
        if error > 0: return curr_temp + h, "H"
    if error_dot > 0:
        if error < 0 or error == 0: return curr_temp + c, "C"
        if error > 0: return curr_temp + h, "H"


def main() -> None:
    error_hist = [CMD-INIT_TEMP]
    temp_hist = [INIT_TEMP]
    time_hist = [0]

    curr_temp = INIT_TEMP
    error_curr = CMD-INIT_TEMP
    error_prev = CMD-INIT_TEMP
    for t in range(1, 101):
        new_temp, _ = change_temp(curr_temp, error_curr, error_prev)

        curr_temp = new_temp
        temp_hist.append(new_temp)

        error_curr = CMD - new_temp
        error_prev = error_curr
        error_hist.append(error_curr)

        time_hist.append(t)

    print(temp_hist)

    plt.title("Temperature vs Time Graph")
    plt.xlabel("Time (s)"); plt.ylabel("Temperature (F)")
    plt.plot(time_hist, temp_hist, marker=".")
    plt.show()

    plt.title("Error vs Time Graph")
    plt.ylim(-5, 5)
    plt.xlabel("Time (s)"); plt.ylabel("Error (cmd - temp)")
    plt.plot(time_hist, error_hist, marker=".")
    plt.show()


if __name__ == "__main__":
    main()


