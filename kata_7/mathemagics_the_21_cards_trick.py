"""
Your task is to implement an algorithm that is able to execute the Twenty-One Card Trick.
To simplify things, the cards will be changed to the set of integers between 1 and 21(inclusive).
The function will be passed as argument a member of the audience that has selected a certain card and has a method
get_input that receives a list of 3 lists as arguments and returns the index of the column containing
the selected card.
"""
# The audience member will always select one of these options
DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]


def guess_the_card(audience):
    """
    audience has the method get_input, that receives a list of 3 lists as parameter
    and returns the index of the list where the selected card is present.
    This method can be called up to 3 times, after that it will throw an Exception.
    """
    arr = DECK
    for i in range(3):
        arr = list(zip(*zip(*[iter(arr)] * 3)))
        p = audience.get_input(arr)
        arr = [*arr.pop(p), *arr[0], *arr[1]]
    return arr[0]
