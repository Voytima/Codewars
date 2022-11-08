import re


def contact(hallway):
    gaps = re.findall(r'>-*<', hallway)
    return min(map(len,gaps), default=-2) >> 1