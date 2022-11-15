from math import ceil


def movie(card, ticket, perc):
    tickets = 0
    times = 1

    while ceil(card) >= tickets:
        card += ticket * (perc ** times)
        tickets += ticket
        times += 1

    return times - 1
