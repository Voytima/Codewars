def sum_triangular_numbers(n):
    _sum = 0
    if n < 1:
        return 0
    else:
        while n > 0:
            _sum += (n*(n+1)//2)
            n -= 1
    return _sum
