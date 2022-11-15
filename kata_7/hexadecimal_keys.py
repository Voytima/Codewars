def find_key(encryption_key):
    dec_num = int(encryption_key, 16)
    print(dec_num)
    divisors = []

    i = 2
    while i * i <= dec_num:
        if dec_num % i == 0:
            dec_num /= i
            divisors.append(i)
            divisors.append(dec_num)
            break
        else:
            i += 1

    return (divisors[0] - 1) * (divisors[1] - 1)
