def solve(s):
    ups = 0
    lows = 0
    numbs = 0
    sp_chars = 0

    for i in s:
        if i.isalpha():
            if i.upper() == i:
                ups += 1
            elif i.lower() == i:
                lows += 1
        elif i.isdecimal():
            numbs += 1
        else:
            sp_chars += 1
    return [ups, lows, numbs, sp_chars]
