#!/usr/bin/env python3
import sys


def mean_temps(temps: list[int]) -> float:
    """
    params: list[int]: list of temperatures
    returns: float: mean of temperatures
    """
    total_temps = 0
    for temp in temps:
        total_temps += temp
    return total_temps//len(temps)


if __name__ == "__main__":
    trash = sys.stdin.readline().strip().split()
    data = sys.stdin.readline().strip().split()
    temps = [int(i) for i in data]
    print(mean_temps(temps))
