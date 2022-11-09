def disemvowel(string_):
    return ''.join(i.replace(i, '') if i in "AEIOUaeiou" else i for i in string_)
