def is_square(arr):
    return all(i ** 0.5 % 1 == 0 for i in arr) if arr else None
