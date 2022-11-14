def open_or_senior(data):
    members = []
    i = 0
    while i < len(data):
        if data[i][0] >= 55 and data[i][1] > 7:
            members.append('Senior')
        else:
            members.append('Open')
        i += 1
    return members
