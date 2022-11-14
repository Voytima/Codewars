from math import floor


def get_positions(n):
    return n % 3, floor(n / 3) % 3, floor(n / 9) % 3
