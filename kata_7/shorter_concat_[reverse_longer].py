def shorter_reverse_longer(a,b):
    return f"{b}{''.join(reversed(a))}{b}" if len(a) >= len(b) else f"{a}{''.join(reversed(b))}{a}"
