# The speeding car: "O='`o"
# The other cars: "X"
def car_crash(road):
    index = road.find("O='`o")
    lane = road[index::]
    if '\n' in lane:
        index2 = lane.find('\n')
        crash_check = lane[0:index2]
        if 'X' in crash_check:
            return True
        else:
            return False
    if 'X' in lane:
        return True
    else:
        return False
