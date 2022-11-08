def swap(st):
    return "".join(i.capitalize() if i in "aeiou" else i for i in st)
