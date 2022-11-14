def number_joy(n):
    b = sum(map(int, str(n)))
    rev_b = int(str(b)[::-1])
    return True if b * rev_b == n else False
