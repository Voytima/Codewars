def solution(frank, sam, tom):
    count = 0
    for i in range(4):
        for j in range(4):
            if frank[j] > sam[i] and frank[j] > tom[i]:
                count += 1
                frank[j] = 0
                break
    return count >= 2
