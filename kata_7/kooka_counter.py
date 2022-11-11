def kooka_counter(laughing):

    if len(laughing) == 0:
        return 0

    count = 1
    laughing = laughing.replace('a', '')

    for i in range(len(laughing) - 1):
        if laughing[i] != laughing[i + 1]:
            count += 1
        i += 1

    return count
