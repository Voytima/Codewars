def spoonerize(words):
    split_words = words.split(' ')
    return f"{split_words[1][0] + split_words[0][1:]} {split_words[0][0] + split_words[1][1:]}"
