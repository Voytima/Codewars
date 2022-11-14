from math import floor


def gps(s, x):
    max_speed = 0

    for i in range(1, len(x)):
        dist = x[i] - x[i - 1]
        speed = (3600 * dist) / s

        if speed > max_speed:
            max_speed = speed

    return floor(max_speed)
